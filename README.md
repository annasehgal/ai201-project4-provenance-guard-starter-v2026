# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. `POST /submit` (`app.py::submit`) receives JSON with `text` and `creator_id`.
2. Missing, empty, too-short or too-long (over 20,000 characters) text is refused with a `400` and logged; nothing else runs.
3. Signal one, `detector.py::model_signal`, scores how predictable the text is to GPT-2 (0–1, higher = more AI-like).
4. Signal two, `stylometry.py::style_signal`, scores the shape of the text — sentence-length spread, word variety, punctuation (0–1, higher = more AI-like).
5. `scoring.py::combine_signals` combines the two into one confidence score.
6. `scoring.py::score_to_label` turns that score into one of three labels and the sentence a reader sees.
7. A `content_id` is created, the decision is written to `logs/audit.jsonl`, and the JSON response goes back. If the writer disagrees, `POST /appeal` with that `content_id` moves it to `under_review`.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How *predictable* the text is to a language model.
`detector.py::model_signal` runs GPT-2 locally, computes perplexity (how
surprised the model is, word by word), and maps it to 0–1 with a logistic
curve centred on perplexity 45. Low perplexity → high score → more AI-like.

**Why that might differ between human and AI writing:** A language model
writes by picking likely next words, so its output is text a model finds easy
to predict. People make odder choices — a specific name, an abrupt turn, a
word that's slightly wrong but theirs.

**What it can't see:** Who wrote it. Predictability is not authorship. It
rewards common words in ordinary sentences, so plain writers — second-language
writers, younger writers, anyone writing simply on purpose — score as
machine-like. The reverse fails too: AI text asked to be ornate, or with rare
words swapped in, scores as human because rare words are what the model can't
predict. It also only reads the first ~400 tokens.

### Signal two — the style signal

**What it measures:** The *shape* of the text, without reading a word of it:
how much sentence lengths vary (stdev ÷ mean of words per sentence), how much
vocabulary repeats (unique words ÷ total words, averaged over 50-word
windows), and how much varied punctuation (commas, semicolons, colons, dashes,
brackets, quotes, ! and ?) appears per word. Built in
`stylometry.py::style_signal`.

**Why that might differ between human and AI writing:** Generated prose tends
toward even, mid-length sentences and plain punctuation. Human writing is
lumpier — a three-word sentence next to a forty-word one, dashes and asides.
I expected AI to have narrower vocabulary too, but on my samples it was the
opposite: the AI text avoided repeating words, while the human text repeated
"I", "the" and names, so high word variety counts as AI-like.

**What it can't see:** Meaning. Anything that changes the shape without
changing the substance moves it: splitting or merging sentences, sprinkling
in dashes and commas, pasting in a quotation. All of that is cheap to do on
purpose. Typos raise word variety, which my signal reads as *more* AI-like —
so a human with messy spelling could be pushed toward an accusation. Under 3
sentences, sentence-length spread can't be measured at all and counts as
neutral.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** A plain weighted average of the two signals, 50/50. Both
signals point the same way (higher = more AI-like), so the combined score does
too. When they disagree, the average lands in the middle on purpose: two
methods disagreeing is uncertainty, and "unsure" is the honest answer.

