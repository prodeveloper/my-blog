+++
title = 'Every Rule Must Pull Its Weight'
date = 2026-10-22T09:00:00Z
draft = true
+++

I spend a fair amount of my week writing rules. Not code rules, mostly. Policies, checklists, the small agreements that keep a team moving in the same direction. Lately I've been rereading the chapter on style guides in *Software Engineering at Google*, and it gave me a better test for whether a rule deserves to exist.

## Rules Have a Cost

The book makes a point that sounds obvious once you hear it: **every rule you add is a tax on everyone who has to learn it.** A new person joining the team has to read it. A veteran has to remember it. Someone has to maintain it when the world changes.

Google's C++ guide has no rule against `goto`. Not because `goto` is fine, but because almost nobody uses it. Writing the rule down would cost every engineer a little attention to prevent a mistake that one or two people might make.

I recognise the opposite habit in myself. When something goes wrong once, my first instinct is to write a rule so it never happens again. Do that for a year and you end up with a handbook nobody reads, which means the rules that matter get lost among the ones that don't.

## A Kitchen Example

Think about a shared kitchen at home. You could post twenty rules on the fridge: rinse the cups, wipe the counter, label the leftovers, don't use the good knife on bread, and so on. Within a month, nobody reads the list.

Or you could post two: **dishes go in the dishwasher, and whoever empties the bin replaces the bag.** Those are the two things that cause real friction. Everything else is handled by ordinary good sense and the occasional conversation.

The second fridge works better, not because people care more, but because the rules are few enough to remember.

## Write for the Reader

The second principle that stuck with me is to **optimize for the reader, not the writer.** Google would rather code be tedious to type than hard to read, because it gets read far more often than it gets written.

The same applies to any document that outlives the week it was written in. A policy written quickly in shorthand saves me ten minutes. It costs every future reader those ten minutes back, plus the risk that they misread it. I've started asking a simple question before I publish anything: **will someone who wasn't in the room understand what I meant, and why?**

That usually means:

- Saying the reason for the rule, not just the rule
- Spelling out the surprising cases, because those are where people get caught
- Using the longer, clearer word over the shorter clever one

## How I Apply It Now

When I'm tempted to add a new rule, I run through three checks:

1. **Is the mistake common?** If one person got it wrong once, a conversation is cheaper than a rule.
2. **Is it already self-evident?** If good judgement covers it, leave it out.
3. **Will a stranger understand it in a year?** If not, rewrite it until they would.

Most candidate rules fail the first check. That's fine. The ones that survive are the ones worth everyone's attention.

## Remember

A rulebook is not stronger because it is longer. **Fewer rules, written clearly, get followed. Many rules, written quickly, get ignored.** Make every rule earn its place.
