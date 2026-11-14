---
name: youtube-bilibili-video-production
description: Guide a confirmed, seven-stage YouTube and Bilibili video workflow from requirements and script through licensed assets, storyboard, editable rough cut, review rounds, and final delivery. Use when the user wants a repeatable cross-platform video workflow; never jump to a final export before the required confirmations.
metadata:
  short-description: 从剧本到 YouTube 与 B 站成片
---

# YouTube 与 Bilibili 视频制作

把用户的主题推进为可审查、可编辑、可发布的双平台视频项目。这个 skill 默认采用七阶段确认制；用户的“确认进入下一步”“需要修改”“返回上一步”是项目状态变更，不是闲聊。先读取本目录下与当前任务相关的参考文件：素材与许可查找用 `references/assets-and-licensing.md`，七阶段门控、文件状态和剪辑交付用 `references/production-workflow.md`，封面协作用 `references/cover-workflow.md`，简介和署名文案用 `references/descriptions-and-credits.md`。需要落盘或校验阶段时，可运行随 skill 提供的 `scripts/workflow_state.py`；它只记录状态，不复制、移动、打开或上传媒体。

## 七阶段确认制（必须遵守）

不要在一次回复或一次工具链中从需求直接生成最终成片。每个阶段只完成该阶段的交付物，打开或展示交付物，然后停在确认门；用户明确确认后才进入下一阶段。用户要求修改时，保留旧版本，更新修订号和变更记录，再次等待确认。只有用户明确要求“跳过某阶段”时，才可以跳过，并把跳过原因和用户原话记录到项目状态。

### 1. 剧本、脚本与需求确认

先尽可能完整地询问：主题、目标观众、平台、画幅、时长、发布语言、叙事目的、核心观点、开头钩子、语气、旁白音色和情绪、字幕语言、镜头风格、实拍/录屏/素材比例、BGM与音效、封面规格、品牌元素、素材来源限制、版权/商业使用、发布日期和验收标准。**在步骤 1 同时调用/遵循 `atuntun-xhs-cover` skill 的收集顺序，逐项确认封面风格、图 1 人物或主体参考、动作/表情、额外素材、背景色调、字体风格、字体颜色效果和封面标题。**它要求一次只问一个问题；不要把整套封面问卷一次性抛给用户，也不要杜撰人物或主体参考。若 `atuntun-xhs-cover` 未安装或不可用，明确说明未调用该 skill，仍按同一顺序收集信息，不要声称已经调用。将答案整理成选题卡、脚本表、封面需求卡和假设清单，逐句列出“时间段 / 旁白 / 画面 / 屏幕字幕 / 素材来源 / 许可状态”。

展示脚本、需求摘要和仍待决定的问题，明确说“当前停在步骤 1，等待脚本确认”。没有用户的明确确认，不搜集素材、不生成配音、不生成分镜或视频。

### 2. 素材搜集、下载与整理确认

仅在步骤 1 确认后，按照已确认的镜头清单搜索素材。先返回候选、原始页面、作者、许可证、YouTube/Bilibili/商业使用状态、署名和 Content ID/指纹风险；得到用户允许下载后再下载。按 `assets/own-video`、`stock-video`、`images`、`music`、`sound-effects`、`fonts`、`graphics` 分类，保存原始页面和许可证页面到 `licenses/source-pages/`，更新 `licenses/asset-log.csv`。

打开素材目录或在 Codex 面板展示目录清单，标出缺失、待确认和替代方案，明确说“当前停在步骤 2，等待素材确认”。素材未确认前不制作正式故事板；许可证不清楚的素材不得当作已批准素材使用。

### 3. 分镜脚本 / 故事板确认

仅使用步骤 1 已确认的脚本和步骤 2 已确认的素材，生成逐镜头故事板：时间码、镜头目的、构图、运动、旁白锚点、字幕、素材文件、转场、声音和许可引用。**在步骤 3 再次调用/遵循 `atuntun-xhs-cover` skill，把步骤 1 已确认的封面方向整理为一条完整的 3:4 竖版提示词，并展示人物/主体位置、标题层级、安全区、贴纸/图标、背景和色彩；随后和用户确认是否要把它改编为 YouTube 16:9、Bilibili 16:9 与 Bilibili 4:3 的封面构图。**封面方向、标题、主体参考、裁切和三种画板规格必须在故事板确认门一起确认。可生成低成本故事板图或静音 animatic，但不得把它称为成片。打开故事板、封面提示词和可编辑源文件，明确说“当前停在步骤 3，等待故事板与封面确认”。

### 4. 根据确认结果生成可编辑剪辑文件

只有故事板、封面方案和素材脚本全部确认后，才调用 Remotion、FilmCraft、PhotoCraft 或其他已连接工具。先生成可编辑的工程和粗剪：独立视频、旁白、BGM、音效、字幕和片尾署名轨道；保留媒体路径、版本号和项目清单。Remotion 动效保留 React/TypeScript 源码、依赖锁文件、素材与 composition 参数，并先打开 Studio 预览；具体交接见 [references/remotion-workflow.md](references/remotion-workflow.md)。此阶段不得替用户发布，也不得把粗剪标记为最终成片。打开剪辑工程或可播放预览，明确说“当前停在步骤 4，等待查看粗剪”。

