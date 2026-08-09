+++
title = 'Infrastructure Teams: Enabler, Not Gatekeeper'
date = 2026-08-06T09:00:00+01:00
draft = true
+++

I've been reading Eben Hewitt's *Technology Strategy Patterns*, and one passage stopped me cold. It's about infrastructure teams and the trap they fall into.

Hewitt describes two mentalities for infrastructure teams. The **enabler** provides quick, reliable support to the teams building customer-facing products. The **gatekeeper** uses standardization as a weapon, a way to keep the business units in line.

He doesn't mince words. "Overindexing on standardization for its own sake to the detriment of customers is missing the point at best and an abuse of power at worst."

## The Trap

I've seen this play out in every organisation I've worked in. A central platform team gets formed to solve a real problem: consistency, security, operational excellence. They build standards, create templates, set up review gates. And slowly, imperceptibly, the mission shifts from "how can we help you move faster?" to "you need to follow our process."

The language changes too. "We need to govern this." "That doesn't meet our standards." "You'll need to submit a request."

None of it is malicious. It's the natural drift of any team that stops talking to its customers. When your only feedback loop is the ticket queue, every request starts to feel like an imposition.

## What Enabling Actually Looks Like

The teams I've seen do this well share a few patterns:

**They measure the right thing.** Not how many tickets were closed or how many standards were enforced. They measure how fast their internal customers can ship, how often they're blocked by infrastructure, and how much time they spend working around platform limitations.

**They treat their internal customers like real customers.** That means understanding their workflows, their pain points, and their deadlines. It means saying yes more often than no, and when you have to say no, offering a viable alternative.

**Standardisation is a means, not an end.** The goal of a standard isn't compliance. It's making it easier for teams to build on something reliable, to train new people, and to count on the platform. If the standard makes life harder for your customers without a proportional benefit, it's not a good standard.

## Where This Hits Home

I've been spending time on **nkosi** recently, our internal dashboard and automation platform. The work has been about making the agents report more useful, getting the action scan to auto-resolve, and cleaning up the per-section history so it keeps the last 30 entries instead of overwriting.

This is classic enabler work. The platform exists so other things can run on top of it. Every improvement I make to nkosi is an improvement to every system that depends on it. That's the leverage of good infrastructure.

But I can feel the gatekeeper pull too. When I'm tempted to say "that doesn't fit our data model" instead of "let me help you make it fit." When I reach for a policy instead of a conversation. When the ticket queue feels like a shield.

## The Wardrobe Test

Hewitt has a simpler test. He asks whether your infrastructure team would pass the "wardrobe test": whether the people running it see themselves as serving the business or policing it.

It's a good question to ask yourself regularly. Not annually in a retrospective. Every week, in the decisions you make about what to prioritise and how to respond to requests.

Because the teams you support will remember how you made them feel. And if they remember you as the team that got in their way, no amount of standardisation will make up for the trust you've lost.
