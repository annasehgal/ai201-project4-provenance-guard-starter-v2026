# Milestone 1 — endpoint shapes and the false positive

## Endpoint shapes

### `POST /submit`

**In**

| Field | Type | Notes |
|---|---|---|
| `text` | string, required | Non-empty, at least a few words. |
| `creator_id` | string, optional | Defaults to `"unknown"`. |

**Out (200)**

| Field | Type | Notes |
|---|---|---|
| `content_id` | string | e.g. `c_36449a985840`. Needed to appeal. |
| `creator_id` | string | Echoed back. |
| `guess` | `"ai"` / `"human"` / `"unsure"` | Machine-readable. |
| `confidence` | float 0–1 | Combined score. Higher = more likely AI. |
| `label` | string | The sentence the writer sees. |
| `model_score` | float 0–1 | Signal one alone. |
| `style_score` | float 0–1 | Signal two alone. |
| `status` | string | `"decided"`. |

Missing, empty, or too-short `text` → `400` with `{"error": "bad_request", "message": "..."}`.

### `POST /appeal`

**In**

| Field | Type | Notes |
|---|---|---|
| `content_id` | string, required | From a previous `/submit` response. |
| `reasoning` | string, required | The writer's explanation. |

**Out (200)**

| Field | Type | Notes |
|---|---|---|
| `content_id` | string | Echoed back. |
| `status` | string | `"under_review"`. |
| `message` | string | Plain confirmation for the writer. |

Unknown `content_id` → `404`. Missing fields → `400`.

## Tracing the false positive

A writer submits a short essay they wrote themselves, in plain language —
common words, steady mid-length sentences, mostly full stops.

- **What score they get:** GPT-2 finds plain writing easy to predict, so the
  model score is high. Even sentence lengths and a modest vocabulary push the
  style score up too. Both signals point the same way, so the combined score
  lands high — somewhere around 0.65–0.75.
- **What the label says to them:** If my AI threshold sits too low, they see a
  high-confidence AI label on their own work. So the threshold has to sit high
  enough that a lean toward AI lands in "unsure" instead, and no label —
  including the AI one — says they cheated.
- **What they can do:** Send their `content_id` and reasoning to
  `POST /appeal`. The item moves to `under_review`, and the log keeps the
  original decision and the appeal side by side.

This already shows up in my own data: my `clearly_human` sample (a casual
first-person story) scored **0.44** on signal one, while the formal AI sample
scored **0.75**. A real human piece sitting that close to the middle is why the
unsure band needs to be wide.
