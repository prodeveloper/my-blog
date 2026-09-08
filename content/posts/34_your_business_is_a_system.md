+++
title = 'Your Business Is a System, So Design It Like One'
date = 2026-09-08T09:00:00Z
draft = true
+++

I keep coming back to a line from Eben Hewitt's *Technology Strategy Patterns*: **you are always building a system**. Your architecture is a system, your strategy is a system, your organization is a system, even your mental model as an observer is a system. Once you see that, the tools you already know from designing software start applying to everything else.

## The organization is a system

Hewitt's argument is simple and a little uncomfortable. You can architect an application, a data center, a project, or an organization. The valued properties are the same across all of them: fitness to purpose, scalability, extensibility, resilience, auditability, testability. And the principles are the same too. Hide details behind an interface. Apply the principle of least knowledge. Create a strong separation of concerns. Ensure loose coupling. Isolate what changes independently.

Read the SOLID principles again, but this time as a process designer. **Single responsibility means a process should have one and only one reason to change.** Interface segregation means a department shouldn't be forced to depend on interfaces it doesn't use. Dependency inversion means high-level functions shouldn't depend on low-level ones. It all maps.

I've spent a lot of time lately building automated compliance pipelines, dashboards, and notification processors. The ones that work feel like well-designed systems. The ones that fight me are the ones where responsibilities blur, where one person is the only interface to a process, where everything depends on a hero.

## Hero culture is a scaling problem

Hewitt lists the symptoms of an organization that can't scale, and they're painfully recognizable: a hero culture, single points of knowledge, single points of failure in processes, smart people who used to care and now don't, a business that still behaves like a startup.

Here's the trap. **Hero culture is vicious because you don't want amazing feats to go unnoticed.** You don't want to alienate the people on whom everything depends. But if you reward the all-nighter, you build a system where the all-nighter is the only way anything gets done. The heroes get strokes for saving the day, so they never step back and fix the context that creates the disasters. Meanwhile everyone else stands around, underused and alienated.

The symptom is not the illness. Culture, strategy, and execution revolve around each other. But you can design your way toward better odds. If your processes are right-sized, nimble, and efficient, you give the cultural work a chance to take hold.

## The Origin Theory

Hewitt's Origin Theory is worth sitting with. Sometimes a company starts as a support function. A big company had a little IT shop, someone built an internal tool that worked well, and they spun it off to sell as a product. The theory states that the company will keep acting like a support function, even to its detriment. **You end where you began.**

The people who got nurtured through the ranks were hired to match the startup's size and culture, where heroics and wearing several hats were a necessity of survival. They don't think in terms of a P&L, or clear guardrails, or strongly separated responsibilities, because there was only one department and it was called Get Stuff Done. They think in terms of projects, long drawn-out loci for people doing activities, instead of outcomes.

I've seen this pattern in places that should know better. Even multibillion-dollar public companies can act like private ones because there's really one or two majority shareholders. Turning that around is hard. First you recognize it, then you get others to see it, then you rethink processes to define clear outputs and interfaces, then you make a cultural shift that changes who is on staff and how you manage customers.

## Build a scalable business machine

The fix Hewitt proposes is a scalable business machine. It's a set of processes across business functions, designed so the business can grow without breaking. The building blocks are small and familiar:

- **Action**: one atomic activity within a single department that produces something of clear value. Create, approve, or review. One role responsible, a clear deadline, a discrete task.
- **Tool**: the application or service used to create a deliverable that someone else can review and use without participating in the process.

The point of a tool is that it formally expresses the output well enough that the consumer doesn't need to be in the room. That's the whole game. **If someone else can use your output without you, you've built an interface. If they can't, you've built a dependency on a person.**

This is fractal too. You can do it for one department or tie them all together into a single scalable metamachine of interrelated machines. It works locally and works the same globally.

## What this means for automation work

The reason I find this pattern so useful is that it reframes what I'm actually doing when I build a dashboard or a pipeline. I'm not just automating a task. I'm designing an interface between departments, a way for one part of the business to consume the output of another without a hero in the middle.

When a compliance tracker reconciles itself nightly, when a notification processor trims its own data, when a dashboard updates without anyone pulling an all-nighter, that's a scalable business machine doing its job. The automation is the tool. The process is the system. And the system is designed so the value flows without depending on any single person.

**The best thing you can build is a system that works when you're not in the room.** That's the whole point of externalizing what you know, making a template every time you solve a problem, so the problem can be solved again without you when next it arises.

## Remember

You are always building a system. Design your processes with the same care you'd give your software. Give every process a single responsibility, hide the details behind an interface, and make sure the output is consumable without the producer being present. Kill the hero culture by making heroes unnecessary. That's how you scale.
