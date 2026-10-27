+++
title = 'Inspect Your Own House Like You Are Buying It'
date = 2026-10-27T09:00:00Z
draft = true
+++

When you buy a house, you hire a surveyor. They walk through every room with a clipboard, tap the walls, look in the loft and write down what they find. When you have lived in a house for ten years, nobody does that. You stop seeing the crack above the door because it has always been there.

Software products are the same. **The people who build a system are the worst placed to see its state, because they have learned to step around its flaws.**

## The Buyer's Checklist

I have been reading Eben Hewitt's *Technology Strategy Patterns*, and one of his templates is a due diligence assessment. It is the tool you would use if your company were about to acquire another one and you had to judge its software. You break the product into a dozen characteristics, write drill-down questions for each, and score every item on a simple scale from 0 (absent) to 4 (implemented and world-class).

The scale matters more than it looks. A feature that is missing and not on anyone's plan sends a different signal from a feature that everyone agrees is important but hasn't been built yet. **A score is only useful if it separates "we forgot" from "we know and we're getting to it."**

## Turn It Inward

The part that stuck with me is his third use for the template. Most of us are not buying companies. So run the due diligence on your own product, as if you had been sent from another firm to assess it.

I have been doing something close to this in my own work. I keep a long list of open findings and work through it every week, and I treat our own controls the way an outside reviewer would: what is the evidence, where does it live, would a stranger accept it? Pretending to be the outsider changes the questions. You stop asking "is this fine?" and start asking "could I prove this is fine to someone who doesn't trust me?"

**Playing the outsider lets you be objective without being political.** You are not criticising a colleague's work. You are filling in a worksheet.

## What You Get Out of It

Once the scores are in, three things fall out for free:

- **A roadmap for technical debt.** The low scores are your backlog, already ranked.
- **A shared language with other leaders.** "Observability is a 1" is easier to discuss than a vague sense that things are fragile.
- **A baseline.** Run it again in six months and you can see whether you moved.

## Write It Down

Hewitt is blunt about the alternative. In many teams, architecture lives in clever people's emails and meetings. It can't be traced, it can't scale, and it vanishes when those people leave. His line that landed hardest for me: **there's never enough time to do it right, but somehow always enough time to do it over.**

A written assessment is the opposite of that. It is boring, it is a spreadsheet, and it outlasts the conversation that produced it.

## Remember

Once a year, walk through your own house with a clipboard. Score every room as if you were deciding whether to buy it. The cracks you find are the ones you had stopped seeing.
