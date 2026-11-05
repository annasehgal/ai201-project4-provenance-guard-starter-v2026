"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

import json
from pathlib import Path

_SAMPLES = Path(__file__).parent / "samples"


def _sample(name: str) -> str:
    """Text from one of the unit 7 calibration samples in samples/."""
    return json.loads((_SAMPLES / f"{name}.json").read_text(encoding="utf-8"))["text"]


# ── My own writing ────────────────────────────────────────────────────────────
# Ten pieces I wrote myself, pasted exactly as I wrote them — typos, lowercase
# and all. Fixing them would test a cleaner writer than me.
MY_WRITING = [
    # 1
    "As I started my university, I realized I did belong at CSU Chico; the campus is beautiful, and the people and professors are the best. Meriam Library is one of my favorite places to do my work and to write essays. Just like I am writing this essay, saying to myself, “I won’t give up no matter how hard it gets,” with a smile on my face.",
    # 2
    "There is beauty in smiling after going through a rough patch. I truly believe humans are quite capable of surviving, evolving, and making it past if we try. We just have to keep trying, no matter what.",
    # 3
    "Why is that we compare ourselves to something else, when they say that everyone and everything is unique. Why do we diminish our own worth to something that survived the same environment. What we look is similarity between each thing and rank what does it better. However, we forget that the one who is better wouldn’t survive the same if they were in our place. Maybe that’s why, we should not compare, maybe that’s why we we should be proud of us each day, for being uniquely ourselves, for ourselves, and continue to grow more unique each day.",
    # 4
    "I love how our fandom consists of people from different backgrounds. I saw someone doing a statistical analysis of true randomness of genral and pre-sale and their results. In addition, I saw some other analysis and was able to tell my hypothesis without data (there does seem to be some underlying factor behind queue numbers). There is another theory it is truly dependent on the random seed we get the first time which is interesting, and making more accounts would give better number (if we get an account which gets lower number, and stays consistent - someone else found that out through another analysis of that data).",
    # 5
    "I actually hated the color Blue for a long time. I have a whole story behind that from 2023, which was fun. However, I love the color again, which means life is getting better.",
    # 6
    "I never like loud areas which filled with too many people, however concert was fun to go to. I met so many people, made new friends, did random things, and enjoyed. I hope to go again sometime in future with more friends that are yet to come.",
    # 7
    "Research is objectively the hardest and easiest thing you could you possibly. Once you get started with literature review, you esentially get confused about what some things mean or how to read a paper. Although eventually you learn how to do read through it without even realizing, and that's the best part.",
    # 8
    "I think computer science is a cool subject to learn, regardless of which major you are from. It teaches you how to think systematically and builds logic. The only downside is the time spent on it, esepcially in age where ai can solve most of the things without understanding or critical thinking.",
    # 9
    "i dont know what i am writing. I dont know why am i writing this, nor do i know what the point of any of this is but hey i am a human. Humans are weird, there are some other people in my group, they don't talk, i dont know how to get them to talk to me.",
    # 10
    "I haven't talked to some people in many days, and I think it is fine. I used to be the person who loved talking all the time, but as we grow we talk less and less to people while living our own life. However, i do think it might change by next year.",
]


# ── Clearly AI ────────────────────────────────────────────────────────────────
# Generated by Claude (Opus 5.5) for this test, unedited, plus the unit 7
# clearly_ai sample. Typical assistant prose: even sentences, signposting,
# "it is important to note".
AI_TEXTS = [
    _sample("clearly_ai"),
    "Effective study habits are essential for academic success in today's competitive educational landscape. Students who develop consistent routines are better equipped to retain information and perform well on examinations. There are several key strategies that can significantly enhance learning outcomes. First, it is important to establish a dedicated study space that minimizes distractions. Second, breaking material into manageable sections allows for deeper understanding. Finally, regular review sessions help reinforce knowledge over time. By implementing these strategies, students can achieve their academic goals and build a strong foundation for future success.",
    "Climate change represents one of the most pressing challenges facing our world today. Rising global temperatures have far-reaching consequences for ecosystems, economies, and communities around the globe. It is important to note that addressing this issue requires a multifaceted approach. Governments, businesses, and individuals all have a crucial role to play in reducing greenhouse gas emissions. Furthermore, investing in renewable energy sources can help mitigate the impacts of climate change while also creating new economic opportunities. Ultimately, collective action is essential to ensure a sustainable future for generations to come.",
    "Social media has fundamentally transformed the way people communicate and share information. Platforms such as Instagram, Twitter, and Facebook enable users to connect with others across the globe instantly. However, it is important to consider both the benefits and drawbacks of these technologies. On one hand, social media fosters community and provides access to diverse perspectives. On the other hand, excessive use can negatively impact mental health and productivity. Therefore, it is crucial for individuals to maintain a healthy balance and use these platforms mindfully.",
    "Artificial intelligence is rapidly reshaping industries across the global economy. From healthcare to finance, AI-powered tools are streamlining processes and enabling more informed decision-making. Moreover, these technologies have the potential to unlock new levels of efficiency and innovation. Nevertheless, it is essential to address the ethical considerations associated with AI deployment, including issues of bias, privacy, and accountability. By fostering responsible development practices, organizations can harness the transformative power of artificial intelligence while minimizing potential risks.",
]

