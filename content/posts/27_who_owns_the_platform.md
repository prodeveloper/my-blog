+++
title = 'Who Owns the Platform?'
date = 2026-08-04T09:00:00Z
draft = true
+++

![A layered platform stack](/images/27-orchestration-layers.png)

I've been spending a lot of time lately building internal platforms. The nkosi dashboard, the action scan pipeline, the compliance automation layer. These are the kind of tools that make everything else possible but don't always get the attention they deserve.

And I keep running into the same question: **who actually owns this thing?**

It sounds obvious. You build it, you own it. But internal platforms are weird. They touch every team. They cross every boundary. The compliance team needs them. The engineering team needs them. The product team wants reports from them. And suddenly the question of who's accountable for what gets very fuzzy.

## The RACI That Nobody Writes

I was reading Eben Hewitt's *Technology Strategy Patterns* and came across something that made me stop. The RACI framework: Responsible, Accountable, Consulted, Informed. It's a project management staple, but Hewitt makes a point that hit home:

> The primary mistake I see people make in RACIs is the temptation to assign multiple people as accountable for a given item.

This is exactly what happens with platforms. Everyone has a stake, so everyone gets a finger in the pie. But **accountability without singularity is just diffusion**. When two people are accountable, nobody is.

The book insists: one accountable person per work item. If it feels like you need two, the task probably isn't defined properly. Split it. Recast it. But don't let the ambiguity slide.

## What This Looks Like in Practice

Take the nightly action scan I've been building. It auto-resolves issues, injects into dashboards, and feeds the compliance pipeline. On paper, it's mine. But in practice:

- The **compliance team** is consulted on what constitutes a valid action
- **Engineering** is informed when their services trigger alerts
- **Operations** is responsible for responding to the outputs

One accountable person (me, for now). Multiple responsible parties. Clear consulted and informed lanes. It works because the boundaries are explicit.

The moment I tried to make both compliance and engineering "accountable" for the scan results, we got nowhere. Compliance wanted stricter thresholds. Engineering wanted looser ones. The scan sat in limbo for two weeks. **One accountable person broke the deadlock.**

## The Life Cycle Lens

Hewitt also talks about company life cycle stages (introduction, growth, maturity, decline) and how your tech strategy should shift with each one. This matters for platforms too.

A platform at a **growth-stage** company needs to prioritise speed and market fit. You ship fast, you iterate, you don't over-engineer. A platform at a **mature** company needs operational excellence, clear SLAs, and documented ownership. The same codebase, same team, different strategy.

I think about nkosi this way. It's in a growth phase, with new features landing weekly and the shape still evolving. But I'm already thinking about what maturity looks like. **The RACI I write today is the foundation for the governance I'll need tomorrow.**

## The Value Chain Test

The last piece that stuck with me is Porter's Value Chain. The idea is simple: map every activity in your organisation to see where value is actually created versus where it's just supported.

For a platform team, this is humbling. Most of what we build is **support**: it enables value creation but doesn't create value directly. That's fine. But you need to know the difference. If you're spending 80% of your time on support activities and calling it product work, you're fooling yourself.

I've started tagging my weekly work against the value chain. Inbound logistics (data ingestion), operations (transformation), outbound logistics (dashboard delivery). It's a useful forcing function. **If I can't map a task to a value chain activity, I question whether it needs doing.**

## Remember

Platforms are invisible when they work and painfully visible when they don't. The difference between a platform that enables and a platform that entangles is often just clarity of ownership. Write the RACI. Know your life cycle stage. Map your value chain. The tools are simple. The discipline is the hard part.
