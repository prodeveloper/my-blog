+++
title = 'After This, Therefore Because of This'
date = 2026-09-29T09:00:00+01:00
draft = true
+++

The first question on every incident bridge is always the same. What changed?

It's the right question. It just isn't the answer, and the gap between those two things has cost me more hours than I care to count.

I've been working through the argument pattern in Eben Hewitt's *Technology Strategy Patterns*, and the part that stuck isn't the section on decks or rhetoric. It's a small Latin phrase he uses to describe the reasoning we all fall into at 2am.

## The fallacy has a name

**Post hoc, ergo propter hoc** means "after this, therefore because of this." P happened, then Q happened, therefore P caused Q.

Hewitt's example is exact. You upgrade the Java version on a server. An hour later the server goes down. Therefore the upgrade took it down. He says he has seen that logic employed on critical incident calls countless times, and so have I. Mine usually involve a config change, a certificate rotation, or a deploy that landed suspiciously close to the first alert.

The reasoning is magnetic because it is so often right. Most outages do follow a change. You chase it, you find the smoking gun, and the habit gets reinforced. **That's what makes it dangerous. It works just often enough that nobody questions it.**

## What you've established

Here is the line from the book I keep coming back to. **All you have done is identify a candidate to investigate.** That is a necessary step. It is not a conclusion.

The change log is a lead, not a verdict. The moment you treat it as a verdict, you stop investigating. You roll back the Java upgrade, the server recovers because the traffic spike passed on its own, you declare victory, and the real cause is still sitting in the system waiting for its next chance.

I have been on both sides of this. I have closed incidents that came back a week later with the original symptom, because we treated the last change as the cause instead of the first suspect. And I have watched teams burn an entire crit-sit chasing a rollback that fixed nothing while the actual fault, an exhausted connection pool, quietly worsened.

## Where it hides outside incidents

Once you know the name, you start hearing it everywhere.

- **Metrics.** A dashboard trends the wrong way right after a release, so the release gets blamed. Nobody checks whether the trend started a month earlier.
- **Compliance.** A control fails an audit the quarter after a new process was introduced, so the process gets scrapped. The control may have been failing quietly for a year.
- **Performance.** A page feels slower after a refactor, so the refactor gets reverted. The real cost was a cold cache that nobody warmed.

In every case the change is a genuine candidate. In every case treating it as the cause stops you from asking the next question.

## The discipline

Hewitt doesn't say to ignore what changed. He says isolate it, then verify it. The change points you at where to look. The evidence tells you what to conclude.

Three habits have helped me.

1. **Write down the causal claim explicitly.** "The Java upgrade caused the outage." Stating it plainly makes it obvious how much you have not tested.
2. **Ask what else changed.** If the answer is nothing, look harder. Something did, even if it was traffic, a config drift, or a neighbouring service.
3. **Try to disprove it.** Roll forward in a test, or check whether the symptom pre-dates the change. A theory that survives an attempt to kill it is worth acting on.

None of this is slow. It is faster than the second outage.

## Remember

The change is a suspect, not a verdict. Ask what changed, then ask what proves it. **Correlation tells you where to look. Only evidence tells you what you found.**

That distinction is the whole difference between an incident you close and one you'll be back on at 2am.
