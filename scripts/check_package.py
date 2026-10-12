#!/usr/bin/env python3
"""Offline structural checks. Does not execute Hermes or measure agent quality."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return None


for path in sorted(ROOT.rglob("*.json")):
    read_json(path)

sources = read_json(ROOT / "research/sources.json") or []
require(len(sources) == 20, "Expected 20 canonical research sources")
require(len({x.get("url") for x in sources}) == len(sources), "Duplicate canonical source URL")
for item in sources:
    require(bool(re.fullmatch(r"[0-9a-f]{40}", item.get("sha", ""))), f"Invalid source commit: {item.get('repo')}")
    require(bool(item.get("collected_at")), "Missing collection timestamp")

evidence = read_json(ROOT / "research/evidence.json") or []
require(bool(evidence), "Evidence inventory is empty")
require(len({x.get("url") for x in evidence}) == len(evidence), "Duplicate evidence URL")
evidence_urls = {x.get("url") for x in evidence}
for item in evidence:
    require(bool(re.fullmatch(r"[0-9a-f]{64}", item.get("sha256", ""))), "Invalid evidence hash")
    require(item.get("bytes", 0) > 0, "Empty evidence file")
    require(f"/blob/{item.get('sha')}/" in item.get("url", ""), "Evidence URL is not pinned")

cases = []
for line_no, line in enumerate((ROOT / "evals/cases.jsonl").read_text().splitlines(), 1):
    try:
        case = json.loads(line)
        cases.append(case)
        for key in ("id", "group", "title", "setup", "prompt", "expected", "failure_conditions", "judge"):
            require(bool(case.get(key)), f"Case line {line_no}: missing {key}")
        require(case.get("status") == "proposed-not-executed", "Seed case incorrectly labeled executed")
        require(case.get("data_type") == "synthetic", "Public seed case must be synthetic")
    except ValueError as exc:
        errors.append(f"Case line {line_no}: {exc}")
require(len(cases) == 30, "Expected 30 evaluation seed cases")
require(len({x["id"] for x in cases}) == len(cases), "Duplicate case ID")
require({x["group"] for x in cases} == {"UX", "CTX", "MEM", "TOOL", "OPS", "EVAL"}, "Missing scenario group")

for path in ROOT.rglob("*.md"):
    content = path.read_text()
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        if target.startswith(("https://", "http://", "#")):
            if target.startswith("https://github.com/") and "/blob/" in target:
                require(target in evidence_urls, f"{path.relative_to(ROOT)}: cited file not in evidence inventory: {target}")
            continue
        resolved = (path.parent / target.split("#", 1)[0]).resolve()
        require(resolved.is_relative_to(ROOT), f"Link escapes package: {target}")
        require(resolved.exists(), f"{path.relative_to(ROOT)}: missing relative link: {target}")

drafts = list((ROOT / "skills-drafts").glob("*/SKILL.md"))
require(len(drafts) == 3, "Expected three skill drafts")
for path in drafts:
    content = path.read_text()
    match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", content)
    require(bool(match), f"Invalid minimal frontmatter: {path.relative_to(ROOT)}")
    if match:
        require(match[1] == path.parent.name, "Skill name does not match directory")
        require(len(match[1]) <= 64 and "--" not in match[1] and not match[1].startswith("-") and not match[1].endswith("-"), "Invalid skill name")
        require(len(match[2]) <= 60, "Draft description exceeds Hermes house limit")
    sections = [content.find(f"## {name}") for name in ("When to Use", "Procedure", "Pitfalls", "Verification")]
    require(all(x >= 0 for x in sections) and sections == sorted(sections), "Missing/incorrect draft section order")

policy = read_json(ROOT / "configs/research-policy.json") or {}
require(policy.get("automatic_local_connection") is False, "Local connection must remain disabled")
require(policy.get("format") == "research-policy-v1-not-hermes-config", "Policy could be confused with native config")

if errors:
    print("Package check failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"PASS: {len(sources)} canonical sources, {len(evidence)} evidence files, {len(cases)} synthetic cases, {len(drafts)} skill drafts; JSON and documentation links valid.")
print("Scope: offline package structure only; no Hermes integration or A/B results.")
