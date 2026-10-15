+++
title = 'The Smallest Step Forward'
date = 2026-10-15T09:00:00Z
draft = true
+++

I have been reading the dependency management chapters of *Software Engineering at Google*, and one idea from them keeps coming back to me. It's called Minimal Version Selection. It sounds like a niche build tool detail, but the lesson underneath it applies to much more than software.

## The Version You Were Tested Against

When a library says it needs "version 1.7 or newer" of something, most tools grab the newest version available. Minimal Version Selection does the opposite. It picks 1.7, the lowest version that satisfies the request.

The reasoning is simple. **If the author wrote "1.7 or newer", the author almost certainly had 1.7 installed.** That pairing is the one combination with at least some evidence that it works. Version 1.8 might be fine in theory. Nobody has checked it in practice.

The book puts it neatly: walk forward only as far as you were asked to, then stop and run your tests.

## Promises Lose Detail

Version numbers are a promise. "This is a minor release, nothing will break." The authors point out that this promise is a compression. A whole set of changes gets squeezed into three numbers, and **every compression throws away detail.**

At small scale the lost detail rarely hurts. With a handful of careful, well maintained dependencies, the promises mostly hold. As the number of things you depend on grows, the small inaccuracies stack up. You get upgrades that should have worked and don't, and combinations that would have worked but get refused.

## The Same Pattern Outside Code

I see this pattern in my own work, which has little to do with build tools. I keep a set of documents, registers and weekly reviews that describe how a system is run. Recently I tidied how readings get recorded so that every number lives in one place with a reason next to it.

The temptation with work like this is to rewrite everything in one big pass. One clean new version. The problem is the same one Minimal Version Selection solves. **The current version is the one people have used. It has been tested by reality.** A big rewrite throws that evidence away and replaces it with a promise.

So I move in small steps. Change one document. Let it go through a review cycle. See whether anyone trips over it. Then take the next step.

It's like rearranging a kitchen. You could empty every cupboard on a Saturday and put everything somewhere better. On Monday morning nobody can find the coffee. Or you move one shelf, live with it for a week, and move the next. The second approach feels slower and finishes sooner.

## Why Small Steps Are Safer

The book makes a comparison I like. Committing an hour of work is safer than dumping a year of work at once. Dependency updates follow the same rule. So does process change, team change and personal habits.

Small steps give you three things:

- **A short list of suspects** when something breaks
- **Evidence** that each step works before you build on it
- **A cheap way back** if a step was wrong

A big jump gives you none of these. When it fails, everything changed, so anything could be the cause.

## Remember

Newer is not the same as tested. When you have something that works, treat it as evidence, not as debt. **Move forward only as far as you need to, then stop and check.** The smallest step that gets you what you asked for is usually the right one.
