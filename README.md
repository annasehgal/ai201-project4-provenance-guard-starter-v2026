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
2. Missing, empty or too-short text is refused with a `400` and logged; nothing else runs.
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
how much sentence lengths vary, how much vocabulary repeats (unique words ÷
total words), and how much varied punctuation (commas, semicolons, dashes)
appears. Built in `stylometry.py::style_signal`.

**Why that might differ between human and AI writing:** Generated prose tends
toward even, mid-length sentences and a safe, narrower vocabulary. Human
writing is lumpier — a three-word sentence next to a forty-word one, dashes
and asides, a repeated word for effect.

**What it can't see:** Meaning. Anything that changes the shape without
changing the substance moves it: splitting or merging sentences, adding typos
(which raise word variety), sprinkling in dashes, pasting in a quotation. All
of that is cheap to do on purpose. It is also length-sensitive — word variety
falls naturally as text gets longer — and a one- or two-sentence submission
barely has a shape to measure.

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

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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