### 5. 粗剪查看与视频细节确认

打开步骤 4 生成的剪辑文件或预览，提供首、中、末段和关键镜头的时间码索引。询问并记录：节奏、镜头顺序、画面裁切、文字、字幕、旁白、BGM、音效、转场、色调、封面一致性和片尾署名。等待用户给出“修改清单”或明确确认；不得直接将观看预览理解为通过。

### 6. 按修改清单调整并再次确认

按已记录的修改清单更新工程，逐项标记已改、无法改或需要用户决定的项目，保留修订前工程。重新打开预览并提供变更对照。只要用户还提出修改，就留在步骤 6；只有用户明确确认最终剪辑，才进入步骤 7。

### 7. 成片、后续交付与位置询问

确认后才导出无字幕母版、YouTube 版、Bilibili 版、中文/英文 SRT、三种封面、工程文件、简介、章节、署名和素材登记。执行首中末抽检、时长/分辨率/fps/音频/字幕/离线素材/署名/许可证检查，写入 `verification.json` 和交付说明。不要上传或发布，除非用户另行明确要求。

完成验收后，必须最后询问用户文件处理方式：“要把整套交付文件保存到哪个目录？需要打开现有文件位置吗？可选：保存到新目录、复制到已有项目目录、只打开当前项目目录。”在用户选择前不要擅自复制、移动、覆盖或打开用户未指定的外部目录；当前项目内的临时产物可以继续保留。

### 状态、回退与确认记录

在项目根目录维护阶段状态（例如 `production-state.json`）：`stage`, `status`, `revision`, `confirmed_by_user`, `confirmed_at`, `artifacts`, `open_questions`, `change_log`。每次确认写入用户确认的原文或简短准确摘要。项目积木画布应按这七个阶段建立卡片和依赖，阶段未确认时保持 `review`/`todo`，不要标记完成。用户要求返回上一步时，不删除后续文件，改为新修订目录或版本号并标记过期，避免误用旧素材或旧时间码。

## 工作原则

- 先确认主题、受众、平台、画幅、时长、语气和发布语言；信息缺失时做明确的低风险假设，并把假设写进项目记录。
- 把“免版权”改写为“许可证允许使用”。每个外部素材都保存原始页面、许可证页面、作者、下载日期、使用位置和许可备注。
- 这个视频同时发布到 YouTube 与 Bilibili，因此素材必须分别核对两个平台、商业使用和收益场景；只写“可用于 YouTube”的素材标为待确认。
- OpenTracks（原 DOVA-SYNDROME）可作为首选 BGM/音效来源。按曲目和作曲者条件使用；可剪辑和作为视频背景使用，但不把音乐作为主要内容，也不注册 Content ID、Bilibili 指纹或重新分发音频文件。
- 免费商用字体也要登记字体名、来源、版本、许可证和下载日期。优先使用 Google Fonts、Fontshare 或明确采用 SIL OFL/Apache 等许可的字体；不要把“免费”标题当作许可证明。
- 素材检索需要用户明确授权下载；先给候选和许可证据，再下载。使用原始页面，不使用搬运、转载或许可证不明的文件。

## 工具执行边界

Remotion、FilmCraft、PhotoCraft、配音、字幕和简介属于阶段 4–7 的执行工具。它们不能绕过阶段 1–3 的确认门：在没有已记录的脚本、素材清单和故事板确认时，不调用渲染、批量下载、配音或最终导出。阶段 4 先产出可编辑粗剪；阶段 5–6 负责观看、修改和复核；阶段 7 才生成无字幕母版、双平台视频、三个封面、两个 SRT、工程文件、简介和登记表。

完整的工具分工、文件结构和验收清单见 [references/production-workflow.md](references/production-workflow.md)。封面 skill 的调用边界和三种画板改编规则见 [references/cover-workflow.md](references/cover-workflow.md)。阶段状态字段和确认记录格式见 [references/production-state.md](references/production-state.md)。

## 工具分工

- **Codex**：选题、脚本、素材检索与许可核对、字幕和简介文案、各工具的操作编排。
- **Remotion**：用 React/TypeScript 制作按帧驱动的片头片尾、动态图形、动态字幕和图表；通过 Studio 预览，确认后将所需动效片段渲染交给 FilmCraft。它不直接生成 AI 视频素材。
- **FilmCraft**：主时间线、自己的视频素材、剪辑、混音、转场、最终视频导出。
- **PhotoCraft**：可修改的分层封面工程和 PNG/JPG 导出。

不要声称素材已获授权、文件已下载、工程已保存或视频已导出，除非实际检查到证据。用户未要求上传或发布时，只准备可交付文件和文案，不执行外部发布。
