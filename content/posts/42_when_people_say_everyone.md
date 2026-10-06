+++
title = 'When People Say Everyone, They Never Mean Everyone'
date = 2026-10-06T09:00:00Z
draft = true
+++

"Everyone needs to sign this off." "Nobody uses that feature." "All the teams are blocked."

I hear sentences like these every week, and I say them too. They sound like facts. They are almost never facts. In *Technology Strategy Patterns*, Eben Hewitt makes a case that surprised me: the most important skill in strategy work might be knowing what you're talking about, in the literal sense.

## The Domain of Discourse

Hewitt borrows an idea from predicate logic called the **domain of discourse**. It's the set of things a statement is about. "Everything is in New York City" sounds absurd, but if your domain contains only the Empire State Building, the statement is true.

That's the trick. **Every claim lives inside an unstated boundary, and the claim is only as good as the boundary.** When someone says "everyone," they don't mean every person alive and dead. They mean something like "the six analysts in that room who used the feature last Tuesday."

His suggested move is simple. Take the absolute statement literally and ask: "Is that true for everyone, always, in all cases?" The answer is always no. Then you get the real claim, which is smaller and far more useful.

## Where I've Seen This Bite

I've been rolling out document sign-off across a set of compliance documents. Early on, the plan said "all signers get notified." Then the questions started:

- All signers on which documents?
- All signers now, or including the people appointed next month?
- Does "approved by" mean the person in the role, or the person named in the delegation of authority?

Each question shrank "all" into a set I could list. **Once the set had members with names, the design got easy.** We turned signer emails off for the first rollout, because the honest domain was "a small group we can talk to directly," not "everyone."

The same pattern shows up in blocker tracking. "We're blocked on access" sounds like one thing. Push on it and it becomes three tickets, two teams, and one person waiting on one approval for 48 days. That's a claim you can act on.

## One Thing or Two Things

Hewitt connects this to system design. Before you decompose a system, check whether two ideas are one thing or two. A book and an instructional video may carry the same content but have different production, audiences, and channels. Depending on where the business is going, they might be one domain or two.

**Architects who skip this step make assumptions about the boundary and then decompose the system in the wrong place.** The code ends up faithfully modelling a sentence nobody examined.

## Hypotheses First, Data Second

The same chapter makes a related point I like. Don't wait for all the data, because there is no such thing as all the data. Draw a line around a set of propositions, make a bold claim, and have people who aren't yes-men argue with it. **Let the cost of being wrong decide how much analysis you do before acting.**

Drawing the domain is what makes that possible. You can't test a hypothesis about "everyone." You can test one about six analysts.

## Remember

- When you hear "everyone," "nobody," or "always," ask who is actually in the set.
- Write down the members before you design anything for them.
- Check whether two things are one thing before you split or merge them.
- Make a claim early, then let the data change your mind.

**Saying something is certain when it isn't sinks ships. Shrinking the claim to its real domain keeps them afloat.**
