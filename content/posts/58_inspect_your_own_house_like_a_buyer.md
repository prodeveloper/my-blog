+++
title = 'Inspect Your Own House Like a Buyer'
date = 2026-11-26T09:00:00Z
draft = true
+++

When you buy a house, you pay an inspector to walk through it with a clipboard. They open the fuse box, check the roof, run every tap. They have no attachment to the place. They are not proud of the kitchen renovation. They write down what they see.

Nobody does this for the house they already live in. You stop noticing the sticky door and the stain on the ceiling. They become furniture.

## The template meant for buying companies

I've been reading Eben Hewitt's *Technology Strategy Patterns*, and one of his templates is a due diligence worksheet. It was built for acquisitions: you are about to buy a company and need to know what its software is worth. You break the product into a dozen characteristics, write drill-down questions for each, and score every item from zero to four, where zero means unsupported and not planned, and four means implemented and world-class. The scores roll up into one summary page.

Then he makes the point that stuck with me. **The best use of this template is pointing it at your own product.** Pretend you were sent from another company to assess it. Score it as a stranger would.

## Why the outsider sees more

Inside a team, every weakness has a story. That service is slow because of a decision made three years ago. That area has no tests because the person who knew it left. The stories are true, and they are also anesthetic. They make the problem feel explained, and an explained problem feels handled.

An inspector doesn't hear the stories. They write "no tests" and move on. **A score of one is a score of one, whatever the history behind it.**

The scale also separates two things that feel the same from inside. Something unsupported and not on the roadmap is a different signal from something everyone agrees matters and is prioritized but not done. Both are "missing." Only one of them has a plan.

## What I've been doing with it

I run a weekly walk through a long list of open findings in our codebase, and a register of things blocking the team. Both work best when I stop reading them as the person who lives in the house. A finding that has sat there long enough starts to look like part of the wall. Reading it as a buyer would, the question changes from "why is this still here" to "what would this cost me if I bought the place today."

That shift does two things:

- **It turns technical debt into a roadmap.** Low scores, sorted by how much they matter, are a plan you can hand to a team.
- **It gives you a language for other leaders.** "We score a one on recovery" lands better than a paragraph of context, and it invites the question of what a three would take.

## Writing it down is the point

Hewitt is blunt about architecture that lives only in email threads and meetings. If the thinking exists only in the heads of the people in the room, the organization can't scale past those people, and nobody can be held to a decision they never recorded. He has a line I keep repeating: there's never enough time to do it right, but somehow always enough time to do it over.

The self-assessment works for the same reason. **A score on a page can be argued with, revisited and improved. A feeling in a meeting can't.**

## Remember

Hire yourself as the inspector. Walk through your own product with a clipboard, score what you see without the stories, and write it down. The sticky door has been there so long you stopped seeing it. A buyer would see it on the first visit.
