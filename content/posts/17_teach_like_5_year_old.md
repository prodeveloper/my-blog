+++
title = 'Want Better AI Results? Dumb Down Your Prompts'
date = 2026-02-23T13:28:22Z
draft = false
+++



"Explain this to me like I'm a smart five-year-old." Interesting advice — and it turns out, it's one of the most effective ways to improve your AI prompts.

When you use this technique, you end up with a prompt that not only *you* understand, but one that tends to give **much more predictable results**.

## The Problem With Powerful Models

Most of the time, the AI you're working with is a frontier model — something from Anthropic like an Opus model, or a reasoning model from OpenAI. Basically, something that is *really* powerful.

The fundamental problem? Because it's a reasoning model, it can make certain jumps in logic with the assumption that it understands what you're saying. **This is not always true.** And that's where the trouble starts  the model is essentially understanding the averages, filling in gaps based on probability rather than precision.

Humans figured this out about themselves a long time ago. There's a reason they say someone truly understands their stuff if they can explain it simply.

## The Technique

Here's what most people do: they tell the model, "Refine this prompt." The model will dutifully refine it  but based on the assumption that the model reading it is *also* smart. That's where things break down.

Instead, try this:

- **Tell the model to rewrite your prompt** so that a much, much simpler model would be able to understand and run it
- **Take that rewritten prompt** and tell the model to execute it

## A Quick Example

Say you're working on a coding project and you write this prompt:

> "Refactor the auth module to be more maintainable."

Sounds reasonable, right? But "more maintainable" is doing a lot of heavy lifting. The model will interpret that however it sees fit — maybe it splits files, maybe it adds comments, maybe it rewrites the whole thing.

Now, ask the model to rewrite that prompt so a much simpler model could follow it. You might get something like:

> **Task:** Split `auth.ts` into smaller files. Do not change how any function works.
>
> **Steps:**
> 1. Read `auth.ts`. Identify the 3 largest groups of related functions (e.g., login, tokens, sessions).
> 2. Create one new file for each group. Move only the functions that belong to that group. Keep the same function names and signatures.
> 3. In each new file, add the necessary imports at the top. Export every function that was public before.
> 4. Update `auth.ts` to re-export everything from the new files, so nothing breaks for existing callers.
> 5. Check: run the project's existing tests. If any test fails, look at the error, fix the import, and re-run. Repeat up to 3 times.
>
> **Done when:** All original tests pass and no function signatures have changed.

That's a *completely* different prompt. Every decision is spelled out — numbered steps, specific limits, a built-in feedback loop, and a clear definition of "done." There's no room for creative interpretation, which is exactly what you want.

## Why This Works

The prompt that comes out of this process is usually something you can actually read. It's made its assumptions **a lot more clear** — nothing is hidden behind implied logic or shorthand.

From there, you can hand-wrangle it to get the prompt exactly where you want it to be. The implicit becomes explicit, and you're back in control.

Give it a try. It's a small shift that makes a real difference.