+++
title = 'Stop Asking People for Numbers They Never See'
date = 2026-11-03T09:00:00Z
draft = true
+++

I've been reading the compute chapter of *Software Engineering at Google*, and one line has stuck with me. When early schedulers asked engineers to declare how much CPU and memory their programs needed, the authors call the idea flawed because **these are not numbers that humans interact with daily**.

That sentence explains a lot of waste I see outside of data centres.

## The form that asks the wrong person

Picture a shared kitchen in an office. Every team has to book fridge shelves at the start of the year. Nobody knows how much food they'll bring in March, so everyone books for their busiest week and adds a bit for safety. By spring the fridge is "full" and half empty at the same time.

Nobody in that story is careless. They were asked to guess a number they never look at, and **when people guess, they guess high, because running short hurts them and over-asking hurts someone else.**

Google saw the same pattern with machines. Engineers padded their resource requests, then the padding outlived the reason for it. The configuration itself became a source of inefficiency.

## Measure instead of ask

The fix in the book is simple to state: let the system watch what a program uses and adjust the reservation for it. Humans set intent ("this must stay fast"), and the machine handles the arithmetic.

I've started applying this to my own work in small ways:

- **Thresholds come from history, not opinion.** When I set an alert or a quality gate, I look at what the last few months looked like before choosing a line. A number pulled from the air will either fire constantly or never.
- **Reservations get reviewed against use.** Anything booked in advance, from licences to meeting rooms to cloud capacity, gets a quick check: what did we use versus what did we hold?
- **Ask people about outcomes, not quantities.** "How quickly must this respond?" is a question a person can answer. "How many cores?" usually isn't.

## Broken things should step aside on their own

The same section describes machines that report their own bad health, get pulled out of rotation, try a reboot, and only then call a human. Work running on them simply restarts elsewhere.

**The lesson isn't about machines. It's that the first response to a known failure should be boring and automatic, and a person should only be pulled in when the boring fix didn't work.** Every recurring job I run now has that shape: retry, fall back, and only then tell me.

## Neighbours who share a room

There's a lovely heading in the chapter: "My neighbor's dog barks in my RAM." When programs share a machine, one greedy tenant hurts everyone around it. The answer was isolation, so that each tenant gets a guaranteed space and a hard limit.

Teams work like this too. A shared backlog with no limits lets the loudest request crowd out everything else. Clear boundaries feel restrictive, but they're what let several groups share one resource without fighting over it.

## Remember

- If a number isn't something a person sees every day, don't make them guess it. Measure it.
- Padding is the rational response to being asked the wrong question.
- Automate the boring first fix; escalate only what it can't solve.
- Shared resources need limits, or the noisiest tenant wins.
