# Skills

以下は、この README のあるディレクトリで実行する。

## サブモジュールのダウンロード

```bash
git submodule update --init --recursive
```

## サブモジュールの更新

```bash
git submodule update --remote
```

更新した参照コミットは、親リポジトリへコミットして記録する。

## シンボリックリンクの作成

初回のみ実行する。既存の実ディレクトリがある場合は、内容を共通の `./skills/` へ移し、元のディレクトリを退避してからリンクを作る。

```bash
mkdir -p skills
ln -s ../oh-my-mermaid/skills/omm-push skills/omm-push
ln -s ../oh-my-mermaid/skills/omm-scan skills/omm-scan
ln -s ../oh-my-mermaid/skills/omm-view skills/omm-view
ln -s ../mattpocock-skills/skills/engineering skills/engineering
ln -s ../mattpocock-skills/skills/productivity skills/productivity
ln -s ../skills/skills ../codex/skills
ln -s ../skills/skills ../claude/skills
```

自作スキルは `./skills/` 直下に実体を置く。外部スキルは同様にリンクを追加する。エージェント側はディレクトリ全体を参照するため、スキルごとのリンク追加は不要。

## omm のセットアップ

Node.js・npm が必要。CLI をローカルでビルドし、PATH に含まれる `~/.local/bin` にリンクする。

```bash
cd oh-my-mermaid
npm ci
npm run build
chmod +x dist/cli.js
mkdir -p "$HOME/.local/bin"
ln -s "$PWD/dist/cli.js" "$HOME/.local/bin/omm"
cd ..
omm --version
```

リンク作成は初回のみ。サブモジュールの更新後は `npm ci`・`npm run build`・`chmod +x dist/cli.js` を再実行する。
