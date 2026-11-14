# 制作与交付

## 七阶段门控与交付物

| 阶段 | 只做什么 | 必须展示 | 进入下一阶段的确认 |
| --- | --- | --- | --- |
| 1. 剧本、脚本确认 | 需求问卷、选题卡、逐句脚本、假设清单；调用阿囤囤 skill 逐项收集封面方向 | `script/brief.md`、`script/script.csv`、`cover/brief.md` 或等价文件、待决定问题 | 用户明确确认脚本/需求和封面需求，或给出修改意见后再次确认 |
| 2. 素材确认 | 候选检索、许可证核对、授权下载、分类整理 | 素材目录、候选比较、`licenses/asset-log.csv`、来源页面 | 用户明确确认素材清单；待确认素材不能进入正式制作 |
| 3. 故事板确认 | 逐镜头故事板、静音 animatic、镜头与声音锚点；用阿囤囤 skill 生成并确认 3:4 封面提示词，再改编三种平台画板 | 故事板图/HTML、时间码表、封面提示词、三种画板构图、可编辑源文件 | 用户明确确认故事板、封面提示词/构图和镜头顺序 |
| 4. 可编辑粗剪 | 建立多轨工程、导入确认素材、配音、BGM、字幕、片尾；建立 Remotion 动效与 Studio 预览 | `.fcproj`、Remotion 源工程、粗剪预览、独立轨道和媒体清单 | 用户看过粗剪并提交修改清单或确认进入细节修改 |
| 5. 细节确认 | 打开粗剪并收集修改意见 | 首/中/末段索引、问题清单、时间码 | 用户确认修改范围或确认无需修改 |
| 6. 修改复核 | 按清单改工程并重新预览 | 修订前后对照、变更清单、最新预览 | 用户明确确认最终剪辑 |
| 7. 成片交付 | 导出、字幕、封面、简介、署名、验收记录 | 最终文件包、`verification.json`、交付说明 | 验收完成后询问保存目录和是否打开现有位置 |

每一阶段都必须停在确认门。用户只说“看看”“继续准备”时，不得把它解释为确认。确认记录应写入项目的 `production-state.json`，并同步到项目积木画布。

## 步骤 1 的询问清单

一次性收集能影响脚本和素材的约束：主题、目标观众、发布平台、画幅、时长、语言、叙事目的、核心观点、开头钩子、语气、旁白音色/情绪、字幕语言、画面风格、实拍/录屏/素材比例、BGM/音效、封面规格、品牌元素、已有素材、来源限制、商业/收益、发布日期和验收标准。封面部分改用阿囤囤 skill 的一次一问顺序，依次确认风格、图 1 人物/主体参考、动作/表情、额外素材、背景色调、字体风格、字体颜色效果和标题。缺失项可以提出低风险假设，但要单列并等待用户确认。

## 步骤 7 的位置询问

完成验收后、任何外部复制或打开前，向用户提供三个清晰选项：

1. 保存到新目录（请用户给出路径）。
2. 复制到已有项目目录（请用户给出路径，并确认是否允许覆盖同名文件）。
3. 只打开当前项目目录，不复制文件。

若用户指定已有目录，先读取目录并报告将新增/覆盖的文件；除非用户明确允许，不覆盖现有文件。不要把“当前工作区”默认为用户最终保存位置。

## 脚本

脚本使用“时间段 / 旁白 / 画面 / 屏幕字幕 / 素材来源”表格。开头 5–15 秒先给结果、冲突或问题；主体按步骤或观点展开；结尾给结论和一个明确 CTA。

## 封面

使用阿囤囤小红书封面 skill 辅助人物参考、动作、表情、标题层级和色彩构图；它产出提示词，不直接生成图片。将 3:4 构思改成三个 PhotoCraft 画板：YouTube 16:9、Bilibili 16:9、Bilibili 4:3。保留可编辑 `.pcraft`，导出 PNG/JPG。文字、人物脸和核心主体留安全边距。

## 剪辑

FilmCraft 负责 A-roll/B-roll、配音、音乐、音量、转场、字幕、片尾署名和最终 MP4。Remotion 负责 React/TypeScript 片头片尾、动态图形、动态字幕和图表，先用 Studio 查看按帧驱动的动效，再把已确认且获准渲染的片段交给 FilmCraft。先锁定内容与声音，再做包装。Remotion 的工程、预览、片段渲染和媒体交接要求见 [remotion-workflow.md](remotion-workflow.md)。

## 署名

许可证强制署名的素材必须出现在片尾和平台简介；不强制的素材也可主动致谢。片尾显示简短版，简介保留作者、来源和许可证链接。不要把素材作者写成频道作者。

## 字幕

从最终音频生成 `video.zh-CN.srt`，校对后生成 `video.en-US.srt`。只交付 `.srt`，不生成 VTT/ASS。中文每行尽量不超过 20 个汉字，英文每行尽量不超过 42 个字符；剪辑变更后重新校正时间码。

## 文件交付

```text
exports/video-master-no-subtitles.mp4
exports/video-youtube.mp4
exports/video-bilibili.mp4
covers/cover-youtube-16x9.png
covers/cover-bilibili-16x9.png
covers/cover-bilibili-4x3.png
subtitles/video.zh-CN.srt
subtitles/video.en-US.srt
projects/filmcraft/*.fcproj
projects/remotion/package.json
projects/remotion/<依赖锁文件>
projects/remotion/src/
projects/remotion/public/
projects/remotion/render-manifest.json
projects/photocraft/*.pcraft
licenses/asset-log.csv
```

导出前抽查首、中、末段，确认无离线媒体、字幕同步、画面比例、声音电平、片尾署名和封面可读性。
