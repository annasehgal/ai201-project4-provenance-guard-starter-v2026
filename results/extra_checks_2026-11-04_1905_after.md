# Extra checks — after

- Produced by: `run_extra_checks.py::main` (appeals: `appeal_trial`, non-object body: `non_object_trial`)
- 3 trials · 2026-11-04 19:05

| Trial | Criterion 4: appeals passed | Criterion 4: fake id → 404, no entry | Criterion 5: non-object body → 400 |
|---|---|---|---|
| 1 | 5/5 | 404 (pass) | 400 (pass) |
| 2 | 5/5 | 404 (pass) | 400 (pass) |
| 3 | 5/5 | 404 (pass) | 400 (pass) |

## Full output

```json
[
  {
    "trial": 1,
    "appeal": {
      "appeals": [
        {
          "content_id": "c_4a1d6242c4cb",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_4a1d6242c4cb",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.7208,
              "content_id": "c_4a1d6242c4cb",
              "creator_id": "eval_appeal_t1_1",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.6311,
              "status": "decided",
              "style_score": 0.8106,
              "timestamp": "2026-11-05T03:05:55+00:00"
            },
            {
              "content_id": "c_4a1d6242c4cb",
              "creator_id": "eval_appeal_t1_1",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:55+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_476f8aded9af",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_476f8aded9af",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5367,
              "content_id": "c_476f8aded9af",
              "creator_id": "eval_appeal_t1_2",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.24,
              "status": "decided",
              "style_score": 0.8333,
              "timestamp": "2026-11-05T03:05:55+00:00"
            },
            {
              "content_id": "c_476f8aded9af",
              "creator_id": "eval_appeal_t1_2",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:55+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_98553a9b926c",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_98553a9b926c",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5847,
              "content_id": "c_98553a9b926c",
              "creator_id": "eval_appeal_t1_3",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4849,
              "status": "decided",
              "style_score": 0.6845,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_98553a9b926c",
              "creator_id": "eval_appeal_t1_3",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_5101f4d5c7f8",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_5101f4d5c7f8",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.4722,
              "content_id": "c_5101f4d5c7f8",
              "creator_id": "eval_appeal_t1_4",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.361,
              "status": "decided",
              "style_score": 0.5833,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_5101f4d5c7f8",
              "creator_id": "eval_appeal_t1_4",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_339253d2fb61",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_339253d2fb61",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5935,
              "content_id": "c_339253d2fb61",
              "creator_id": "eval_appeal_t1_5",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4203,
              "status": "decided",
              "style_score": 0.7667,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_339253d2fb61",
              "creator_id": "eval_appeal_t1_5",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        }
      ],
      "fake": {
        "content_id": "c_fake5eb28c45",
        "appeal_status": 404,
        "appeal_response": {
          "error": "not_found",
          "message": "No submission found with content_id 'c_fake5eb28c45'."
        },
        "log_entries_for_id": [],
        "passed": true
      }
    },
    "non_object": {
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
  },
  {
    "trial": 2,
    "appeal": {
      "appeals": [
        {
          "content_id": "c_032d8c757d58",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_032d8c757d58",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.7208,
              "content_id": "c_032d8c757d58",
              "creator_id": "eval_appeal_t2_1",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.6311,
              "status": "decided",
              "style_score": 0.8106,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_032d8c757d58",
              "creator_id": "eval_appeal_t2_1",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_4a40db38e6d9",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_4a40db38e6d9",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5367,
              "content_id": "c_4a40db38e6d9",
              "creator_id": "eval_appeal_t2_2",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.24,
              "status": "decided",
              "style_score": 0.8333,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_4a40db38e6d9",
              "creator_id": "eval_appeal_t2_2",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_e818ff4c0459",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_e818ff4c0459",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5847,
              "content_id": "c_e818ff4c0459",
              "creator_id": "eval_appeal_t2_3",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4849,
              "status": "decided",
              "style_score": 0.6845,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_e818ff4c0459",
              "creator_id": "eval_appeal_t2_3",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_0b630a8b81c4",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_0b630a8b81c4",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.4722,
              "content_id": "c_0b630a8b81c4",
              "creator_id": "eval_appeal_t2_4",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.361,
              "status": "decided",
              "style_score": 0.5833,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_0b630a8b81c4",
              "creator_id": "eval_appeal_t2_4",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_b9908510809f",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_b9908510809f",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5935,
              "content_id": "c_b9908510809f",
              "creator_id": "eval_appeal_t2_5",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4203,
              "status": "decided",
              "style_score": 0.7667,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_b9908510809f",
              "creator_id": "eval_appeal_t2_5",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        }
      ],
      "fake": {
        "content_id": "c_fakeef33d249",
        "appeal_status": 404,
        "appeal_response": {
          "error": "not_found",
          "message": "No submission found with content_id 'c_fakeef33d249'."
        },
        "log_entries_for_id": [],
        "passed": true
      }
    },
    "non_object": {
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
  },
  {
    "trial": 3,
    "appeal": {
      "appeals": [
        {
          "content_id": "c_0b25ade6c7a1",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_0b25ade6c7a1",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.7208,
              "content_id": "c_0b25ade6c7a1",
              "creator_id": "eval_appeal_t3_1",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.6311,
              "status": "decided",
              "style_score": 0.8106,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_0b25ade6c7a1",
              "creator_id": "eval_appeal_t3_1",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_13250d605a12",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_13250d605a12",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5367,
              "content_id": "c_13250d605a12",
              "creator_id": "eval_appeal_t3_2",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.24,
              "status": "decided",
              "style_score": 0.8333,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_13250d605a12",
              "creator_id": "eval_appeal_t3_2",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_afb3caa02246",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_afb3caa02246",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5847,
              "content_id": "c_afb3caa02246",
              "creator_id": "eval_appeal_t3_3",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4849,
              "status": "decided",
              "style_score": 0.6845,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_afb3caa02246",
              "creator_id": "eval_appeal_t3_3",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_bfe3f0fcb447",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_bfe3f0fcb447",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.4722,
              "content_id": "c_bfe3f0fcb447",
              "creator_id": "eval_appeal_t3_4",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.361,
              "status": "decided",
              "style_score": 0.5833,
              "timestamp": "2026-11-05T03:05:56+00:00"
            },
            {
              "content_id": "c_bfe3f0fcb447",
              "creator_id": "eval_appeal_t3_4",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:56+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_2bc9100ff0b0",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_2bc9100ff0b0",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5935,
              "content_id": "c_2bc9100ff0b0",
              "creator_id": "eval_appeal_t3_5",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4203,
              "status": "decided",
              "style_score": 0.7667,
              "timestamp": "2026-11-05T03:05:57+00:00"
            },
            {
              "content_id": "c_2bc9100ff0b0",
              "creator_id": "eval_appeal_t3_5",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T03:05:57+00:00"
            }
          ],
          "passed": true
        }
      ],
      "fake": {
        "content_id": "c_fake4a9a20f6",
        "appeal_status": 404,
        "appeal_response": {
          "error": "not_found",
          "message": "No submission found with content_id 'c_fake4a9a20f6'."
        },
        "log_entries_for_id": [],
        "passed": true
      }
    },
    "non_object": {
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
  }
]
```
