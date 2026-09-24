+++
title = 'The Backlog That Ranks Itself'
date = 2026-09-24T09:00:00+01:00
draft = true
+++

---

Most of my working hours lately have gone into triage. A vulnerability backlog with 123 open findings and 76 fixed. Compliance gaps with owners and dates attached. Review cycles that need to actually happen on a schedule. I have been treating all of it as a question of effort and discipline, and then I read the ranking section of the Code Search chapter in *Software Engineering at Google* and recognised my own queue in it.

The chapter is about searching code at Google's scale, but the problem it describes is not really a search problem. It is a prioritisation problem, and I have been living inside it.

## When ranking stops being optional

For a small codebase, ranking does not provide much benefit, because there are not many results anyway. Ten findings, and you just work them. Three hundred, and something has to decide the order.

That something is a ranking function, whether or not you named it. **If you have a backlog, you have a ranking function. The only question is whether anyone chose it deliberately.**

In Google's case, any short substring occurs thousands or millions of times. Without ranking, the user either checks every result in order or keeps refining the query until the set is small enough to eyeball. Both waste the developer's time. My version of this is scrolling a scanner report until something looks familiar, which is not a triage process. It is a search for recognition.

## The signal that eats itself

Their two headline signals are the number of file views and the number of references to a file, the second one borrowed from page rank with include statements standing in for web links. That second signal is the interesting one, because it is structural rather than popularity-based: it measures how load-bearing a file actually is, not how often someone happened to open it.

The first one has a flaw the authors are candid about. Scoring frequently viewed documents higher increases the chance that developers look at them, which decreases the chance for everything else to reach the top of the list. **They name it exploitation versus exploration, and that is exactly what a stale backlog is.**

The item at the top of my Snyk queue is not necessarily the worst one. It is often the one I have looked at five times, because looking at it pushed it higher. Effort compounds on the things I have already touched. That is a feedback loop wearing the costume of a priority order.

## New things arrive with no signal at all

The part that landed hardest is their admission that this is a problem for new files, which do not yet have enough information for a good signal. Anything that just arrived is structurally the hardest thing to surface, because the only signal it has is the one it has not accumulated yet.

I have watched this play out in my own dashboards. A finding that has been open for months has references, comments, a history, and a rank. A finding that appeared this morning has none of that. So the newest work loses to the oldest work by default, and the queue slowly calcifies around whatever was there first.

In search this is inconvenient. In a security backlog it is a real risk, because a fresh critical issue enters the queue looking exactly like a fresh trivial one until somebody reads it.

## The ranking is a product decision

Google does not treat the signal set as natural law. They mention A/B search experiments and curation of training data as ways of correcting the loop. The lesson is that someone owns the ranking, and that ownership is where the quality comes from.

For a backlog, that means the order has to be built from things that actually describe severity: exploitability, exposure, blast radius, whether the thing is reachable at all. Not from familiarity. **How bad something is and how often I have looked at it are different variables, and only one of them deserves to drive the queue.**

The other useful line from the chapter is about why central tools win at scale: the utility of a central solution increases with the number of developers using it and the size of the code space. That is the argument for one hub over five spreadsheets, and I have been living that argument all year.

## Latency is a bill you can actually calculate

There is a second, harder-edged insight in the chapter that I have been ignoring in my own tooling.

Google processes more than a million search queries from developers per day. At that volume, adding just one second per request costs roughly 35 idle full-time engineers every day, against a search backend maintainable for about a tenth of that. The break-even sits around 100,000 queries per day, which is fewer than 5,000 developers.

Then they point out the loss is not linear. A UI feels responsive below 200 ms. After a second, attention drifts. After ten, the developer has context-switched entirely, which carries well-known productivity costs. **The recommendation is sub-200 ms for every frequent operation, and the reasoning behind it is arithmetic, not perfectionism.**

I have been treating the friction in my own dashboards as free. A slow page, a manual step, a report I have to rebuild by hand. None of it shows up as a line item, so I have let it run. At my volume it is not thirty-five engineers, but the pattern holds at any scale: **friction on work you do daily is a recurring tax, and it is invisible precisely because it is small.**

## Where this leaves me

Two changes, both small. First, I am going to separate severity from familiarity in the queue and make sure the newest items get read on their own merits instead of waiting to accumulate a signal. Second, I am going to stop accepting slow routine operations as a fact of life and measure the ones I hit every day.

The ranking insight is the one that stung. I have been trusting an order that was never designed, produced by signals I never chose. That is the same mistake I wrote about in [A Pile of Tools Is Not a Strategy](/posts/a_pile_of_tools_is_not_a_strategy/), just one layer down. The tools were not the strategy, and the order was not the priority.

Both were just whatever happened to be in front of me.
