# YouTube+B站视频制作 · Codex 插件

将 `youtube-bilibili-video-production` skill 打包为 Codex 本地插件，版本 `1.2.1`。

采用七阶段确认制：脚本与需求确认 → 素材搜集确认 → 故事板确认 → 可编辑粗剪 → 视频细节确认 → 修改复核 → 成片与交付。步骤 1 和步骤 3 接入 `atuntun-xhs-cover`，逐项确认封面风格、主体参考、标题、构图和三种平台画板；每阶段停在确认门，最后询问保存目录或是否打开现有文件位置。插件附带无第三方依赖的 `workflow_state.py`，用于记录阶段确认、修订和交付物。`atuntun-xhs-cover` 需要单独安装；不可用时会明确说明并按同一顺序收集封面信息，不会虚称已调用。

## 视频说明

[观看《YouTube+B站视频制作 Codex 插件｜3分钟讲解》](https://youtu.be/Bdf3F31kUPw)

通过视频了解插件的七阶段制作流程，以及从脚本、素材和故事板确认到粗剪、修改与最终交付的使用方式。

## 安装

在本 GitHub 仓库点击 **Code → Download ZIP** 并完整解压，或使用 `git clone https://github.com/YZ2020CHINA/youtube-bilibili-video-production.git` 获取插件。随后按以下步骤安装：

1. 解压整个 ZIP 到准备长期保留的文件夹，例如 `D:\Apps\CodexPlugins\youtube-bilibili-video-production-plugin`，保留隐藏的 `.agents` 文件夹。
2. 在解压目录运行以下命令（需要当前支持 `codex plugin` 的 Codex CLI）：

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\install-plugin.ps1
   ```

3. 打开新的 Codex 聊天，选择 **YouTube+B站视频制作**，或者输入：

   ```text
   使用 $youtube-bilibili-video-production，从步骤 1 开始确认脚本和阿囤囤封面需求。
   ```

也可手动注册和安装：

```powershell
codex plugin marketplace add . --json
codex plugin add youtube-bilibili-video-production@youtube-bilibili-local --json
codex plugin list --marketplace youtube-bilibili-local --json
```

如果命令中找不到 `codex`，将可执行文件路径传给安装脚本的 `-CodexExe` 参数。`-CodexHome` 可指定独立配置目录。

本插件只提供工作流 skill，不包含 MCP 服务。HyperFrames、FilmCraft、PhotoCraft 及可选的阿囤囤封面 skill 需单独安装并连接；在缺少制作工具时仍可准备脚本、镜头表、许可登记和简介文案，执行前先确认实际可用工具。插件不会下载制作软件或替用户发布视频。`workflow_state.py` 是一个无第三方依赖的可选状态记录工具，支持初始化、记录交付物、阶段确认、修订和校验；它不会代替用户确认，也不会复制、移动、打开或上传媒体。

若之前安装过同名独立 skill，插件会保留它；出现两个同名入口时，可在 Codex 中选择插件所属入口。此安装器不会删除原 skill。

## 插件内容

```text
.agents/plugins/marketplace.json
plugins/youtube-bilibili-video-production/
  plugin.json
  assets/logo.png
  assets/logo.svg
  skills/youtube-bilibili-video-production/
    SKILL.md
    agents/openai.yaml
    references/assets-and-licensing.md
    references/cover-workflow.md
    references/production-workflow.md
    references/production-state.md
    references/descriptions-and-credits.md
    scripts/workflow_state.py
install-plugin.ps1
README.md
```

分发包不包含项目积木运行程序、画布数据、日志、缓存或绝对机器路径。插件没有账户认证或 API 密钥配置；后续实际使用的制作工具可能有各自要求。

## 重新打包（源项目）

在源项目执行 `python scripts/build_plugin.py`，会将原 skill 文件同步到插件目录，并在 `dist/` 生成 ZIP 与 `.zip.sha256`。构建只使用 Python 标准库；安装现成 ZIP 无需 Python。当前版本为 `1.2.1`，分发包包含 14 个白名单文件，不包含项目积木、视频工程、缓存或本机绝对路径。
