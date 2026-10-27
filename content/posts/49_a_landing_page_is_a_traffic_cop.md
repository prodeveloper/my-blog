+++
title = 'A Landing Page Is a Traffic Cop'
date = 2026-10-27T09:00:00Z
draft = true
+++

I keep a lot of pages. Dashboards, plans, trackers, small reports that refresh overnight. Over time I noticed a pattern: the page I open first every morning was always the one in the worst shape. It had grown links, notes, half a status report, a setup guide and a reminder to myself from three months ago.

A short passage in *Software Engineering at Google* named the problem for me.

## The Page That Tries to Do Everything

The book describes the typical team landing page: some interesting links, a few documents titled "read this first!", and information for both the team and its customers. These pages start out useful. Then they become so cumbersome to maintain that, in the authors' words, they get fixed "by only the brave or the desperate."

That was my front page. Every time something new mattered, I added it there, because that was where I would see it. **The page became important precisely because I kept putting things on it, and it became unusable for the same reason.**

## Direct Traffic, Don't Carry Cargo

The fix the book offers is simple. A landing page should state its purpose and then link out. Nothing else.

> If something on a landing page is doing more than being a traffic cop, it is not doing its job.

I like the image. A traffic cop at a junction doesn't carry anyone's shopping. They point, and people move on to where they need to be. **A good landing page is judged by how quickly you leave it.**

So when I rebuilt mine, I applied three rules:

1. **One sentence at the top saying what the page is for.**
2. **Everything substantial lives on its own page**, with a single link from the front.
3. **If it scrolls more than a screen or two, split it by topic** into sections, each with its own short list of links.

The setup notes moved to their own page. The status snippets moved to the dashboards that already owned that data. The front page shrank to something I can read in ten seconds.

## Don't Serve Two Masters

The second point in the passage hit harder. Most messy landing pages serve two audiences at once: the people who use what you build, and the people who build it. **What your team needs to know is different from what your customers need to know**, and one page trying to satisfy both ends up confusing everyone.

Think of a restaurant. The menu is for diners. The prep list taped inside the kitchen door is for the cooks. Nobody would print the prep list on the back of the menu, yet that is exactly what a mixed landing page does.

I had done this too. My front page mixed what I wanted others to see with my own working notes. Splitting them into a public-facing page and a private working page made both clearer, and made it obvious which one needed polish and which one could stay rough.

## Concepts Need Their Own Home

The same section makes a related point about concept documents: explanations of how several pieces fit together. They are the hardest documents to write and the most neglected, partly because there is no natural place to put them. The book's line is that if comments are the unit tests of documentation, **concept documents are the integration tests.**

When I find myself stuffing an explanation onto a landing page, it's usually a concept document that has nowhere else to live. The answer isn't to cram it in. It's to give it a page and point to it.

## Remember

- A landing page states its purpose and links out. That's the whole job.
- If the page scrolls for screens, split it by topic.
- Keep the page for users separate from the page for the team.
- Explanations of how things fit together deserve their own document.

The page you open first should be the one that gets you somewhere else fastest.
