+++
title = 'Treat Changes Like Cattle'
date = 2026-08-13T09:00:00Z
draft = true
+++

Reading through the Large-Scale Changes chapter in Software Engineering at Google, one line kept pulling me back: the analogy of **pets versus cattle**. A handcrafted change is a pet. You spend days on it, you know it intimately, and you feel a small sting when a reviewer rejects it. A change churned out by automation is cattle. It's nameless, it's faceless, and losing a few of them on any given day costs nothing, as long as the herd moves forward.

That reframing has quietly changed how I think about the automation I run every day.

## The shift from pets to cattle

Most of my recent work is automation. CAPA items, dashboards, email digests, Teams conversation logs, cron jobs that run on their own schedule. These generate a lot of changes without me hand-crafting each one. And that creates a weird mental tension if I'm not careful.

For a long time I treated every commit like a pet. Each one deserved attention, care, a personal stake in its success. That worked when changes were rare and meaningful. It stops working when your tooling produces dozens of them a week.

The book makes the point that losing a few cattle now and then isn't a problem, because **automation means new changes can be regenerated at very low cost**. A merge conflict, a flaky test, a rejection. None of it is a tragedy. The herd is what matters.

## The real lesson is the investment in tooling

Here's what struck me most. Google holds that if a change requires more than 500 edits, it's usually more efficient to learn the change-generation tooling than to do it by hand. And the tooling should be comprehensive, so the author can be confident the change covers every case it's meant to fix.

That's a hard bar, but the principle scales down. **Every hour I spend building better automation pays for itself if it replaces repetitive manual work.** My dashboards and cron jobs are exactly that. They don't just produce output. They turn one-off manual effort into something repeatable, testable, and cheap to regenerate.

The early investment is the part that's easy to skip, and it's the part that matters most.

## The approval process is the hard part

The chapter spends a lot of time on Google's approval process for LSCs. A committee of experienced engineers reviews the plan before the change ships. The goal isn't to block work. It's to make sure widespread automated changes have some oversight, rather than indiscriminate tweaking.

I felt this one directly. The easy path with automation is to let it run and trust the output. The better path is to keep a human review layer in front of it. That's why my compliance dashboards aren't just generated and forgotten. They feed into dated approval packs. There's a checkpoint between "the automation produced this" and "this is now a decision."

**Automation makes the work cheap. Review keeps the work sane.**

## A formatter a day keeps the chaos away

One detail I enjoyed: Google runs automated formatters as a separate pass on every LSC-generated change, so the output "fits in" with code written by a human. Without that, automated changes would never have become accepted.

Same instinct applies to my output. When a cron job generates a dashboard or a digest, it should look as if a person cared about it, even if a person didn't. Consistent formatting is the difference between output people trust and output people skim.

## Remember

If everything you ship is a pet, you'll never scale past what you can personally attend to. Build the tooling, trust the herd, and keep a light human hand on the review. That's the balance worth stealing from Google's playbook.
