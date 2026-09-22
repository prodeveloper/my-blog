+++
title = 'A Pile of Tools Is Not a Strategy'
date = 2026-09-22T09:00:00+01:00
draft = true
+++

---

I have been spending a lot of my working hours lately on compliance automation, vulnerability backlogs, and the dashboards that try to hold all of it together. Somewhere in the middle of that, reading Eben Hewitt's *Technology Strategy Patterns*, I hit a line that made me stop and audit my own work.

**Many shops are just collections of tools.**

That stung, because it was almost true of mine. I had a scanner here, a dashboard there, a repo of policies, a pipeline running nightly. Plenty of moving parts. What I was not sure I had was a reason for any of them to exist other than the fact that each one solved the problem sitting in front of me at the time.

## Three layers, in order

Hewitt lays out a chain that I now run as a checklist on new work:

1. **Principles.** The propositions the team believes. Abstract by nature, but they should force action. If they do not, they are decoration.
2. **Practices.** The things people do every day. The processes, the way work gets done, the manner in which the principles show up in daily work.
3. **Tools.** The specific software that carries out the practices. Concrete, not abstract. Named things: Terraform, Kafka, a scanner, a ticketing system.

The ordering is the whole point. **The tools support the practices. The practices realize the principles.** Read it the other way and you have a pile.

If your principles are not a decomposition of the wider strategy, he is blunt about the outcome: you will be doing stuff that does not matter. That phrase keeps coming back to me, because it names something I have watched happen. Busy teams, real effort, clean boards, and a nagging sense that none of it is moving the thing that matters. That is what mistaking activity for progress looks like from the inside.

## The altitude problem

Here is where most principle statements die. Hewitt's example is a principle called "Global cloud." Short, confident, and completely inert. Stating it **will not drive an ounce of change in the organization**, because nobody can look at a project and say yes or no to it.

So you unpack it. Into the technical terms the people doing the work can act on:

- Services should externalize configuration, to keep them portable.
- Infrastructure as code should be employed.
- Services must expect to run across multiple regions, so they should be stateless and their data partitioned.

Now you have something real. From those statements the practices fall out almost automatically: infrastructure as code, CI/CD pipelines, service design review and governance. And only then do tools enter the picture. Something off the shelf, or built in-house with Python and CloudFormation. That choice comes after the practice, and it turns on the same logic I keep returning to: **build the things that are competitive differentiators for you, and buy everything that is not.**

## What the tools cannot do for you

The reason the pile keeps happening is that tools are the visible, buyable, demonstrable layer. Principles are a paragraph nobody reads. Practices are a calendar invite and a habit. But a tool arrives in a box, can be installed this week, and shows up nicely on a slide.

So the tool gets bought first. And then you have a scanner nobody triages, a dashboard nobody opens, a register nobody updates. **The tool is not the practice, and no amount of tooling will substitute for the cadence.**

I have seen the reverse version of this lately too, and it is more encouraging. The compliance work only started producing anything useful once the review cycle itself existed, as a practice with a date attached and someone accountable for it. Once that practice was real, the tooling had something to serve, and it stopped being an artifact and started being an instrument.

## What you leave out is a decision

Worth noting: a principle list is also defined by its omissions. The NASA CIO publishes a technology strategy built on vision, mission, principles, goals, outcomes, and it does **not** list "innovation" as a principle. It lists secure, integrated, cost-effective.

That omission is not an accident. It is a stance. Those three words drive a completely different set of decision criteria and a different set of adoption habits than "innovation" would. Choosing what to leave off the list is as strategic as choosing what goes on it, and most teams never make that choice consciously.

## Where this leaves me

The honest version of my checklist now looks like this. Before I add anything, I ask what practice it serves. Before I can name the practice, I have to know which principle it realizes. And if I cannot answer either question, the thing does not get added, no matter how good the demo was.

Hewitt's warning is that without this, you get less efficiency, less clarity, and less harmony, a diverse collection of overlapping tools, and a widening gap between what people do every day and where the strategy claims to be going.

The gap is quiet. It does not show up as an outage or a missed date. It shows up as a team that is working hard on things that turn out not to matter. That is worth an hour of auditing, and it costs nothing but honesty.
