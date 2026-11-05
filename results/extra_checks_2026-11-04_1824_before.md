# Extra checks — before

- Produced by: `run_extra_checks.py::main` (appeals: `appeal_trial`, non-object body: `non_object_trial`)
- 3 trials · 2026-11-04 18:24

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
        },
        {
          "content_id": "c_75be23bb0d93",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_75be23bb0d93",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5367,
              "content_id": "c_75be23bb0d93",
              "creator_id": "eval_appeal_t1_2",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.24,
              "status": "decided",
              "style_score": 0.8333,
              "timestamp": "2026-11-05T02:24:23+00:00"
            },
            {
              "content_id": "c_75be23bb0d93",
              "creator_id": "eval_appeal_t1_2",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:23+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_c6fbc8949b33",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_c6fbc8949b33",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5847,
              "content_id": "c_c6fbc8949b33",
              "creator_id": "eval_appeal_t1_3",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4849,
              "status": "decided",
              "style_score": 0.6845,
              "timestamp": "2026-11-05T02:24:23+00:00"
            },
            {
              "content_id": "c_c6fbc8949b33",
              "creator_id": "eval_appeal_t1_3",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:23+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_82ae06f61bf2",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_82ae06f61bf2",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.4722,
              "content_id": "c_82ae06f61bf2",
              "creator_id": "eval_appeal_t1_4",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.361,
              "status": "decided",
              "style_score": 0.5833,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_82ae06f61bf2",
              "creator_id": "eval_appeal_t1_4",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_9e6f1b291487",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_9e6f1b291487",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5935,
              "content_id": "c_9e6f1b291487",
              "creator_id": "eval_appeal_t1_5",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4203,
              "status": "decided",
              "style_score": 0.7667,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_9e6f1b291487",
              "creator_id": "eval_appeal_t1_5",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        }
      ],
      "fake": {
        "content_id": "c_fake8440bbbb",
        "appeal_status": 404,
        "appeal_response": {
          "error": "not_found",
          "message": "No submission found with content_id 'c_fake8440bbbb'."
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
          "content_id": "c_6d290130c4f7",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_6d290130c4f7",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.7208,
              "content_id": "c_6d290130c4f7",
              "creator_id": "eval_appeal_t2_1",
              "guess": "ai",
              "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.",
              "model_score": 0.6311,
              "status": "decided",
              "style_score": 0.8106,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_6d290130c4f7",
              "creator_id": "eval_appeal_t2_1",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_556d7200c69d",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_556d7200c69d",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5367,
              "content_id": "c_556d7200c69d",
              "creator_id": "eval_appeal_t2_2",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.24,
              "status": "decided",
              "style_score": 0.8333,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_556d7200c69d",
              "creator_id": "eval_appeal_t2_2",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_537877bbae95",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_537877bbae95",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5847,
              "content_id": "c_537877bbae95",
              "creator_id": "eval_appeal_t2_3",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4849,
              "status": "decided",
              "style_score": 0.6845,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_537877bbae95",
              "creator_id": "eval_appeal_t2_3",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_bccc0668edda",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_bccc0668edda",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.4722,
              "content_id": "c_bccc0668edda",
              "creator_id": "eval_appeal_t2_4",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.361,
              "status": "decided",
              "style_score": 0.5833,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_bccc0668edda",
              "creator_id": "eval_appeal_t2_4",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_8531b7ba2903",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_8531b7ba2903",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5935,
              "content_id": "c_8531b7ba2903",
              "creator_id": "eval_appeal_t2_5",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4203,
              "status": "decided",
              "style_score": 0.7667,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_8531b7ba2903",
              "creator_id": "eval_appeal_t2_5",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        }
      ],
      "fake": {
        "content_id": "c_fake7bd46daf",
        "appeal_status": 404,
        "appeal_response": {
          "error": "not_found",
          "message": "No submission found with content_id 'c_fake7bd46daf'."
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
          "content_id": "c_dc02a8ce91d7",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_dc02a8ce91d7",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.7208,
              "content_id": "c_dc02a8ce91d7",
              "creator_id": "eval_appeal_t3_1",
              "guess": "ai",
              "label": "Our check suggests this was likely generated with AI. Automated checks can be wrong — if you wrote this yourself, you can ask for a review and a person will look at it.",
              "model_score": 0.6311,
              "status": "decided",
              "style_score": 0.8106,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_dc02a8ce91d7",
              "creator_id": "eval_appeal_t3_1",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_b964801fd574",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_b964801fd574",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5367,
              "content_id": "c_b964801fd574",
              "creator_id": "eval_appeal_t3_2",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.24,
              "status": "decided",
              "style_score": 0.8333,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_b964801fd574",
              "creator_id": "eval_appeal_t3_2",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_390b0ace1e38",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_390b0ace1e38",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5847,
              "content_id": "c_390b0ace1e38",
              "creator_id": "eval_appeal_t3_3",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4849,
              "status": "decided",
              "style_score": 0.6845,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_390b0ace1e38",
              "creator_id": "eval_appeal_t3_3",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_949cd7c4caa5",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_949cd7c4caa5",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.4722,
              "content_id": "c_949cd7c4caa5",
              "creator_id": "eval_appeal_t3_4",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.361,
              "status": "decided",
              "style_score": 0.5833,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_949cd7c4caa5",
              "creator_id": "eval_appeal_t3_4",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        },
        {
          "content_id": "c_45c413f2de78",
          "submit_status": 200,
          "appeal_status": 200,
          "appeal_response": {
            "content_id": "c_45c413f2de78",
            "message": "Thanks — your appeal has been recorded and a person will review this piece.",
            "status": "under_review"
          },
          "log_entries_for_id": [
            {
              "combined_score": 0.5935,
              "content_id": "c_45c413f2de78",
              "creator_id": "eval_appeal_t3_5",
              "guess": "unsure",
              "label": "Our check gave mixed results on this piece, so we're not making a call. If you'd like a person to look at it, you can ask for a review.",
              "model_score": 0.4203,
              "status": "decided",
              "style_score": 0.7667,
              "timestamp": "2026-11-05T02:24:24+00:00"
            },
            {
              "content_id": "c_45c413f2de78",
              "creator_id": "eval_appeal_t3_5",
              "event": "appeal",
              "reasoning": "I wrote this myself; the label is wrong.",
              "status": "under_review",
              "timestamp": "2026-11-05T02:24:24+00:00"
            }
          ],
          "passed": true
        }
      ],
      "fake": {
        "content_id": "c_fake53105aaf",
        "appeal_status": 404,
        "appeal_response": {
          "error": "not_found",
          "message": "No submission found with content_id 'c_fake53105aaf'."
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
