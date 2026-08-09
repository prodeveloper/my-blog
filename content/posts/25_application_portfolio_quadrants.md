+++
title = 'The Four Things You Can Do With Any Application'
date = 2026-07-28T09:00:00+01:00
draft = true
+++

![A portfolio of applications](/images/25-data-sources.png)

I've been reading Eben Hewitt's *Technology Strategy Patterns*, and one framework jumped out at me because it maps so cleanly onto the decisions I make every week.

It's the Application Portfolio Management quadrant. Four boxes. Every application you own fits into one of them, and each box tells you exactly what to do next.

## The Quadrant

Score each application on two axes: **business value** (how strategically important is it?) and **technical health** (how much debt, risk, or entropy has accumulated?). Plot them on a 2x2 grid, and you get four postures:

**1. Grow / Evolve / Maintain.** High value, healthy tech. These are your stars. Keep investing, keep the team strong, don't let them atrophy through neglect. The risk here is complacency: assuming they'll stay healthy without deliberate attention.

**2. Tolerate.** Low value, healthy tech. They exist for a reason, but they're not your future. Staff them lean, minimize cost, and figure out a plan to consolidate or retire them eventually. The trap is letting them linger forever, quietly draining budget.

**3. Retire.** Low value, high debt. These are the hardest conversations because there are always people attached to them. But the math is clear: the cost of keeping them exceeds their contribution. Kill them, consolidate any salvageable function, and move on.

**4. Reengineer / Modernize / Replace.** High value, high debt. These are the painful ones. They're critical to the business but have been mismanaged: short-term feature investment, no architectural care, a revolving door of leaders who kicked every can down the road. You can't ignore them because they matter. But fixing them is expensive, slow, and politically fraught.

## Where This Bites

I've been spending time on **nkosi** recently, fixing the agents report, making the action scan auto-resolve, cleaning up the per-section history so it keeps the last 30 entries instead of overwriting. That's a Grow quadrant play. The system is valuable and the tech is solid. The work is about keeping it that way.

Meanwhile, **compliance** sits in a different posture. It's high value and we need it, but the technical state requires attention. That's the Reengineer box. The work is harder, slower, and requires more stakeholder conversations. But the quadrant tells you not to look away.

The mistake I see most often is treating everything like it belongs in the same box. Every application gets the same investment model, the same staffing approach, the same urgency. That's how you end up starving your stars while over-investing in things that should be retired.

## The 30-Second Answer

Hewitt also has a pattern called the **30-Second Answer** that pairs well with this framework. When an executive asks about an application, you give them three bullet points and stop. No "it depends." No 10-minute tour of the architecture. Three declarative statements and then silence.

The quadrant gives you the structure for those three bullets. "This application is in the Reengineer box. It's high value to the business, but the technical debt is significant. We need a multi-year plan to modernize it, and I need your help protecting the investment from feature pressure."

That's it. The boss can drill down or move on. Either way, you've done your job.

## The Real Value

The quadrant framework isn't about getting the perfect score. It's about forcing the conversation. When you sit down with stakeholders and plot your portfolio together, you surface assumptions that were never stated aloud. You find the applications everyone assumed were strategic but are actually being tolerated. You find the ones everyone knows are broken but nobody wanted to name.

The APM itself does nothing. It gives you a current state assessment, and then it's up to you to bring those findings before other stakeholders and use them as the start of some crucial conversations.

That's the part that actually matters.
