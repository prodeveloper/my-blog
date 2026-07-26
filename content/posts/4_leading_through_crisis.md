+++
title = 'When Everything Goes Wrong: Leading Through a Critical System Recovery'
date = 2025-08-22T12:52:57+01:00
draft = false
+++


As a software engineering manager, I've faced my share of technical challenges, but nothing quite prepared me for the week when our core loyalty points administration system went completely dark.

## The Perfect Storm

LPA The system that orchestrates this entire operation, let's call it our loyalty platform, had lost connectivity to essential services. We were looking at a potential customer impact that could affect our entire quarterly cycle.

The technical details were complex: our replica server in the cloud couldn't communicate with the master server on-premises, authentication services were down, and network connectivity had been severed due to recent security changes. On top of all of this we are working with a strained organization just from hardening exercises.

## The Most Important Lesson: Aggressive Prioritization Saves the Day

![leading through crisis](https://storage.googleapis.com/blog-chenchatech-images/4_blog_leading_through_crisis.jpg)

Here's what I learned that I wish every engineering manager knew: **When facing a true crisis, you must be ruthlessly aggressive about prioritization, even when it feels uncomfortable.**

The moment we understood the severity of the situation, we made a decision that felt radical at the time. We completely paused all other work—including a high-visibility travel rewards project that had executive attention and redirected our entire engineering capacity to the recovery effort. Every network engineer, every infrastructure specialist, every architect within our portfolio was pulled into this single focus.

This wasn't a popular decision initially. The engineer working on the travel project questioned whether this was really necessary. Other stakeholders wondered if we were overreacting. But I realized that half-measures in a crisis are often worse than no measures at all.

## The Ripple Effect of Decisive Action

What happened next validated this approach completely. Because we had everyone focused on the same problem:

- Our network team could immediately drop into emergency change processes (ECAB)
- Infrastructure specialists could work in parallel rather than sequence
- We could compress a typically week long design and approval process into hours
- Most importantly, everyone understood this was the top priority no competing demands

The engineer initially expressed frustration about pausing other work, but once they understood the broader context and saw the entire organization mobilizing, they became one of our most effective contributors to the solution.

## Technical and Organizational Alignment

The technical solution required multiple teams to coordinate perfectly: network firewall rules needed updating, security protocols had to be fast-tracked, and infrastructure changes required emergency approvals. Without complete organizational alignment, this would have been impossible.

We scheduled back-to-back review sessions, compressed our design approval process, and even arranged emergency architecture reviews. The phrase "we need to get this over the line" became our rallying cry. Everyone from offshore teams to senior network architects understood that normal processes were temporarily suspended.

## The Human Element

One of the most striking aspects was watching how the team responded once they understood the stakes. The same engineer who initially questioned the priority shift became incredibly proactive, staying late to ensure network configurations were ready for morning reviews. Our offshore colleagues adjusted their schedules to support real-time collaboration. 

People rise to meet clear expectations, but only if leadership provides that clarity decisively.

## Lessons for Engineering Managers

1. **Don't hedge your bets in a real crisis.** Go all-in or don't go in at all. Half the team working on a critical issue while the other half continues normal work often means neither effort succeeds.

2. **Communicate the 'why' relentlessly.** People need to understand not just what you're asking them to do, but why it matters more than everything else.

3. **Compress feedback loops.** We moved from daily check-ins to twice-daily syncs, scheduled design reviews within hours instead of days, and created emergency approval processes.

4. **Accept that some people will initially resist.** Not everyone will immediately understand why you're making dramatic changes. That's okay—clear communication and visible commitment from leadership eventually brings everyone along.

5. **Use the crisis to build trust.** When your team sees you making hard decisions and taking ownership of outcomes, it strengthens your relationship for future challenges.

## The Outcome

We restored full service connectivity within 48 hours—a timeline that would normally take weeks through standard processes. More importantly, the team came out of this experience with increased confidence in our ability to handle crises and clearer understanding of how to mobilize when it truly matters.

The travel rewards project resumed once the crisis was resolved, and ironically, the focused sprint mentality we developed during the crisis made us more effective when we returned to normal work.

## Final Thoughts

Not every problem requires this level of response. But when you're facing a true crisis that threatens core business operations, the biggest mistake is treating it like a normal problem with normal processes. Sometimes being a good engineering manager means making decisions that feel extreme in the moment but are exactly what the situation demands.

The key is knowing the difference between a crisis that requires this response and a problem that just feels urgent. But when you're truly in crisis mode, decisive action and complete team alignment aren't just helpful—they're the only path forward.