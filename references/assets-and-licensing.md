# 素材、字体与许可

## 素材需求表

按镜头记录：类型、内容、时长、画幅、分辨率、情绪、使用位置、平台、许可状态和来源。类型包括 A-roll、B-roll、街景、风景、图片、屏幕录制、BGM、音效、图标、Logo、字体和封面参考。

## 优先来源

- OpenTracks（旧 DOVA-SYNDROME）：BGM、Jingle 和音效。官方许可通常允许个人/商业作品和在线视频背景使用；曲目或作曲者附加条件优先。不能把音源作为主要内容、单独分发或注册指纹系统。
- Pexels：图片和视频。检查人物、商标和地点权利，不把原始文件再分发为素材库。
- Pixabay：图片、视频、音乐和音效。检查具体条款、商标/人物权利和 Content ID 情况。
- YouTube Audio Library：适合 YouTube；逐曲确认署名要求，不能据此自动推断 Bilibili 许可。
- Google Fonts、Fontshare、SIL OFL/Apache 明确授权的字体：登记字体与许可证；不要下载来源不明的“商用免费字体”。

## Codex 搜索指令模板

```text
本视频会发布到 YouTube 和 Bilibili。根据镜头清单搜索可按许可使用的图片、街景/风景视频、BGM、音效和免费商用字体。
优先使用 OpenTracks、Pexels、Pixabay、Google Fonts、Fontshare 和官方音频库。
每项返回：名称、作者、原始页面、下载页、许可证、是否允许 YouTube、是否允许 Bilibili、是否允许商业/收益使用、署名要求、Content ID/指纹风险、使用位置和下载日期。
许可证不清楚、只有“no copyright”宣传、来自转载页或仅明确允许 YouTube 的项目标为待确认，不下载。
```

## 登记字段

`file_name, type, title, author, source_url, license_url, license_name, youtube_ok, bilibili_ok, commercial_ok, attribution_required, attribution_text, fingerprint_or_content_id, downloaded_at, used_at, notes`

将许可证页面和必要的截图/文本保存到 `licenses/source-pages/`，素材按 `assets/own-video`、`stock-video`、`images`、`music`、`sound-effects`、`fonts`、`graphics` 分类。
