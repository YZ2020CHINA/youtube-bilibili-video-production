# 阶段状态与确认记录

项目开始时创建 `production-state.json`。它是流程门控的事实来源，不能用文件是否存在代替用户确认。

```json
{
  "stage": 1,
  "status": "review",
  "revision": "r01",
  "confirmed_by_user": false,
  "confirmed_at": null,
  "artifacts": [],
  "open_questions": [],
  "change_log": []
}
```

`stage` 只能为 1–7；`status` 使用 `draft`、`review`、`confirmed`、`blocked`、`done`。进入下一阶段前必须写入 `confirmed_by_user: true`、确认时间和确认摘要。用户提出修改时增加 `revision`，把旧交付物标记为 superseded，并把修改原文写入 `change_log`。

建议的阶段目录：

```text
01-script/       brief.md, script.csv, assumptions.md
02-assets/       candidates.csv, approved.csv, source-pages/
03-storyboard/   storyboard.md, storyboard.png, animatic/
04-edit/         rough-cut/, project/
05-review/       review-notes.md, preview/
06-revision/     change-list.md, comparison/
07-delivery/     exports/, subtitles/, covers/, licenses/, verification.json
```

每个阶段的 `artifacts` 要写相对路径和用途；外部素材还要在 `licenses/asset-log.csv` 中登记。保存、复制和打开目录属于阶段 7 的最后确认：先让用户选择新目录、已有项目目录或只打开当前项目目录，再执行对应动作。

## 状态 helper

插件附带 `scripts/workflow_state.py`（Python 标准库，无第三方依赖）：

```powershell
python scripts/workflow_state.py init production-state.json
python scripts/workflow_state.py status production-state.json
python scripts/workflow_state.py artifact production-state.json --path 01-script/script.csv --purpose "已确认脚本"
python scripts/workflow_state.py advance production-state.json --summary "用户确认步骤1脚本和封面需求"
python scripts/workflow_state.py revise production-state.json --summary "用户要求缩短开头并更换封面标题"
python scripts/workflow_state.py validate production-state.json
```

`advance` 只应在用户明确确认后运行；它会把当前阶段写入确认历史并移动到下一阶段。`revise` 会增加修订号并将当前阶段退回 `review`。helper 不会代替对话确认，也不会执行文件复制或外部发布。
