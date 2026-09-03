+++
title = 'The Customization Tax in Infrastructure'
date = 2026-09-03T09:00:00Z
draft = true
+++

I've been working through *Software Engineering at Google* again, and the chapter on Borg's compute architecture keeps pulling me back to a lesson I feel every time I touch our internal tooling. It's the story of what happens when you let one special case at a time erode a platform you thought was coherent.

## The free lunch that isn't

The part that grabbed me first was Google's trick for running batch jobs almost for free. Serving jobs need headroom so they can survive a spike or an outage. That headroom sits idle most of the time, which feels wasteful. The temptation is to overcommit the machine. But Borg does something smarter: it fills that slack with batch jobs, on the condition that the batch work gets reclaimed the moment a serving job needs the resources.

Batch jobs are happy to soak up whatever's spare because they measure performance in aggregate throughput across hundreds of workers. Kill a few replicas and nothing breaks, you just reprocess. In Google's case, most of the time, batch effectively ran for free.

The mental model underneath it is the real insight: **serving jobs and batch jobs are different animals, and treating them the same wastes both.** One cares about individual latency, the other about total throughput. One needs a graceful shutdown with warning, the other can be killed at will.

## The cost of special cases

The second half of the chapter is where it gets uncomfortable. Google built one compute platform, Borg, and then every team that needed something different pushed it a little further from coherence.

The Cloud team needed live migration for VMs, so Borg learned to avoid at-will killing. Search needed to survive disk failure on its own giant index, so Borg added an opt-out for default disk handling. Each of these was a reasonable request in isolation. Each one also added a flag, a mode, a carve-out. After enough of them, the API surface became large and unwieldy, and the intersection of behaviors became impossible to predict or test.

Nobody could answer what happened if a container asked for both the Cloud eviction treatment and the Search disk-failure treatment. Not because anyone was careless, but because the cumulative weight of special cases had outrun anyone's ability to hold it in their head.

This is the customization tax, and it's insidious because no single decision feels wrong. Each one is justified, even sensible. But **every carve-out you add to a shared platform is a small bet that you'll be the last person to need one.** Eventually you stop owning the platform and start negotiating with it.

## What this means for the rest of us

Most of us will never run a fleethood of servers, but the principle shows up everywhere Jacob-shaped infrastructure lives. I run a small army of automation: compliance dashboards, CAPA advance logic, notification pipelines, health checks, metrics scrapers. Each of them started clean. Each of them has accumulated its own little exceptions over time.

The pattern is the same at a human scale as it is at Google scale. The question is never "should I add this one thing to make my life easier right now." It's "am I willing to pay the interest on this carve-out for as long as this platform lives." Whitelisting power features, as Borg eventually did, is the sane middle ground. It acknowledges you can't say no to every reasonable request without killing the platform's usefulness, but it refuses to let power features spread silently.

## Remember

The next time you're tempted to special-case your shared infrastructure, pause on the two questions Borg's history answers for you. First, is this workload naturally cattle, or does it secretly need pet treatment? Second, if I add this carve-out today, who has to reason about the intersection of my carve-out and everyone else's next week?

Because the real cost isn't the code you write to handle your case. It's the coherence you lose across every other case that now has to coexist with yours.
