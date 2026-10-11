# Blog Style Guide

## Voice

Write in first person. Conversational but polished — like talking to a smart colleague, not presenting to a boardroom. Draw from personal experience. Share observations, don't lecture.

## Tone Rules (without losing spirit)

- **Remove unnecessary emphasis/superlatives** — cut "extremely", "very", "really", "incredibly"
- **Remove hedging or filler** — cut "basically", "essentially", "actually", "so to speak", "kind of", "sort of"
- **No profanity**
- **Be direct** — if you can say it in one sentence, don't use three
- Contractions are fine (it's, you're, they're)

## Structure

Every post must have:
- A proper human-readable **title** (not a filename slug)
- **Section headers (`##`)** — no wall of text; break ideas into named sections
- A **closing** — either a "Remember" section, a clean summary, or a strong final sentence

Optional but encouraged:
- A relevant image near the top
- Subsections (`###`) for long sections only

## Formatting

- **Bold key insights** within paragraphs — the one thing someone should take away from that sentence
- Use **bullet lists** for examples, options, or multiple parallel items
- Use **numbered lists** for sequences or steps
- Avoid deep nesting — `###` is the limit

## Frontmatter

```toml
+++
title = 'Human Readable Title'
date = YYYY-MM-DDTHH:MM:SSZ
draft = false
+++
```

## Linking

Where genuinely relevant, link to existing posts inline. Don't force it. Use the post slug:

```markdown
[Post Title](/posts/post-slug/)
```

## What to Avoid

- Repeating the same point with different wording
- Throat-clearing intros ("Today I want to talk about...")
- Over-explaining — trust the reader
- Excessive superlatives applied to real people ("great, great, great engineer")
- **Em dashes (`—`)** — a common AI tell. Use a comma, colon, or restructure the sentence instead

## Share the Lesson, Not the Facts

The blog is public. Work is the inspiration, never the content.

- No employer, client, auditor or colleague names, no ticket or change IDs, no internal system names.
- No live numbers from work tools. Say the situation exists and that it is being managed: "a long list of open findings I work through every week", not "251 open Snyk findings".
- Better still, tell an example close to the real one, or an allegory (a garden, a kitchen, a household budget) that makes the same point.
- Never use "honest" or "honestly", and no em or en dashes at all.
- Run `python3 scripts/check_draft.py <post>` before publishing. It must print PASS.
