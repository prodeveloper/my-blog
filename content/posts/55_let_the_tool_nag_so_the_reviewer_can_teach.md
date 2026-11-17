+++
title = 'Let the Tool Nag So the Reviewer Can Teach'
date = 2026-11-17T09:00:00Z
draft = true
+++

In the early days of Google, one engineer sat down with every new hire and reviewed their first big commit line by line. Whitespace, naming, which shared library to use, how code is written here. It worked beautifully until the company hired faster than one person could read.

I've been reading the knowledge sharing chapter of *Software Engineering at Google*, and the part that stuck with me is not the mentorship program that grew out of that habit. It's the quiet line about what happens to it over time: **every comment a tool can make is a comment a human no longer has to.**

## The Two Kinds of Review Comment

Think about a head chef training a new cook. Some of the corrections are about rules: wipe the board between proteins, label the container with the date, knives go back on the magnet. Others are about judgment: this sauce needs more acid, you plated this before the fish rested, a guest with that order will want the dressing on the side.

The first kind is important, but it doesn't need the chef. A printed checklist by the station, a colour code on the boards, a label maker that stamps the date automatically. **The second kind is the only reason you need a chef standing there at all.**

Code review has the same split. "Trailing whitespace" and "this name breaks our convention" are rules. "Someone outside this team won't follow this function" is judgment. When a reviewer spends their attention on the first kind, they have less left for the second, and the author learns that review is about nitpicks.

## What I Changed in My Own Work

I write a lot of things that other people read: reports, status notes, posts like this one. For a while I had a written style guide and a habit of rereading against it. The rereading caught most things. It also took the energy I needed for the harder question, which is whether the piece says anything worth reading.

So I turned the rules into a script. It fails the draft on banned words, on punctuation I've decided not to use, on details that should never leave work. It runs before anything gets published. **The rules stopped being something I remember and became something I can't skip.**

Two things happened that the book predicts:

1. **The rules got applied every time**, not just on the days I was paying attention.
2. **My review moved up a level.** I stopped scanning for dashes and started asking whether the example lands, whether the lesson is clear, whether the closing earns its place.

## Where the Line Sits

The trap is thinking the tool replaces the mentor. It doesn't. The book is clear that the human program stayed, and the reviewers were expected to cite the reason behind each rule, so authors learn why the fence is there before they move it. A tool can tell you that something broke a rule. It can't tell you whether the rule fits this case, and it can't tell you that the whole approach is wrong.

A useful test for any comment you find yourself repeating:

- **Could a script say this?** Write the script.
- **Does it need context about the reader, the goal or the trade-off?** That's yours to say, and now you have the time.

## Remember

Every repeated correction is a candidate for automation. Move the rules into tools, and **spend the human attention on the things only a human can see.** The chef should be tasting the sauce, not checking the labels.
