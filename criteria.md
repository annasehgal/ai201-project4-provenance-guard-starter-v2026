# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives on my own writing

Of 10 pieces I wrote myself, **at most 2** receive the high-confidence AI label, in each of 3 trials.

**Why this target:** On a writing site, wrongly accusing a real writer costs far more than missing some AI text, so false positives get the tightest limit of any error here. I chose 2 rather than 0 or 1 because my own "clearly human" sample already scored 0.44 on the model signal alone, so plain human writing really does drift toward the AI end; 0 would be a promise I can't back. But 2 is the ceiling, not the goal, and every writer inside it still has the appeal path.

---

## 2. Clearly-AI and clearly-human text score apart

Across 5 clearly AI-generated texts and 5 clearly human-written texts, the **mean combined score of the AI texts is at least 0.30 higher** than the mean of the human texts, in each of 3 trials.

**Why this target:** If the two groups score only a little apart, small random wobble from the model can push a piece across a label boundary, and the labels stop meaning anything. A gap of 0.30 is roughly the width of my unsure band, so clearly-AI and clearly-human text should land on opposite sides of it rather than both ending up in the middle.

---

## 3. Every label is reachable

Of 9 inputs chosen across the range (3 I judge clearly AI, 3 clearly human, 3 borderline), **each of the three labels** — high-confidence human, unsure, high-confidence AI — **appears at least 2 times**, in each of 3 trials.

**Why this target:** A label that never appears is a bug, not a design choice. Asking for each label twice rather than once means no label is reached by a single lucky input sitting right on a boundary, and it checks that "unsure" is a real band that borderline text lands in, not a gap the score skips over.

---

## 4. Appeals always change status and are always recorded

Of 5 appeals sent with real `content_id`s, **5 of 5** return 200, set the status to `under_review`, and show up in `GET /log` next to the original decision. An appeal with a made-up `content_id` returns **404** and adds no `under_review` entry.

**Why this target:** The appeal is the only thing between a wrong accusation and nothing at all, so a lost appeal is the worst failure this service can have for the writer, and anything below 100% isn't acceptable. The fake-id check matters because a typo in a content_id should fail loudly with a 404, not look like it worked while recording nothing.

---

## 5. Bad input never crashes the service

Of 4 bad requests — no `text` field, empty `text` (`""`), a body that isn't a JSON object, and `text` of 50,000 characters — **4 of 4 return 400** with an error message, and **0** return a 500.

**Why this target:** A crash tells the writer nothing and leaves no useful trace, and bad input is the first thing an attacker will send. A clear 400 tells the caller what to fix. Enormous text is refused rather than scored because the detector only reads the first ~400 tokens anyway, so a label on 50,000 characters would be judging a small slice of the work as if it were the whole thing.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
