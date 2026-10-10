#!/usr/bin/env python3
"""Adapt Claude's command and filename policies to Codex PreToolUse."""
import fnmatch
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys

HOOKS = Path(__file__).resolve().parent


def command_parts(command):
    lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|\n")
    lexer.whitespace = " \t\r"
    lexer.whitespace_split = True
    parts, tokens = [], []
    for token in lexer:
        if token and all(char in ";&|\n" for char in token):
            if tokens:
                parts.append(" ".join(tokens))
                tokens = []
        else:
            tokens.append(token)
    if tokens:
        parts.append(" ".join(tokens))
    return parts


def sensitive_path(path):
    return any(part.startswith(".env") for part in path.replace("\\", "/").split("/"))


def command_reason(command):
    patterns = json.loads((HOOKS / "policy.json").read_text())["bash_deny"]
    for part in [command, *command_parts(command)]:
        for pattern in patterns:
            if fnmatch.fnmatchcase(part, pattern):
                return "Claude の禁止設定に一致します: " + pattern
    result = subprocess.run(
        ["bash", str(HOOKS / "bash-guard.sh")],
        input=json.dumps({"tool_input": {"command": command}}),
        capture_output=True, text=True, check=True,
    )
    if not result.stdout.strip():
        return None
    decision = json.loads(result.stdout)["hookSpecificOutput"]
    reason = decision["permissionDecisionReason"]
    # Codex cannot implement Claude's ask decision in PreToolUse.
    if decision["permissionDecision"] == "ask":
        return "操作を分けてください: " + reason
    return reason


def path_values(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"path", "file_path", "filename", "paths", "files"}:
                if isinstance(item, str):
                    yield item
                elif isinstance(item, list):
                    yield from (path for path in item if isinstance(path, str))
            if isinstance(item, (dict, list)):
                yield from path_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from path_values(item)


def decide(payload):
    args = payload.get("tool_input", {})
    tool = payload.get("tool_name", "")
    if tool in {"Bash", "exec_command"}:
        command = args.get("command", args.get("cmd", ""))
        return command_reason(command) if command else None
    if tool == "apply_patch":
        patch = args.get("command", args.get("patch", ""))
        for path in re.findall(r"^\*\*\* (?:Add File|Update File|Delete File|Move to): (.+)$", patch, re.M):
            if sensitive_path(path):
                return "Claude の禁止設定に一致します: **/.env*"
    for path in path_values(args):
        if sensitive_path(path):
            return "Claude の禁止設定に一致します: **/.env*"
    return None


def main():
    try:
        payload = json.load(sys.stdin)
        event = payload.get("hook_event_name", "PreToolUse")
        reason = decide(payload)
        if event == "PermissionRequest":
            if reason:
                decision = {"behavior": "deny", "message": reason}
            else:
                policy = json.loads((HOOKS / "policy.json").read_text())
                tool = payload.get("tool_name", "")
                args = payload.get("tool_input", {})
                command = args.get("command", args.get("cmd", ""))
                parts = command_parts(command) if tool in {"Bash", "exec_command"} else []
                allowed = (bool(parts) and all(any(
                    fnmatch.fnmatchcase(part, pattern) for pattern in policy["bash_allow"]
                ) for part in parts)) or tool in policy["tool_allow"] or (
                    tool == "apply_patch" and {"Edit", "Write"} <= set(policy["tool_allow"])
                )
                if not allowed:
                    return
                decision = {"behavior": "allow"}
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "PermissionRequest", "decision": decision,
            }}, ensure_ascii=False))
            return
    except (ValueError, TypeError, AttributeError, OSError, subprocess.SubprocessError):
        # Hook errors alone do not prevent Codex from running a tool.
        reason = "フックの入力・設定を処理できません。"
    if reason:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse", "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }}, ensure_ascii=False))


if __name__ == "__main__":
    main()
