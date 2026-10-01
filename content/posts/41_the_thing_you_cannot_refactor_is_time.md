+++
title = 'The Thing You Cannot Refactor Is Time'
date = 2026-10-01T09:00:00+01:00
draft = true
+++

I finished *Software Engineering at Google* this week. Eighty-eight sections in, the part that stayed with me wasn't the chapter on build systems or the one on testing. It was the afterword, five pages from the end, where Asim Husain writes one sentence that I have not been able to get out of my head.

**"The passage of time and the importance of change cannot be ignored."**

That's the whole book, compressed. Everything else in it is a mechanism. That line is the reason the mechanisms exist.

## Shipping is the midpoint, not the finish line

Most of us learn software through the lens of delivery. You build the thing, you test the thing, you ship the thing, you move on. The reward is the launch.

The book reframes that. **Sustainability is the core of the discipline, not a phase after it.** Over a codebase's expected lifespan you have to react and adapt to changes in product direction, technology platforms, underlying libraries, operating systems, and everything else the world decides to move underneath you. None of that is hypothetical. All of it is coming.

The uncomfortable part is that a codebase has a lifespan and no one tells you how long it is. You only find out in hindsight, usually when someone asks you to change something a decade after the original decision was made.

## The number that never gets to zero

This week my Snyk reports came back at 251 open findings and 102 fixed. I've watched that number move for months. It has never gone to zero, and I've stopped pretending it should.

For a long time that bothered me. If you treat a finding list like a project, an endless list looks like failure. **If you treat it like a garden, an endless list is just what a garden is.** The goal was never a clean report. The goal is a trend that says you are keeping up, and a process that survives the person who set it up leaving.

That is the difference between a fix and a practice. A fix closes a ticket. A practice keeps closing tickets after you have stopped looking at them. One of those survives time. The other is a story you tell at a retrospect.

## Agility is not speed, it is durability

The afterword uses a phrase I want to steal: "resolute agility." Husain defines it as the ability to identify solutions that work for current-day problems *and* withstand inevitable changes to technical systems.

Read that second half again, because it rules out most of what gets called agility. **Fast is easy. Fast plus still correct in three years is the actual skill.** A shortcut that saves a week and costs a quarter of remediation is not agility, it is borrowing. Somebody always pays the loan back, usually someone who wasn't in the room when you took it out.

This is also why the book keeps circling back to versioning, deprecation, and long-lived interfaces. Those are not boring topics. They are the machinery that lets a system change without breaking the people depending on it.

## Why the combination is rare

Husain makes an admission worth quoting honestly: very few organizations have achieved *both* sustainability and scale. Most pick one.

- Startups get speed and spend it on debt they never repay.
- Large organizations get stability and calcify into change that costs a quarter of engineering to make.
- **The teams that get both treat code health as a standing commitment, not a cleanup project.**

That last line is the one I keep testing my own work against. When I advance a CAPA item, build the audit trail, or refresh a control on a schedule instead of in a panic, that is not bureaucracy. It is the maintenance window being funded on purpose, before the incident decides to fund it for me.

## The responsibility nobody assigns you

The afterword closes on something I did not expect from a book about build systems. It says technology that helps only a set of users isn't innovative at all, and that building for the sole purpose of innovation is no longer acceptable.

I think that is the same insight wearing different clothes. Time is the thing that exposes whether you built for a moment or for a user. **The features that survive are the ones that were designed for people who will still be here when the technology underneath them has been replaced twice.**

## Remember

You are not maintaining a snapshot. You are maintaining something that has to keep working while everything around it changes.

**The passage of time cannot be ignored, so you might as well plan for it.** Pick the practice over the fix. Pick the interface over the shortcut. Pick the boring mechanism that will still be right when you have moved on and someone else opens the file.

Time is the one dependency you cannot upgrade, refactor, or pin to a version. Everything else in the book is about making peace with that.
