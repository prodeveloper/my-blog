+++
title = 'How I Recovered 66GB on My Laptop Using Claude'
date = 2026-03-08T14:38:31Z
draft = false
+++


My laptop was running out of space. I had 5GB left on a 228GB drive and I had no idea why.

I knew the usual suspects (too many apps, too many downloads), but the numbers never added up when I tried to investigate on my own. So I decided to let Claude do the detective work.

What followed was one of the most satisfying cleanup sessions I've had in years.

---

## Starting with the obvious question

I asked Claude a simple question: *why is my laptop full?*

Within seconds it ran a scan and gave me a breakdown I'd never seen before. Not just "your Downloads folder is big": a full picture of where every gigabyte was hiding.

The top offenders:

- **Docker**: 29GB sitting in a container VM that I hadn't touched in months
- **Microsoft Office** (Outlook, OneNote, Teams, OneDrive): 19GB, from a company I no longer work for
- **Google Drive & Chrome app support**: 8.8GB
- **Descript**: 2.7GB
- **App caches**: 5.3GB

Seeing it laid out like that was clarifying. It wasn't one thing eating my disk. It was a graveyard of old tools I'd never thought to clean up.

---

## The old company problem

The Microsoft Office discovery was a small shock. I don't have a OneDrive account, or so I thought. Turns out when you install Office for a company, it leaves behind gigabytes of data long after you've moved on.

We removed everything: Outlook, OneNote, Teams, OneDrive, and all their associated data. One command at a time, 20GB gone.

It's a good reminder: when you leave a job, clean your machine.

---

## Apps I hadn't opened in years

This was the most interesting part. Claude pulled the last-opened date for every app on my machine by querying macOS metadata. The results were humbling.

Firefox: last opened in **2021**.
Postman: **2021**.
DataGrip, Anki, DBeaver, Warp, Cisco Webex: all **2022**.
Slack, Logseq, Cursor, Kreya: somewhere in **2024**.

None of these sparked any urgency in me when I saw the list. I kept calibre, SimpleMind, and Chrome. Everything else went.

That's the thing about storage. Apps don't announce when they've become dead weight. They just sit there, quietly taking up space, waiting for a day that never comes.

---

## The hidden costs of developer tools

If you're a developer, your machine has a second layer of bloat that most cleanup guides ignore.

- **Docker's VM disk** had ballooned to 29GB even after I'd long stopped using those containers. `docker system prune -a` cleared 5GB of images. Shrinking the VM disk in Docker Desktop settings recovered the rest.
- **VS Code extensions** (specifically old versions of Claude Code) had accumulated 14 copies of the same extension, totalling over 2GB.
- **npm cache**: 2.3GB of packages I'd never need again.
- **Whisper model cache**: 2GB for an AI transcription model I'd tested once.

These don't show up in typical disk usage tools because they're buried deep in hidden folders. But they add up fast.

---

## The result

We started at **5GB free**. After a few hours of methodical cleanup:

**73GB free.**

That's 68GB recovered. More than a quarter of my total disk, without deleting a single file I actually needed.

---

## What I'd do differently going forward

A few habits I'm taking away from this:

**When you leave a job, uninstall their software.** Office, VPNs, collaboration tools. All of it. Don't let the digital residue of old roles pile up on your machine.

**Check last-opened dates once a year.** macOS tracks this. If you haven't opened something in six months, you probably don't need it.

**Developer caches need manual attention.** Docker, npm, pip, Homebrew. None of these clean themselves up. Add `brew cleanup` and `docker system prune` to your routine.

**The stuff you don't see costs the most.** The Downloads folder is obvious. The 14 copies of an extension you auto-updated, the Whisper model you tested once, the VM disk from a side project. That's where the real waste hides.

---

The whole experience took a few hours and felt like clearing out a room you'd been ignoring for three years. Highly recommend.
