+++
title = 'Plan How Your Data Leaves Before It Arrives'
date = 2026-11-05T09:00:00Z
draft = true
+++

I've been reading Eben Hewitt's *Technology Strategy Patterns*, and the chapter on architecture templates has a section on data that stopped me. He frames it as a list of questions: **how to get it, what to do with it, how much there is, how long to keep it, how to move it, and how to get rid of it.**

Most design documents I have read answer the first three well. The last three are usually missing.

## The Pantry Problem

Think of a kitchen pantry. When you move into a new home you plan carefully what goes in: which shelf holds the flour, where the tins sit, what you buy each week. Nobody plans what comes out. Two years later there is a jar of spice from a recipe you cooked once, three opened bags of rice, and something at the back that nobody can name.

Systems fill up the same way. **Data has an arrival plan and no departure plan.** Each record made sense when it came in. Nobody decided when it should leave, so it never does.

## Why the Exit Gets Skipped

Getting data in delivers visible value on day one. Getting rid of it delivers value years later, usually to someone else. So the question gets deferred, and deferred questions turn into permanent answers.

The cost shows up quietly:

- Storage and backup bills that grow every month without anyone choosing that
- Test environments filled with copies of real personal data because that was the easy way to populate them
- Audits where the question "why do you still hold this?" has no good answer
- Migrations that take months because nobody knows which old records still matter

I spend a fair amount of time on security and compliance work, and a large share of the findings I work through trace back to the same root. **Somebody stored something and nobody owned its ending.**

## The Questions Worth Asking Up Front

Hewitt's template turns this into a short checklist. I've started using a version of it before any new data store goes live:

1. **Volatility:** how often will this data change, and who changes it?
2. **Retention:** how long do we keep it, and what rule says so?
3. **Environments:** how do test and staging get data, and does it need to be real?
4. **Movement:** how does it get in, and how would we move it out if we switched tools?
5. **Disposal:** what deletes it, on what schedule, and how do we prove it happened?

The fifth one matters most. A retention policy that nothing enforces is a wish, not a policy. **If deletion is not automated, it is not happening.**

## Writing It Down Changes Behaviour

The value of putting these questions in the design document is not the answers themselves. It's that the team has to say them out loud before the first record lands. Once someone has written "records older than two years are removed by a nightly job", that job gets built. When nobody writes it, nobody builds it.

## Remember

Every piece of data you collect is a small promise to look after it. Decide how it leaves on the same day you decide how it arrives, and the pantry stays one you can find things in.