The style signal itself averages three measures equally, each mapped to 0–1
AI-ness: sentence-length spread (low = AI), word variety (high = AI — this
runs the opposite way to what I expected; on my samples the AI text avoided
repeating words and the human text didn't), and punctuation per word (low =
AI). Under 3 sentences, spread counts as neutral (0.5).

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5`,
`HUMAN_THRESHOLD = 0.35`, `AI_THRESHOLD = 0.70` (in `config.py`). I raised the
AI threshold from 0.65 to 0.70 because my formal human sample scored 0.64 —
one model wobble from being accused.

| Input | model | style | combined | guess |
|---|---|---|---|---|
| clearly AI | 0.754 | 0.889 | 0.822 | ai |
| clearly human | 0.445 | 0.075 | 0.260 | human |
| formal human | 0.677 | 0.596 | 0.637 | unsure |
| lightly-edited AI | 0.726 | 0.833 | 0.779 | ai |

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
My clearly-human sample (a casual first-person story) scored 0.445 on the
model signal — nearly unsure — but 0.075 on the style signal, because its
sentence lengths swing widely and it's full of dashes and commas. The 50/50
average puts it at 0.260, which is high-confidence human. The style signal
pulled it to the right side here; the risk is the reverse case, where plain
human writing scores AI-ish on both signals and nothing pulls it back. That is
the formal human sample (0.637), and the 0.70 threshold is what keeps it in
unsure.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 (inclusive) | We think this was probably written by a person. |
| unsure | above 0.35, below 0.70 | Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review. |
| high-confidence AI | 0.70 – 1.00 (inclusive) | Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it. |

The text lives in `scoring.py` (`LABEL_HUMAN`, `LABEL_UNSURE`, `LABEL_AI`).
All three are reachable: `clearly_human.json` scored 0.260 (human),
`formal_human.json` 0.637 (unsure), `clearly_ai.json` 0.822 (AI).

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It describes what the *check* did ("gave mixed results"), not what the writer
did, so it can't be read as an accusation. "We're not making a call" tells
them nothing bad has happened, and offering a review gives them something to
do if it still bothers them — without implying they need to defend
themselves.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d @samples/clearly_ai.json
```

```json
{
  "confidence": 0.8217,
  "content_id": "c_072ce8ceab20",
  "creator_id": "demo_instructor",
  "guess": "ai",
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "model_score": 0.7544,
  "status": "decided",
  "style_score": 0.8891
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "c_072ce8ceab20", "reasoning": "I wrote this myself for a workplace newsletter. It sounds formal because that is the house style."}'
```

