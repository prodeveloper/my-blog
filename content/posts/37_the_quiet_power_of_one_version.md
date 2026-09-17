+++
title = 'The Quiet Power of One Version'
date = 2026-09-17T09:00:00+01:00
draft = true
+++

---

A rule Winters describes in the Software Engineering at Google material keeps coming back to me: **developers must never have a choice about which version of a component they depend on.** On its face it sounds restrictive. Remove choice from engineers and you are removing agency, right? But the more I run systems, the more I think he is pointing at something deeper. Removing the choice is not a restriction. It is the thing that lets the organization scale.

## Choice is the expensive part

For one developer, being told "you can't pick the version" feels like an arbitrary impediment. You have a strong opinion about the widget library and you want the newer one, today. That is a reasonable instinct at the scale of one person. The problem is that the choice does not stay local. Every time someone gets to decide, the organization ends up with two or three versions of the same thing in use at once. Now every upgrade, every security fix, every refactor has to touch multiple versions. The merge discussions, the diamond dependencies, the lost work. That is where the cost lives.

**Consistency is a choke point you can lean on.** When everyone depends on the same version, a fix applied once propagates everywhere. A security patch is one change, not a survey of who is on what. The single version becomes infrastructure you do not have to think about.

## No long-lived branches

The One Version rule has a quiet companion: keep your development branches short-lived, or better, work against trunk directly. Winters ties this to trunk-based development and the DORA research that keeps finding a predictive link between it and high-performing teams.

The reason is the same as the version choice. A long-lived branch is a version of the world that exists in parallel with the real one. The longer it lives, the more it drifts, and the more expensive it is to bring back together. That drift is the same "choice" problem wearing a different costume. Someone has to reconcile that branch with trunk, and the reconciliation is where time and effort go up in flames.

I run a handful of small repos rather than a monorepo, so the literal Google setup does not map one to one. But the principle does. **Keep changes small, keep them against the main line, and commit regularly.** Every pending item left sitting on a branch is work in progress, and work in progress is a debt that accrues interest.

## Monorepo is not the point

The interesting part of the chapter is Winters being honest that the monorepo is not the One True Way. A monorepo just happens to make One Version nearly effortless, because it is harder to violate the rule than to follow it. But fine-grained repositories, virtual monorepos, git submodules, all of these can give you the same outcome if you hold the principle.

**What matters is not how you store the code. It is that you adhere to One Version to the greatest extent possible.** The storage format is a detail, like choosing a filesystem. What you write to it matters more than the format itself.

## What this means for the way I work

Lately I have been thinking about my own automation and the repos I maintain as the same system Winters is describing. When my cron jobs and dashboards read from a single source of truth, I am applying One Version to my own operations. When a notification pipeline and a dashboard both read the same file, I never have to ask "which version of the truth am I looking at." The choice is gone, and the absence of that choice is what keeps the whole thing cheap to maintain.

The rule is worth borrowing even at a much smaller scale than Google. **Whenever you give people a choice, you are asking them to carry coordination cost. Whenever you remove one, you are buying consistency back.** Choose your battles.

Remember: your choice of VCS, or repo layout, matters far less than whether you have removed the version choice. The single source of truth is the point. Everything else is just a filesystem.
