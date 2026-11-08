"""Build a skill-only Codex plugin and a portable local-marketplace ZIP (stdlib only)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "youtube-bilibili-video-production"
MARKET = "youtube-bilibili-local"
SKILL_FILES = (
    "SKILL.md", "agents/openai.yaml",
    "references/assets-and-licensing.md",
    "references/production-workflow.md",
    "references/production-state.md",
    "references/cover-workflow.md",
    "references/descriptions-and-credits.md",
    "scripts/workflow_state.py",
)


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build() -> dict:
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    if manifest["name"] != NAME:
        raise ValueError("Unexpected plugin name")
    version = manifest["version"]
    if not all(part.isdigit() for part in version.split(".")) or len(version.split(".")) != 3:
        raise ValueError("Version must be numeric major.minor.patch")
    plugin = ROOT / "plugins" / NAME
    # Explicit source list: never copy project boards, logs, or machine-local state.
    copies = {ROOT / "plugin.json": plugin / "plugin.json",
              ROOT / "LICENSE": plugin / "LICENSE"}
    for rel in ("logo.png", "logo.svg"):
        copies[ROOT / "assets" / rel] = plugin / "assets" / rel
    for rel in SKILL_FILES:
        copies[ROOT / rel] = plugin / "skills" / NAME / rel
    for source, target in copies.items():
        if not source.is_file():
            raise FileNotFoundError(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    marketplace = ROOT / ".agents/plugins/marketplace.json"
    write_json(marketplace, {
        "name": MARKET,
        "interface": {"displayName": "YouTube+B站视频制作 · 本地插件"},
        "plugins": [{
            "name": NAME,
            "source": {"source": "local", "path": f"./plugins/{NAME}"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Creativity",
        }],
    })
    files = list(copies.values()) + [marketplace, ROOT / "README.md", ROOT / "install-plugin.ps1", ROOT / "LICENSE"]
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    archive = dist / f"{NAME}-plugin-{version}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(files):
            info = zipfile.ZipInfo(f"{NAME}-plugin/" + path.relative_to(ROOT).as_posix(), (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, path.read_bytes())
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="ascii")
    return {"plugin": str(plugin), "marketplace": str(marketplace), "archive": str(archive),
            "sha256": digest, "files": len(files), "skills": 1, "mcpServers": 0}


if __name__ == "__main__":
    print(json.dumps(build(), ensure_ascii=False, indent=2))