```json
{
  "content_id": "c_072ce8ceab20",
  "message": "Thanks \u2014 your appeal has been recorded and a person will review this piece.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.8217,
      "content_id": "c_072ce8ceab20",
      "creator_id": "demo_instructor",
      "guess": "ai",
      "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
      "model_score": 0.7544,
      "status": "decided",
      "style_score": 0.8891,
      "timestamp": "2026-11-04T02:52:25+00:00"
    },
    {
      "content_id": "c_072ce8ceab20",
      "creator_id": "demo_instructor",
      "event": "appeal",
      "reasoning": "I wrote this myself for a workplace newsletter. It sounds formal because that is the house style.",
      "status": "under_review",
      "timestamp": "2026-11-04T02:52:25+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1 — choosing my acceptance criteria**

- *What I asked for:* Help making Milestone 2 easier, without the AI writing
  my criteria for me.
- *What came back:* Instead of finished criteria, Claude gave me
  multiple-choice options for the target in each area (e.g. 0, 1 or 2 false
  positives out of 10; a 0.20 vs 0.30 score gap), with the trade-off of each.
  When I asked it to also draft the "why" lines, it did, and pointed out that
  my own clearly-human sample already scored 0.44 on the model signal.
- *What I changed:* I picked every number myself — including keeping "at most
  2 of 10" when it asked me to confirm I could defend it — and chose to reject
  enormous text with a 400 instead of scoring it. I reviewed the reasons
  before committing them.

**Moment 2 — building the style signal and the combining rule**

- *What I asked for:* To build the three stylometry measures and test both
  signals on the same inputs, including formal human writing and
  lightly-edited AI.
- *What came back:* A side-by-side table. It showed word variety runs
  backwards from the starter's assumption (the AI text had *more* varied
  vocabulary), and that my formal human sample scored 0.64 combined — just
  under the default 0.65 AI threshold. It offered four combining rules and
  three threshold settings.
- *What I changed:* I chose a plain 50/50 average over the model-weighted and
  "disagreement guard" options, and raised the AI threshold from 0.65 to 0.70
  so formal human writing lands in "unsure" instead of one wobble from an
  accusation. I also picked the wording of all three labels from the options
  it gave.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
A real writer submits their own piece, maybe edits it and checks again, so a
few submissions an hour. Five a minute leaves room for a quick
resubmit-after-a-typo burst without them ever seeing a 429. Fifty a day covers
even a heavy day of drafting. A script trying to map my 0.35 / 0.70 thresholds
needs hundreds or thousands of variations. At 5/minute that takes hours instead
of seconds, and the 50/day cap means one caller can't finish the job in a day.
I lowered the starter's 10/minute and 200/day because nothing a real writer
does needs 200 checks a day. Those numbers mostly helped a prober.

**What a caller counts as:** per `creator_id`, falling back to IP address
when no creator_id is sent. That fits a household or classroom sharing one
address, since each writer gets their own budget. The weakness is that
creator_id is just a string the caller picks, so a script can rotate it
(`bot1`, `bot2`, …) and look like a thousand separate writers. The per-address
fallback only catches callers that leave the field out.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

Full run with every response: `results/attack_run_2026-11-04_1740_before.md`
(produced by `run_attacks.py::main`, 56 attacks, 2026-11-04 17:40). Thresholds
at the time of the run: below 0.35 = human, 0.35–0.70 = unsure, 0.70 and up = ai.

**How I marked held vs. broke**

| Family | HELD if… | BROKE if… |
|---|---|---|
| evasion (AI text) | it still came back `ai` | it came back `unsure` or `human`, i.e. it escaped the AI label it was aiming to escape |
| false_positive (human text) | it came back `human` or `unsure` (no accusation, review offered) | it came back `ai`, i.e. a real writer got accused |
| prompt_injection | the instruction changed nothing about how the service behaved | the guess, label text or audit log did what the instruction asked |
| malformed | clean, logged 400, or a 200 that makes no call | crash/5xx, a confident `ai`/`human` verdict on something that isn't writing, or bad data written to the log |
| flood_same_creator | 429s start once the creator passes 5/minute | requests past the limit still get through |

**Results**

| Family | Attacks | Held | Broke |
|---|---|---|---|
| evasion | 10 | 4 | **6** |
| false_positive | 8 | 3 | **5** |
| prompt_injection | 6 | 6 | 0 |
| malformed | 20 | 15 | **5** |
| flood_same_creator | 12 | 12 | 0 |
| **Total** | **56** | **40** | **16** |

| ID | Targeting | Status | Guess | Score | Model | Style | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | signal two: typos raise word variety | 200 | unsure | 0.582 | 0.164 | 1.000 | **BROKE** |
| EV02 | signal two: broken-up sentences raise length spread | 200 | unsure | 0.605 | 0.594 | 0.616 | **BROKE** |
| EV03 | signal two: a pasted quotation changes the shape | 200 | ai | 0.739 | 0.666 | 0.812 | HELD |
| EV04 | signal one: unusual words raise perplexity | 200 | ai | 0.806 | 0.611 | 1.000 | HELD |
| EV05 | both signals: heavy human editing pass | 200 | unsure | 0.434 | 0.321 | 0.547 | **BROKE** |
| EV06 | signal two: one very long sentence and one very short | 200 | unsure | 0.529 | 0.573 | 0.486 | **BROKE** |
| EV07 | signal two: padding with punctuation | 200 | unsure | 0.449 | 0.586 | 0.312 | **BROKE** |
| EV08 | signal one: text below the token window | 200 | unsure | 0.539 | 0.245 | 0.833 | **BROKE** |
| EV09 | both: AI text with a human opening paragraph bolted on | 200 | ai | 0.795 | 0.704 | 0.886 | HELD |
| EV10 | signal two: repeated stanza structure | 200 | ai | 0.797 | 0.979 | 0.615 | HELD |
| FP01 | plain, clear human writing with no flourishes | 200 | unsure | 0.628 | 0.618 | 0.638 | HELD |
| FP02 | human writing in a formal register | 200 | ai | 0.703 | 0.739 | 0.667 | **BROKE** |
| FP03 | a non-native English speaker writing carefully | 200 | ai | 0.772 | 0.805 | 0.739 | **BROKE** |
| FP04 | a student essay written to a rubric | 200 | ai | 0.777 | 0.833 | 0.721 | **BROKE** |
| FP05 | technical documentation written by a person | 200 | ai | 0.734 | 0.801 | 0.667 | **BROKE** |
| FP06 | a person imitating a formal template | 200 | ai | 0.713 | 0.881 | 0.545 | **BROKE** |
| FP07 | human writing that repeats a phrase deliberately | 200 | unsure | 0.654 | 0.882 | 0.427 | HELD |
| FP08 | very short genuine human submission | 200 | unsure | 0.624 | 0.322 | 0.926 | HELD |
| PI01 | instruction to ignore the check | 200 | unsure | 0.631 | 0.463 | 0.799 | HELD |
| PI02 | instruction disguised as a system message | 200 | unsure | 0.495 | 0.204 | 0.786 | HELD |
| PI03 | instruction wrapped in the writer's voice | 200 | ai | 0.748 | 0.594 | 0.901 | HELD |
| PI04 | attempt to make the label text hostile | 200 | unsure | 0.565 | 0.500 | 0.631 | HELD — label is a fixed string; the `<script>` never reaches it |
| PI05 | attempt to inject into the audit log | 200 | unsure | 0.570 | 0.640 | 0.500 | HELD — the log line is intact (text is escaped by `json.dumps`, no fake `"guess": "human"` field appeared) |
| PI06 | instruction plus real human text | 200 | unsure | 0.608 | 0.558 | 0.658 | HELD |
| MF01 | text is only whitespace | 400 | — | — | — | — | HELD (logged `missing_or_empty_text`) |
| MF02 | text is a single character | 400 | — | — | — | — | HELD (logged `text_too_short`) |
| MF03 | text is control characters | 200 | unsure | 0.417 | 0.000 | 0.833 | HELD — no call made, but it was scored at all |
| MF04 | text is only punctuation | 200 | human | 0.339 | 0.011 | 0.667 | **BROKE** — certified punctuation as human writing |
| MF05 | text is a very long single word | 200 | ai | 0.916 | 0.998 | 0.833 | **BROKE** — `aaaa…` labelled AI with the highest score of the run |
| MF06 | text is emoji only | 200 | ai | 0.749 | 0.997 | 0.500 | **BROKE** — emoji labelled AI |
| MF07 | text is right-to-left script | 200 | ai | 0.703 | 0.906 | 0.500 | **BROKE** — Arabic writing labelled AI |
| MF08 | text is 60,000 characters | 400 | — | — | — | — | HELD (logged `text_too_long`, length 57640) |
| RQ01 | no text field at all | 400 | — | — | — | — | HELD |
| RQ02 | no creator_id | 200 | unsure | 0.536 | 0.240 | 0.833 | HELD (logged as `unknown`) |
| RQ03 | text is a number | 400 | — | — | — | — | HELD |
| RQ04 | text is a list | 400 | — | — | — | — | HELD |
| RQ05 | text is null | 400 | — | — | — | — | HELD |
| RQ06 | creator_id is an object | 200 | unsure | 0.441 | 0.049 | 0.833 | **BROKE** — `{"id": "x"}` written into the log's `creator_id` field |
| RQ07 | body is a JSON array, not an object | 400 | — | — | — | — | HELD |
| RQ08 | body is unparseable JSON | 400 | — | — | — | — | HELD |
| RQ09 | body is empty | 400 | — | — | — | — | HELD |
| RQ10 | body is form-encoded, not JSON | 429 | — | — | — | — | HELD* |
| RQ11 | body is JSON claiming to be plain text | 429 | — | — | — | — | HELD* |
| RQ12 | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01–05 | 20 rapid submissions from one creator | 200 | unsure | 0.431 | 0.029 | 0.833 | HELD (within the 5/minute limit) |
| FL01_06–12 | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD (limited and logged) |

\* RQ10 and RQ11 never reached my route. They had no usable creator_id, so the
limiter counted them against my IP address. RQ02, RQ06, RQ07, RQ08 and RQ09
had already used that address's 5 requests for the minute (the 400s count too).
They're logged as `rate_limited`, so nothing went missing, but this run doesn't
tell me how my route would handle a form-encoded or `text/plain` body.

**Ten audit log entries from the run** (from `logs/audit.jsonl`)

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-05T01:40:22+00:00", "content_id": "c_d0a4dda5800c", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.7386, "combined_score": 0.7719, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:22+00:00", "content_id": "c_c26b711e664b", "creator_id": "attacker_FP04", "guess": "ai", "model_score": 0.8329, "style_score": 0.7209, "combined_score": 0.7769, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:21+00:00", "content_id": "c_cfaa6d059ea1", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.6667, "combined_score": 0.7027, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:21+00:00", "content_id": "c_d36e6ab03224", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 1.0, "combined_score": 0.5817, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:21+00:00", "content_id": "c_ea9b1c5822af", "creator_id": "attacker_EV08", "guess": "unsure", "model_score": 0.2452, "style_score": 0.8333, "combined_score": 0.5393, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:23+00:00", "content_id": "c_0a91610245c5", "creator_id": "attacker_MF05", "guess": "ai", "model_score": 0.9976, "style_score": 0.8333, "combined_score": 0.9155, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:23+00:00", "content_id": "c_c2ab33239717", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 0.5, "combined_score": 0.7032, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:22+00:00", "content_id": "c_ea99cac48c7b", "creator_id": "attacker_MF04", "guess": "human", "model_score": 0.0112, "style_score": 0.6667, "combined_score": 0.3389, "label": "We think this was probably written by a person.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:23+00:00", "content_id": "c_91c3955cd34b", "creator_id": {"id": "x"}, "guess": "unsure", "model_score": 0.0492, "style_score": 0.8333, "combined_score": 0.4413, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:22+00:00", "content_id": "c_d88d4b8a63be", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.5, "combined_score": 0.57, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "status": "decided"}
{"timestamp": "2026-11-05T01:40:23+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-05T01:40:23+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

Why these: three of the five false accusations (FP02 only just over the line at
0.7027), two evasions where the two signals pulled in opposite directions
(EV01: model 0.16, style 1.0), junk that got a confident verdict (MF04 `human`,
MF05 `ai` at 0.92, Arabic MF07 `ai`), an object written into the `creator_id`
field (RQ06), the log-injection attempt with its line intact (PI05), and two
rejections: one from the flood rows and one from the requests with no
creator_id that were counted against my IP address (RQ10/RQ11).

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03: a non-native English speaker writing carefully about their first month
in a new country.** My service told them their writing was "likely generated
with AI" (combined 0.7719; model 0.8051, style 0.7386). Both signals put it
above the AI line on their own, so no single signal disagreed and it wasn't a
borderline call. It's the writer who's most likely to be doubted already, and
the one with the least power to argue back.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

Criteria 1, 2, 3 and three of the four criterion 5 requests ran through
`run_eval.py --label before` using the inputs in `scenarios.py`
→ `results/run_2026-11-04_1824_before.md`.
`run_eval.py` only calls `/submit`, so I wrote **`run_extra_checks.py`** for
criterion 4 (submit, appeal, then read `GET /log`) and for criterion 5's fourth
request (a body that isn't a JSON object, which `scenarios.py` can't express)
→ `results/extra_checks_2026-11-04_1824_before.md`. Both ran three trials
back to back with nothing changed in between.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing labelled AI | ≤ 2 of 10 | 1/10 | 1/10 | 1/10 | **MET** |
| 2. AI mean minus human mean (combined score) | ≥ 0.30 | 0.355 (0.818 − 0.463) | 0.355 | 0.355 | **MET** |
| 3. Each label appears ≥ 2 times in 9 inputs | 3 of 3 labels | 2/3 (ai 5, unsure 4, human 0) | 2/3 (same) | 2/3 (same) | **MISSED** |
| 4. Real appeals → 200 + `under_review` + logged; fake id → 404, no entry | 5/5 + fake 404 | 5/5 + 404 | 5/5 + 404 | 5/5 + 404 | **MET** |
| 5. Bad requests → 400, none → 500 | 4 of 4 | 4/4 | 4/4 | 4/4 | **MET** |

All three trials were identical for every criterion, down to the fourth
decimal. Neither signal has randomness in it, so that's expected.

**Inputs:** criterion 1 is ten pieces I wrote myself, pasted with their typos.
Criterion 2's AI group is the unit 7 `clearly_ai` sample plus four paragraphs
generated by Claude; its human group is the unit 7 `clearly_human` sample plus
my pieces 1–4 (picked by number, not by score). Criterion 3 is three more
Claude paragraphs, my pieces 6–8, and three borderline texts (`borderline`,
`edited_ai`, and an AI paragraph I rewrote casually by hand). Criteria 2 and 3
reuse some of my own writing from criterion 1 because I had no other
guaranteed-human text that a language model hasn't memorised.

**Real output from one trial (trial 1 of each)**

Criterion 1 — `run_eval.py::main`, scenario `c1 my own writing`
(`results/run_2026-11-04_1824_before.md`). Piece 2 is the one labelled AI:

```json
[
  {"status": 200, "guess": "unsure", "confidence": 0.4823, "model_score": 0.5583, "style_score": 0.4063, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "As I started my university, I realized I did belong at CSU Chico; the "},
  {"status": 200, "guess": "ai", "confidence": 0.7408, "model_score": 0.6735, "style_score": 0.808, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "There is beauty in smiling after going through a rough patch. I truly "},
  {"status": 200, "guess": "unsure", "confidence": 0.4763, "model_score": 0.48, "style_score": 0.4727, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "Why is that we compare ourselves to something else, when they say that"},
  {"status": 200, "guess": "unsure", "confidence": 0.3578, "model_score": 0.2498, "style_score": 0.4657, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "I love how our fandom consists of people from different backgrounds. I"},
  {"status": 200, "guess": "unsure", "confidence": 0.5379, "model_score": 0.5135, "style_score": 0.5624, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "I actually hated the color Blue for a long time. I have a whole story "},
  {"status": 200, "guess": "unsure", "confidence": 0.4948, "model_score": 0.4947, "style_score": 0.4948, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "I never like loud areas which filled with too many people, however con"},
  {"status": 200, "guess": "unsure", "confidence": 0.559, "model_score": 0.407, "style_score": 0.7111, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "Research is objectively the hardest and easiest thing you could you po"},
  {"status": 200, "guess": "unsure", "confidence": 0.5486, "model_score": 0.3564, "style_score": 0.7409, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "I think computer science is a cool subject to learn, regardless of whi"},
  {"status": 200, "guess": "unsure", "confidence": 0.6224, "model_score": 0.8394, "style_score": 0.4054, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "i dont know what i am writing. I dont know why am i writing this, nor "},
  {"status": 200, "guess": "unsure", "confidence": 0.5789, "model_score": 0.6859, "style_score": 0.472, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "I haven't talked to some people in many days, and I think it is fine. "}
]
```

Criterion 2 — `run_eval.py::main`, scenarios `c2 gap AI texts` (mean 0.8180)
and `c2 gap human texts` (mean 0.4634):

```json
[
  {"status": 200, "guess": "ai", "confidence": 0.8217, "model_score": 0.7544, "style_score": 0.8891, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "The importance of effective time management cannot be overstated in to"},
  {"status": 200, "guess": "ai", "confidence": 0.8615, "model_score": 0.7415, "style_score": 0.9815, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Effective study habits are essential for academic success in today's c"},
  {"status": 200, "guess": "ai", "confidence": 0.8978, "model_score": 0.9353, "style_score": 0.8602, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Climate change represents one of the most pressing challenges facing o"},
  {"status": 200, "guess": "ai", "confidence": 0.7797, "model_score": 0.8943, "style_score": 0.6651, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Social media has fundamentally transformed the way people communicate "},
  {"status": 200, "guess": "ai", "confidence": 0.7291, "model_score": 0.7827, "style_score": 0.6755, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Artificial intelligence is rapidly reshaping industries across the glo"}
]
```

```json
[
  {"status": 200, "guess": "human", "confidence": 0.2596, "model_score": 0.4445, "style_score": 0.0746, "label": "We think this was probably written by a person.", "sent": "I didn't sleep. Not properly, anyway — I lay there listening to the bo"},
  {"status": 200, "guess": "unsure", "confidence": 0.4823, "model_score": 0.5583, "style_score": 0.4063, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "As I started my university, I realized I did belong at CSU Chico; the "},
  {"status": 200, "guess": "ai", "confidence": 0.7408, "model_score": 0.6735, "style_score": 0.808, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "There is beauty in smiling after going through a rough patch. I truly "},
  {"status": 200, "guess": "unsure", "confidence": 0.4763, "model_score": 0.48, "style_score": 0.4727, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "Why is that we compare ourselves to something else, when they say that"},
  {"status": 200, "guess": "unsure", "confidence": 0.3578, "model_score": 0.2498, "style_score": 0.4657, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "I love how our fandom consists of people from different backgrounds. I"}
]
```

Criterion 3 — `run_eval.py::main`, scenario `c3 label coverage`. Order: 3
clearly AI, my pieces 6–8, 3 borderline. No input reached `human`:

```json
[
  {"status": 200, "guess": "ai", "confidence": 0.8777, "model_score": 0.8015, "style_score": 0.9538, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Time management is a critical skill that can significantly impact both"},
  {"status": 200, "guess": "ai", "confidence": 0.8092, "model_score": 0.7832, "style_score": 0.8352, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Reading offers numerous benefits that extend far beyond simple enterta"},
  {"status": 200, "guess": "ai", "confidence": 0.8163, "model_score": 0.7831, "style_score": 0.8494, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Teamwork is a fundamental component of success in any organization. Wh"},
  {"status": 200, "guess": "unsure", "confidence": 0.4948, "model_score": 0.4947, "style_score": 0.4948, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "I never like loud areas which filled with too many people, however con"},
  {"status": 200, "guess": "unsure", "confidence": 0.559, "model_score": 0.407, "style_score": 0.7111, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "Research is objectively the hardest and easiest thing you could you po"},
  {"status": 200, "guess": "unsure", "confidence": 0.5486, "model_score": 0.3564, "style_score": 0.7409, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "I think computer science is a cool subject to learn, regardless of whi"},
  {"status": 200, "guess": "unsure", "confidence": 0.4216, "model_score": 0.3489, "style_score": 0.4944, "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.", "sent": "Time management matters more than people admit, especially now that wo"},
  {"status": 200, "guess": "ai", "confidence": 0.7794, "model_score": 0.7256, "style_score": 0.8332, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Effective time management matters a lot in today's fast-paced work env"},
  {"status": 200, "guess": "ai", "confidence": 0.761, "model_score": 0.7259, "style_score": 0.796, "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.", "sent": "Reading is good for you in more ways than just being fun. If you read "}
]
```

Criterion 4 — `run_extra_checks.py::appeal_trial`
(`results/extra_checks_2026-11-04_1824_before.md`). One of the five real
appeals, with its log entries, then the fake id:

```json
{
  "content_id": "c_bd31103edc5b",
  "submit_status": 200,
  "appeal_status": 200,
  "appeal_response": {
    "content_id": "c_bd31103edc5b",
    "message": "Thanks — your appeal has been recorded and a person will review this piece.",
    "status": "under_review"
  },
  "log_entries_for_id": [
    {
      "combined_score": 0.7208,
      "content_id": "c_bd31103edc5b",
      "creator_id": "eval_appeal_t1_1",
      "guess": "ai",
      "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.",
      "model_score": 0.6311,
      "status": "decided",
      "style_score": 0.8106,
      "timestamp": "2026-11-05T02:24:23+00:00"
    },
    {
      "content_id": "c_bd31103edc5b",
      "creator_id": "eval_appeal_t1_1",
      "event": "appeal",
      "reasoning": "I wrote this myself; the label is wrong.",
      "status": "under_review",
      "timestamp": "2026-11-05T02:24:23+00:00"
    }
  ],
  "passed": true
}
```

```json
{
  "content_id": "c_fake8440bbbb",
  "appeal_status": 404,
  "appeal_response": {
    "error": "not_found",
    "message": "No submission found with content_id 'c_fake8440bbbb'."
  },
  "log_entries_for_id": [],
  "passed": true
}
```

Criterion 5 — `run_eval.py::main`, scenario `c5 bad input` (missing text,
empty text, 50,000 characters), then `run_extra_checks.py::non_object_trial`:

```json
[
  {"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"creator_id\": \"eval_bad_missing\"}"},
  {"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "(empty text)"},
  {"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "I wrote this sentence myself. I wrote this sentence myself. I wrote th"}
]
```

```json
{
  "sent": [
    "text",
    "creator_id"
  ],
  "status": 400,
  "response": {
    "error": "bad_request",
    "message": "Send JSON with a non-empty \"text\"."
  },
  "passed": true
}
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
