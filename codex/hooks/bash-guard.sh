#!/usr/bin/env bash
# PreToolUse Bash guard for Claude Code.
# Reads tool input JSON on stdin; emits a permission decision JSON if the
# command should be denied or forced into a prompt.
set -u

cmd=$(jq -r '.tool_input.command // ""' 2>/dev/null)
[ -z "$cmd" ] && exit 0

emit() {
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"%s","permissionDecisionReason":"%s"}}\n' "$1" "$2"
  exit 0
}

# ===== DENY =====
echo "$cmd" | grep -qE '\.env(rc)?([^a-zA-Z]|$)' \
  && emit deny ".env access blocked"

echo "$cmd" | grep -qE '(curl|wget|fetch)[[:space:]].*\|[[:space:]]*(sh|bash|zsh|fish|python|python3|perl|ruby|node)([[:space:]]|$)' \
  && emit deny "remote download piped to interpreter"

echo "$cmd" | grep -qE '<\([[:space:]]*(curl|wget|fetch)[[:space:]]' \
  && emit deny "process-substitution remote download"

echo "$cmd" | grep -qE '(^|[[:space:];&|()])(eval|source|\.)[[:space:]].*\$\([[:space:]]*(curl|wget|fetch)[[:space:]]' \
  && emit deny "eval/source of remote download"

echo "$cmd" | grep -qE '(bash|sh|zsh|fish|python|python3|perl|ruby|node)[[:space:]]+-(c|e)[[:space:]]+["'\''][^"'\'']*\$\([[:space:]]*(curl|wget|fetch)[[:space:]]' \
  && emit deny "interpreter -c with remote download"

# ===== ASK (force prompt even if listed allow rules match) =====
echo "$cmd" | grep -qE '[;&|][[:space:]]*sudo([[:space:]]|$)' \
  && emit ask "chained sudo"

echo "$cmd" | grep -qE '[;&|][[:space:]]*(pip3?|conda|mamba|apt(-get)?|yum|dnf|npm|yarn|pnpm|gem|cargo|brew)[[:space:]]+([a-zA-Z0-9._-]+[[:space:]]+)*?(install|uninstall|remove|update|upgrade|add)([[:space:]]|$)' \
  && emit ask "chained package install"

echo "$cmd" | grep -qE 'find[[:space:]].*(-delete([[:space:]]|$)|-exec([[:space:]]|$))' \
  && emit ask "find with -delete/-exec"

exit 0