# Three more, generated the same way, for label coverage.
AI_TEXTS_COVERAGE = [
    "Time management is a critical skill that can significantly impact both personal and professional success. Individuals who manage their time effectively are able to accomplish more while experiencing less stress. One effective approach is to create a daily schedule that prioritizes the most important tasks. Additionally, setting clear and achievable goals provides direction and motivation. It is also beneficial to minimize distractions by turning off notifications during focused work periods. By adopting these practices, individuals can maximize their productivity and achieve a healthier work-life balance.",
    "Reading offers numerous benefits that extend far beyond simple entertainment. Engaging with books regularly can improve vocabulary, enhance critical thinking skills, and broaden one's understanding of the world. Furthermore, reading has been shown to reduce stress and promote relaxation. It is worth noting that both fiction and nonfiction provide unique advantages. Fiction fosters empathy by allowing readers to experience different perspectives, while nonfiction delivers valuable knowledge and insights. Overall, cultivating a reading habit is an investment in lifelong learning and personal growth.",
    "Teamwork is a fundamental component of success in any organization. When individuals collaborate effectively, they can leverage diverse skills and perspectives to achieve shared objectives. Clear communication is essential for ensuring that all team members are aligned and informed. Moreover, establishing mutual trust and respect creates a positive environment in which everyone feels valued. It is also important to define roles and responsibilities to avoid confusion and duplication of effort. Ultimately, strong teamwork drives innovation, improves productivity, and contributes to long-term organizational success.",
]

# Borderline: the two unit 7 borderline samples, plus one AI paragraph I
# rewrote by hand (casual phrasing, a couple of my own asides).
BORDERLINE = [
    _sample("borderline"),
    _sample("edited_ai"),
    "Reading is good for you in more ways than just being fun. If you read a lot your vocabulary gets better and you start thinking more critically, at least I think so. It also helps with stress, which honestly I need. Fiction and nonfiction both help but in different ways. Fiction lets you see things from someone else's side, and nonfiction just teaches you stuff. So basically reading is worth making a habit, even if it's only a few pages before bed.",
]


SCENARIOS = [
    # Criterion 1 — at most 2 of 10 of my own pieces get the AI label.
    {
        "name": "c1 my own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },

    # Criterion 2 — mean combined score of AI texts is at least 0.30 above the
    # mean of the human texts. Two scenarios so each group's mean is separate.
    # Human group: the unit 7 clearly_human sample plus my pieces 1–4 (chosen
    # by number, not by score).
    {
        "name": "c2 gap AI texts",
        "criterion": 2,
        "texts": AI_TEXTS,
    },
    {
        "name": "c2 gap human texts",
        "criterion": 2,
        "texts": [_sample("clearly_human")] + MY_WRITING[0:4],
    },

    # Criterion 3 — each of the three labels appears at least twice across
    # 3 clearly AI, 3 clearly human (my pieces 6–8), 3 borderline.
    {
        "name": "c3 label coverage",
        "criterion": 3,
        "texts": AI_TEXTS_COVERAGE + MY_WRITING[5:8] + BORDERLINE,
    },

    # Criterion 4 — appeals. run_eval.py only calls /submit, so the appeal path
    # is tested by run_extra_checks.py (5 real appeals + 1 fake id, 3 trials).

    # Criterion 5 — bad input returns 400, never 500. Three of the four bodies
    # are here; the fourth (a body that isn't a JSON object) can't be written
    # as a dict, so run_extra_checks.py sends it.
    {
        "name": "c5 bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},               # no text field
            {"text": "", "creator_id": "eval_bad_empty"},    # empty text
            {"text": ("I wrote this sentence myself. " * 2000)[:50000],
             "creator_id": "eval_bad_huge"},                 # 50,000 characters
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
