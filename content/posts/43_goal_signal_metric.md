+++
title = 'Goal, Signal, Metric: Say What You Want Before You Count It'
date = 2026-10-08T09:00:00Z
draft = true
+++

Most dashboards I've built started with the numbers. Something was easy to count, so I counted it, then went looking for a reason it mattered. Chapter 7 of *Software Engineering at Google* runs it in the other direction, and I think it's the right way round.

## The Three Layers

Google's engineering productivity team evaluated their readability process (the certification that lets an engineer approve code in a given language) using a simple ladder:

1. **Goal**: the outcome you want, in plain language. "Engineers write higher-quality code as a result of the readability process."
2. **Signal**: how you'd know the goal was met, if you could see everything. "Engineers who have readability judge their code to be of higher quality."
3. **Metric**: the thing you can measure that stands in for the signal. "Quarterly survey: proportion of engineers satisfied with the quality of their own code."

**The metric is the last thing you write, not the first.** It's a proxy, and you can only judge a proxy if you know what it's standing in for.

## QUANTS Keeps You Honest

They group goals under five headings: Quality of the code, Attention from engineers, iNtellectual complexity, Tempo and velocity, and Satisfaction. The point isn't the acronym. **The point is that one metric on its own will lie to you.** If readability made code more consistent but doubled review latency, a quality-only dashboard would call it a win.

Some of their metrics are also framed in the negative: the proportion of engineers reporting that readability had *no impact or a negative impact*. I like that. It's a metric designed to catch you being wrong.

## Where I See This at Work

This week I've had a Snyk report tick over to 166 open and 253 fixed, and a daily plan feasibility check running against delivery dates. Both are metrics. Neither is a goal.

- For Snyk, the goal is closer to "we don't ship exploitable vulnerabilities," and the signal is "nothing exploitable reaches production." A falling open count could mean that, or it could mean we fixed the easy ones and left the reachable criticals.
- For plan feasibility, the goal is "commitments we make are ones we keep." A re-dated ticket improves the overdue count without improving that at all.

**When a number moves, I want to be able to say which signal it moved toward.** If I can't, I'm watching a scoreboard, not managing anything.

## Remember

Write the goal in a sentence. Describe what you'd see if it were true. Only then pick something to count, and pick at least one number that would tell you if you're fooling yourself.
