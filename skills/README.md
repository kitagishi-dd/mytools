# Skills

## スキル一覧

`skills/` 配下のスキル（リンク先・標準スキルを含む）。名前を指定して「google-review を使って変更をレビューして」のようにエージェントへ依頼する。

### 自作

| スキル | できること |
| --- | --- |
| [google-review](skills/google-review/SKILL.md) | Googleのガイドラインに沿ってコードをレビューする。 |

### oh-my-mermaid：構成図

| スキル | できること |
| --- | --- |
| [omm-scan](skills/omm-scan/SKILL.md) | コードを調べ、システムの構成図を生成・更新する。 |
| [omm-view](skills/omm-view/SKILL.md) | 構成図をブラウザで表示する。 |
| [omm-push](skills/omm-push/SKILL.md) | 構成図をクラウドへアップロードして共有する。 |

### Matt Pocock：開発

| スキル | できること |
| --- | --- |
| [ask-matt](skills/engineering/ask-matt/SKILL.md) | 状況に合うスキルと作業の進め方を提案する。 |
| [setup-matt-pocock-skills](skills/engineering/setup-matt-pocock-skills/SKILL.md) | 開発スキル用の課題管理・用語集・設計記録の設定を整える。 |
| [grill-with-docs](skills/engineering/grill-with-docs/SKILL.md) | 質問で計画を詰め、用語集と設計判断を記録する。 |
| [wayfinder](skills/engineering/wayfinder/SKILL.md) | 大規模な計画の未決事項を整理し、実装方針を固める。 |
| [research](skills/engineering/research/SKILL.md) | 公式資料などの一次情報を調べ、出典付きで記録する。 |
| [prototype](skills/engineering/prototype/SKILL.md) | UIやロジックを試すための使い捨て試作品を作る。 |
| [to-spec](skills/engineering/to-spec/SKILL.md) | 会話で決まった内容を仕様書にまとめ、課題管理へ登録する。 |
| [to-tickets](skills/engineering/to-tickets/SKILL.md) | 仕様や計画を、依存関係付きの実装チケットに分割する。 |
| [implement](skills/engineering/implement/SKILL.md) | 指定した仕様やチケットを実装し、テスト・レビューする。 |
| [implement-spec](skills/engineering/implement-spec/SKILL.md) | 仕様全体のチケットを複数エージェントで並列実装・統合する。 |
| [tdd](skills/engineering/tdd/SKILL.md) | テストを先に書いて、機能追加やバグ修正を進める。 |
| [diagnosing-bugs](skills/engineering/diagnosing-bugs/SKILL.md) | 難しいバグや性能低下を再現し、原因特定・修正する。 |
| [code-review](skills/engineering/code-review/SKILL.md) | 基準点からの変更を、コーディング規約と仕様の両面でレビューする。 |
| [pr](skills/engineering/pr/SKILL.md) | 変更内容と動作確認の証拠をまとめたPR本文を書く。 |
| [triage](skills/engineering/triage/SKILL.md) | 届いたIssueや外部PRを分類・検証し、対応に必要な情報を整理する。 |
| [codebase-design](skills/engineering/codebase-design/SKILL.md) | モジュールの責務・インターフェース・テストしやすさを設計する。 |
| [improve-codebase-architecture](skills/engineering/improve-codebase-architecture/SKILL.md) | 設計の改善候補をHTMLレポートにまとめ、選んだ案を詰める。 |
| [domain-modeling](skills/engineering/domain-modeling/SKILL.md) | プロジェクトの用語を整理し、用語集と設計判断を記録する。 |
| [wizard](skills/engineering/wizard/SKILL.md) | 認証設定など、人間の操作が必要な手順を対話型スクリプトにする。 |
| [retro](skills/engineering/retro/SKILL.md) | 開発セッションを振り返り、エージェントの作業環境の改善を提案する。 |

### Matt Pocock：相談・学習・引き継ぎ

| スキル | できること |
| --- | --- |
| [grilling](skills/productivity/grilling/SKILL.md) | 質問を重ね、計画やアイデアの曖昧さを解消する。 |
| [grill-me](skills/productivity/grill-me/SKILL.md) | grillingを呼び出し、計画や設計を質問で詰める。 |
| [to-questionnaire](skills/productivity/to-questionnaire/SKILL.md) | 他の人に確認したい事項を質問票にまとめる。 |
| [teach](skills/productivity/teach/SKILL.md) | 学びたい内容の教材を作り、継続的な学習を支援する。 |
| [wait-what](skills/productivity/wait-what/SKILL.md) | 分かりにくかった直前の説明を、背景から簡単な英語で説明し直す。 |
| [handoff](skills/productivity/handoff/SKILL.md) | 会話と作業状況を、次のエージェント向けの引き継ぎ文書にする。 |
| [writing-for-agents](skills/productivity/writing-for-agents/SKILL.md) | SKILL.md・AGENTS.mdなど、AI向けの指示文を作成・改善する。 |

### Codex標準

| スキル | できること |
| --- | --- |
| [imagegen](skills/.system/imagegen/SKILL.md) | イラスト・写真などの画像を生成・編集する。 |
| [openai-docs](skills/.system/openai-docs/SKILL.md) | CodexやOpenAI APIの使い方を公式資料で確認する。 |
| [skill-creator](skills/.system/skill-creator/SKILL.md) | スキルを新規作成・更新する。 |
| [skill-installer](skills/.system/skill-installer/SKILL.md) | 配布リストやGitHubからスキルをインストールする。 |
| [review-agent](skills/.system/review-agent/SKILL.md) | 別エージェントから委任された変更のレビューで、具体的な不具合を探す。 |

## セットアップ・更新

以下は、この README のあるディレクトリで実行する。

### サブモジュールのダウンロード

```bash
git submodule update --init --recursive
```

### サブモジュールの更新

```bash
git submodule update --remote
```

更新した参照コミットは、親リポジトリへコミットして記録する。

### シンボリックリンクの作成

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

### omm のセットアップ

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
