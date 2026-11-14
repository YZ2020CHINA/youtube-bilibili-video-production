# Remotion 动效与剪辑交接

在步骤 4 制作动效、步骤 5–6 调整预览或步骤 7 交付工程时读取本文件。Remotion 负责片头片尾、动态字幕、图表和补充动态图形，FilmCraft 负责主时间线与最终混音、输出。素材、脚本和故事板确认门沿用主工作流。

## 工程与依赖

- 开始制作前检查 Node.js、项目包管理器、Remotion 及所需制作工具是否可用；可用时遵循已安装的 Remotion skills。缺少依赖时说明缺项，在当前权限与授权范围内安装，不把本插件安装成功当作 Remotion 已配置成功。
- 在视频项目的 `projects/remotion/` 保留可编辑 React/TypeScript 工程，包括 `package.json`、对应包管理器的锁文件、入口、composition 源码和 `public/` 内获准使用的素材。沿用现有项目的包管理器；Remotion 与配套 `@remotion/*` 包使用匹配版本。交付不包含 `node_modules/` 和浏览器缓存。
- 每个片段记录 composition ID、宽高、fps、`durationInFrames`、props、素材相对路径与许可引用。动效由当前帧驱动，使用 `useCurrentFrame()`、`interpolate()`、`spring()` 等；不要依赖墙上时钟、CSS 自行播放的动画或未固定种子的随机数控制视频时间。
- Remotion 用于编排与渲染已有素材和图形。需要 AI 生成的画面时，另行使用适用的生成工具并记录来源与许可。

## 预览与确认

在 Remotion 工程目录启动 Studio：

```sh
npx remotion studio --no-open
```

用返回的实际 URL 在 Codex 面板打开预览，检查目标 composition 可加载且无缺失素材。若无法打开面板，保留服务并提供可访问的 URL；启动或加载失败时报告具体错误。步骤 4 展示源工程与预览，在步骤 5–6 根据时间码反馈修改，并保留修订记录。

粗剪阶段默认使用 Studio 预览。需要供 FilmCraft 导入的预渲染片段时，先取得该片段渲染的明确授权并记录；该授权不代表整片已通过验收。只有步骤 6 的最终剪辑确认后，才在步骤 7 导出整片。

## 片段渲染与交接

获准渲染后，从 Studio 导出或在项目目录执行，例如：

```sh
npx remotion render <composition-id> out/motion-clip.mp4
```

这是不透明片段的示例；需要透明叠加时，先核对 FilmCraft 实际支持的透明视频格式，选择双方兼容且保留 alpha 的编码，不能把普通 MP4 当作透明叠加。片段宽高与 fps 对齐主时间线，保留完整源工程后再导入 FilmCraft，并核对入点、出点、声音和字幕，避免重复叠加旁白或字幕。

在 `render-manifest.json` 记录每个片段的 composition ID、渲染参数、props、素材引用、输出相对路径，以及其在 FilmCraft 时间线中的使用位置。交付时提供实际使用的启动/渲染命令，检查首中末帧、时长、分辨率、fps、缺失素材和字体；没有实际运行的检查不得写成已通过。

插件自身采用 MIT；Remotion、字体、媒体及其他制作工具遵循各自许可，按实际使用场景核对 [Remotion 许可](https://www.remotion.dev/license)。
