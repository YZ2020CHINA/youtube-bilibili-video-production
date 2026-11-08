"""Small stdlib-only state helper for the seven-stage video workflow.

The skill remains conversational: this helper records the user's confirmation,
revision history, and artifacts so a later turn can verify which gate is open.
It never copies, moves, opens, uploads, or deletes project media.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

STAGES = 7
STATUSES = {"draft", "review", "confirmed", "blocked", "done"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def default_state() -> dict:
    return {
        "stage": 1,
        "status": "draft",
        "revision": "r01",
        "confirmed_by_user": False,
        "confirmed_at": None,
        "confirmation_summary": "",
        "confirmation_history": [],
        "artifacts": [],
        "open_questions": [],
        "change_log": [],
    }


def read(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"state file does not exist: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit("state root must be an object")
    return value


def write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def validate(value: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(value.get("stage"), int) or not 1 <= value["stage"] <= STAGES:
        errors.append("stage must be an integer from 1 to 7")
    if value.get("status") not in STATUSES:
        errors.append(f"status must be one of {sorted(STATUSES)}")
    if not isinstance(value.get("revision"), str) or not value["revision"]:
        errors.append("revision must be a non-empty string")
    if not isinstance(value.get("confirmed_by_user"), bool):
        errors.append("confirmed_by_user must be boolean")
    for key in ("artifacts", "open_questions", "change_log", "confirmation_history"):
        if not isinstance(value.get(key), list):
            errors.append(f"{key} must be an array")
    if value.get("status") == "done" and value.get("stage") != STAGES:
        errors.append("only stage 7 may be done")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Record and validate video workflow stage gates")
    parser.add_argument("command", choices=("init", "status", "advance", "revise", "artifact", "validate"))
    parser.add_argument("state", type=Path)
    parser.add_argument("--summary", default="", help="user confirmation or revision summary")
    parser.add_argument("--path", dest="artifact_path", default="")
    parser.add_argument("--purpose", default="")
    args = parser.parse_args()

    if args.command == "init":
        if args.state.exists():
            raise SystemExit(f"refusing to overwrite existing state: {args.state}")
        value = default_state()
        write(args.state, value)
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return 0

    value = read(args.state)
    errors = validate(value)
    if errors:
        raise SystemExit("invalid state: " + "; ".join(errors))

    if args.command == "status":
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return 0
    if args.command == "validate":
        print(json.dumps({"valid": True, "stage": value["stage"], "status": value["status"]}, ensure_ascii=False))
        return 0
    if not args.summary and args.command in {"advance", "revise"}:
        raise SystemExit("--summary is required for advance/revise")

    timestamp = now()
    if args.command == "advance":
        if value["status"] not in {"draft", "review", "confirmed"}:
            raise SystemExit("only draft/review/confirmed stages can advance")
        current = value["stage"]
        record = {"stage": current, "revision": value["revision"], "summary": args.summary, "at": timestamp}
        value["confirmed_by_user"] = True
        value["confirmed_at"] = timestamp
        value["confirmation_summary"] = args.summary
        value["confirmation_history"].append(record)
        value["change_log"].append({"type": "stage-confirmed", **record})
        if current < STAGES:
            value["stage"] = current + 1
            value["status"] = "review"
            value["confirmed_by_user"] = False
            value["confirmed_at"] = None
            value["confirmation_summary"] = ""
        else:
            value["status"] = "done"
    elif args.command == "revise":
        number = int(value["revision"][1:]) if value["revision"].startswith("r") and value["revision"][1:].isdigit() else 1
        value["revision"] = f"r{number + 1:02d}"
        value["status"] = "review"
        value["confirmed_by_user"] = False
        value["confirmed_at"] = None
        value["confirmation_summary"] = ""
        value["change_log"].append({"type": "revision-requested", "summary": args.summary, "at": timestamp, "revision": value["revision"]})
    elif args.command == "artifact":
        if not args.artifact_path:
            raise SystemExit("--path is required for artifact")
        value["artifacts"].append({"path": args.artifact_path, "purpose": args.purpose, "stage": value["stage"], "revision": value["revision"]})
    write(args.state, value)
    print(json.dumps(value, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
