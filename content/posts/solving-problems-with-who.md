+++
title = 'How to solve ambigous problems'
date = 2025-08-21T11:07:51+01:00
draft = false
+++


Picture this: You walk into a new organization, excited about the challenges ahead. Your first assignment? Supporting the gift card service that validates whether someone's gift card is legitimate before processing it. Simple enough, right?

Then reality hits. Day two of your new role, and suddenly the app stops working when pushed to production. Key metrics are showing issues across the board. You're staring at a broken system, and you have no idea what's happening.

This exact scenario played out for me recently, and it reminded me of a lesson I learned years ago during one of the most stressful days of my early career.

## When Obama Came to Kenya (And Nearly Broke Our Website)

Back when I was the only full-time developer at iHub (one of Kenya's premier tech incubators), President Obama announced a visit to Kenya. Overnight, our website traffic spiked 100x normal levels. The system immediately started throwing 500 errors.

I panicked. I threw every capacity solution I could think of at the problem. Maxed out servers, optimized databases, tried every trick in my playbook. Nothing worked.

So I did what any desperate developer would do: I bought a book on scaling software services and started reading. By 3 PM, after burning most of the day, I finally found a workaround. I created a static HTML copy of our homepage and served that instead of hitting the database directly.

It worked, but barely. And it taught me something crucial about how senior problems actually get solved.

## The Problem with Being Senior

Here's what I've learned about leadership: the higher you climb, the more ambiguous your problems become. By the time a problem reaches your desk, multiple people have already taken reasonable attempts at solving it. They've failed. Now it's your problem.

When that gift card service broke, I initially did what I always used to do. I researched. I read documentation. I even tried ChatGPT for faster answers. But here's the thing I realized: even AI isn't fast enough when you're dealing with truly complex, ambiguous problems.

The bottleneck isn't information access. It's human understanding.

![Diagram illustrating leadership challenges as an iceberg. The visible tip, labeled "Unsolved Problems," represents issues reaching leadership's desk. Below the surface are three hidden layers: "Previous Attempts" (orange, with the note "Multiple failed attempts to solve problem"), "Information Overload" (yellow, with the note "AI and research are not enough"), and "Lack of Understanding" (blue, with the note "Bottleneck is human comprehension of problem"). The diagram emphasizes the hidden complexity beneath leadership challenges.](https://storage.googleapis.com/blog-chenchatech-images/solving_problems_blog.png)

## The Conversation Hack

Then it hit me: the fastest way to solve an ambiguous problem isn't more research. It's finding the right person to talk to.

For the gift card issue, I went through my mental list of people in the organization. I thought about who might know something, anything, about this particular system. I found an engineer I'd built a relationship with and asked for a quick call.

But here's the key: I didn't call empty-handed.

## The Preparation Framework

Before that conversation, I did my homework:
- Read through the logs to understand what was happening
- Documented the current state versus the previous working state  
- Formed a working theory (even though I knew it was probably wrong)
- Gathered specific artifacts and error messages

When we talked, I shared my research upfront. I explained what I'd found, what I thought might be happening, and where I was stuck. The conversation lasted 30 minutes. I walked away with 80% of the solution.

## Where vs Why: The Better Question

Most people facing ambiguous problems ask "Why is this happening?" But when you don't understand the system, why questions lead nowhere fast.

Instead, ask "Where was this problem X days ago?"

Where was this issue yesterday? Last week? Last month? This approach gives you concrete data points to discuss. It moves you from abstract theorizing to specific investigation.

## The Network Effect

This experience crystallized something important: your problem-solving capability is directly proportional to your network size. The more people you can call, the more problems you can solve.

But networks require investment before you need them. You can't build relationships in crisis mode. The engineer who helped me with the gift card service? I'd already established rapport with him through casual conversations and previous collaborations.

## The Modern Twist

Sure, you could ask ChatGPT or search Google for basic answers. Use those tools for questions that have straightforward solutions. But for anything that could be answered with a simple search, you're probably wasting someone else's time.

Remember "Let Me Google That For You"? Don't be that person. Do your preliminary research first. Then leverage your network for the insights that only experience can provide.

## The Core Formula

Here's what I've learned about solving ambiguous problems:

**[Your Research] + [Expert's Knowledge] = [Rapid Problem Solving]**

The bigger your network, the more problems you can tackle. But the key is preparation. When you approach someone for help, come with:
- What you've already discovered
- Where you're stuck
- Specific artifacts they can examine
- A working theory (even if you suspect it's wrong)

This isn't just about being respectful of their time. It's about creating the conditions for breakthrough insights to emerge quickly.

The next time you face an ambiguous problem, resist the urge to research your way to a solution. Do enough homework to ask intelligent questions. Then find the right person and have the conversation that gets you 80% of the way there in 30 minutes.

Your network isn't just your net worth. It's your problem-solving superpower.