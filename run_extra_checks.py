"""
The checks run_eval.py can't express. ← UNIT 8, MILESTONE 3

    python run_extra_checks.py --label before

Criterion 4 — appeals. Each trial submits 5 pieces, appeals each content_id,
and checks: the appeal returns 200, the response says `under_review`, and
GET /log shows the appeal right after the original decision. Then it appeals
a content_id that was never issued and checks for a 404 with no
`under_review` entry added.

Criterion 5, fourth request — a body that isn't a JSON object. scenarios.py
only accepts dict bodies, so it's sent from here. Passes on a 400.

Three trials, nothing changed in between. Output lands in results/.
Needs the service running in another terminal.
"""

import argparse
import datetime as dt
import json
import sys
import uuid

import requests

import config

APPEAL_TEXTS = [
    "I wrote this paragraph about my weekend myself. We went hiking and it rained the whole time, but it was still fun.",
    "My notes from class today were messy. The professor talked fast and I only got half of the examples written down.",
    "The bus was late again this morning, so I walked. It took forty minutes and I was late to my first lecture anyway.",
    "I cooked dinner for my roommates tonight. The rice burned a little, nobody complained, and we watched a movie after.",
    "Studying for the exam took longer than I planned. I kept getting stuck on the same practice problem until midnight.",
]
REASONING = "I wrote this myself; the label is wrong."


def appeal_trial(url, trial):
    """Criterion 4: 5 real appeals + 1 fake one."""
    appeals = []
    for i, text in enumerate(APPEAL_TEXTS, 1):
        creator = f"eval_appeal_t{trial}_{i}"
        sub = requests.post(f"{url}/submit", json={"text": text, "creator_id": creator}, timeout=60)
        sub_body = sub.json() if sub.content else {}
        content_id = sub_body.get("content_id")

        app = requests.post(f"{url}/appeal", json={"content_id": content_id, "reasoning": REASONING}, timeout=30)
        app_body = app.json() if app.content else {}

        entries = [e for e in requests.get(f"{url}/log", timeout=30).json()["entries"]
                   if e.get("content_id") == content_id]
        statuses = [e.get("status") for e in entries]
        recorded = statuses[:2] == ["decided", "under_review"]

        passed = (app.status_code == 200 and app_body.get("status") == "under_review" and recorded)
        appeals.append({
            "content_id": content_id,
            "submit_status": sub.status_code,
            "appeal_status": app.status_code,
            "appeal_response": app_body,
            "log_entries_for_id": entries,
            "passed": passed,
        })

    fake_id = f"c_fake{uuid.uuid4().hex[:8]}"
    fake = requests.post(f"{url}/appeal", json={"content_id": fake_id, "reasoning": REASONING}, timeout=30)
    fake_entries = [e for e in requests.get(f"{url}/log", timeout=30).json()["entries"]
                    if e.get("content_id") == fake_id]
    fake_result = {
        "content_id": fake_id,
        "appeal_status": fake.status_code,
        "appeal_response": fake.json() if fake.content else {},
        "log_entries_for_id": fake_entries,
        "passed": fake.status_code == 404 and not fake_entries,
    }
    return {"appeals": appeals, "fake": fake_result}


def non_object_trial(url):
    """Criterion 5, fourth request: a JSON array instead of an object."""
    body = ["text", "creator_id"]
    r = requests.post(f"{url}/submit", json=body, timeout=30)
    try:
        payload = r.json()
    except ValueError:
        payload = {"raw": r.text[:300]}
    return {"sent": body, "status": r.status_code, "response": payload,
            "passed": r.status_code == 400}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:5000")
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    args = parser.parse_args()

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py", file=sys.stderr)
        sys.exit(1)

    trials = []
    for t in range(1, args.trials + 1):
        a = appeal_trial(args.url, t)
        n = non_object_trial(args.url)
        ok = sum(x["passed"] for x in a["appeals"])
        print(f"trial {t}: appeals {ok}/5 · fake id {a['fake']['appeal_status']} "
              f"({'pass' if a['fake']['passed'] else 'FAIL'}) · non-object body {n['status']} "
              f"({'pass' if n['passed'] else 'FAIL'})")
        trials.append({"trial": t, "appeal": a, "non_object": n})

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"extra_checks_{stamp}{label}.md"
    lines = [
        f"# Extra checks{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_extra_checks.py::main` (appeals: `appeal_trial`, "
        "non-object body: `non_object_trial`)",
        f"- {args.trials} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "| Trial | Criterion 4: appeals passed | Criterion 4: fake id → 404, no entry | Criterion 5: non-object body → 400 |",
        "|---|---|---|---|",
    ]
    for tr in trials:
        a, n = tr["appeal"], tr["non_object"]
        lines.append(f"| {tr['trial']} | {sum(x['passed'] for x in a['appeals'])}/5 | "
                     f"{a['fake']['appeal_status']} ({'pass' if a['fake']['passed'] else 'FAIL'}) | "
                     f"{n['status']} ({'pass' if n['passed'] else 'FAIL'}) |")
    lines += ["", "## Full output", "", "```json", json.dumps(trials, indent=2, ensure_ascii=False), "```", ""]
    config.RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
