# Attack run

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 17:40
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_d36e6ab03224` | unsure | 0.582 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_85b4961dde5b` | unsure | 0.605 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_736a1f17731e` | ai | 0.739 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_85856b13cd09` | ai | 0.806 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_a9a2c5b77a74` | unsure | 0.434 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_22c85fd2e536` | unsure | 0.529 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_655662544e8e` | unsure | 0.449 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | `c_ea9b1c5822af` | unsure | 0.539 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_dc606d2582b6` | ai | 0.795 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_c958931f5579` | ai | 0.797 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_032346d35122` | unsure | 0.628 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c_cfaa6d059ea1` | ai | 0.703 | **BROKE** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_d0a4dda5800c` | ai | 0.772 | **BROKE** |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_c26b711e664b` | ai | 0.777 | **BROKE** |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_cabdcd029c7f` | ai | 0.734 | **BROKE** |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_be7791601bc6` | ai | 0.713 | **BROKE** |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_209192bdc928` | unsure | 0.654 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `c_fbd81b8b187c` | unsure | 0.624 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_10a2cbf3406c` | unsure | 0.630 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_fabb6375dd05` | unsure | 0.495 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_766fbd8a5c71` | ai | 0.748 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_c9ee5def45b2` | unsure | 0.565 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_d88d4b8a63be` | unsure | 0.570 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_edc8767cfbe0` | unsure | 0.608 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `c_4a7f7df6f181` | unsure | 0.417 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `c_ea99cac48c7b` | human | 0.339 | **BROKE** |
| MF05 | malformed | text is a very long single word | 200 | `c_0a91610245c5` | ai | 0.915 | **BROKE** |
| MF06 | malformed | text is emoji only | 200 | `c_cbb552a82f41` | ai | 0.749 | **BROKE** |
| MF07 | malformed | text is right-to-left script | 200 | `c_c2ab33239717` | ai | 0.703 | **BROKE** |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `c_354be2c8e1e4` | unsure | 0.536 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `c_91c3955cd34b` | unsure | 0.441 | **BROKE** |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_635369279613` | unsure | 0.431 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_3cd7597ed755` | unsure | 0.431 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_6549c087c64f` | unsure | 0.431 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_e4fd13d8f09f` | unsure | 0.431 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_cf460d37e113` | unsure | 0.431 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_d36e6ab03224",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5817,
  "model_score": 0.1635,
  "style_score": 1.0,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c_85b4961dde5b",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.6049,
  "model_score": 0.5943,
  "style_score": 0.6155,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c_736a1f17731e",
  "creator_id": "attacker_EV03",
  "guess": "ai",
  "confidence": 0.739,
  "model_score": 0.6662,
  "style_score": 0.8119,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c_85856b13cd09",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.8057,
  "model_score": 0.6114,
  "style_score": 1.0,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c_a9a2c5b77a74",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.4342,
  "model_score": 0.3212,
  "style_score": 0.5472,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c_22c85fd2e536",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5295,
  "model_score": 0.5727,
  "style_score": 0.4863,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c_655662544e8e",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4491,
  "model_score": 0.5862,
  "style_score": 0.312,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c_ea9b1c5822af",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.5393,
  "model_score": 0.2452,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c_dc606d2582b6",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.7951,
  "model_score": 0.7042,
  "style_score": 0.8859,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c_c958931f5579",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7969,
  "model_score": 0.9792,
  "style_score": 0.6145,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c_032346d35122",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6276,
  "model_score": 0.6175,
  "style_score": 0.6376,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c_cfaa6d059ea1",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7027,
  "model_score": 0.7387,
  "style_score": 0.6667,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c_d0a4dda5800c",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7719,
  "model_score": 0.8051,
  "style_score": 0.7386,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c_c26b711e664b",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7769,
  "model_score": 0.8329,
  "style_score": 0.7209,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c_cabdcd029c7f",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7336,
  "model_score": 0.8005,
  "style_score": 0.6667,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c_be7791601bc6",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7131,
  "model_score": 0.8814,
  "style_score": 0.5449,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_209192bdc928",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6544,
  "model_score": 0.8816,
  "style_score": 0.4273,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c_fbd81b8b187c",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.6242,
  "model_score": 0.3223,
  "style_score": 0.9261,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c_10a2cbf3406c",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.6305,
  "model_score": 0.4625,
  "style_score": 0.7985,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c_fabb6375dd05",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.4952,
  "model_score": 0.2044,
  "style_score": 0.786,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c_766fbd8a5c71",
  "creator_id": "attacker_PI03",
  "guess": "ai",
  "confidence": 0.7475,
  "model_score": 0.5943,
  "style_score": 0.9007,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c_c9ee5def45b2",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5652,
  "model_score": 0.4998,
  "style_score": 0.6306,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c_d88d4b8a63be",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.57,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c_edc8767cfbe0",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.6082,
  "model_score": 0.5583,
  "style_score": 0.6581,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c_4a7f7df6f181",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.4167,
  "model_score": 0.0,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "c_ea99cac48c7b",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3389,
  "model_score": 0.0112,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c_0a91610245c5",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9155,
  "model_score": 0.9976,
  "style_score": 0.8333,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c_cbb552a82f41",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7485,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c_c2ab33239717",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong \u2014 if you wrote this yourself, you can ask for a review and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "c_354be2c8e1e4",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.5364,
  "model_score": 0.2395,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "c_91c3955cd34b",
  "creator_id": {
    "id": "x"
  },
  "guess": "unsure",
  "confidence": 0.4413,
  "model_score": 0.0492,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c_635369279613",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.431,
  "model_score": 0.0287,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c_3cd7597ed755",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.431,
  "model_score": 0.0287,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c_6549c087c64f",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.431,
  "model_score": 0.0287,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c_e4fd13d8f09f",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.431,
  "model_score": 0.0287,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c_cf460d37e113",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.431,
  "model_score": 0.0287,
  "style_score": 0.8333,
  "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
