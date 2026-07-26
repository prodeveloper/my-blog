+++
title = 'I Just Wanted to Check My Gmail from the Terminal'
date = 2026-03-10T17:52:03Z
draft = false
+++

It started with a simple idea: use Claude to check my Gmail without opening a browser.

I found a CLI tool called `gws`, the Google Workspace CLI. It promised to let you query Drive, Gmail, Calendar, Sheets, all from the terminal. Perfect. I installed it, set up OAuth credentials in Google Cloud Console, and ran `gws auth login`.

And immediately hit a wall.

---

## The first error: invalid_client

```
OAuth flow failed: Server error: invalid_client: Unauthorized
```

`invalid_client` is Google's way of saying: I don't recognise these credentials at all. Not a permissions issue. Not a scope issue. The credentials themselves were wrong.

I had a `client_secret.json` file in the right place. I checked the client ID — correct. I checked the secret. Also correct, I thought.

Turns out `gws` stores its own copy of your credentials at `~/.config/gws/client_secret.json`. And somewhere along the way, that file had the client ID pasted into the `client_secret` field. Both fields had the same value. The same long string. Completely wrong.

One file copy later, the login succeeded.

---

## The second error: a machine that doesn't exist

```
Authentication failed: Failed to decrypt credentials: Decryption failed.
Credentials may have been created on a different machine.
```

I had just logged in. On this machine. Thirty seconds ago.

What was happening: `gws` encrypts your OAuth token after login using your OS Keyring (macOS Keychain on a Mac). When Claude runs a terminal command in a subprocess, it has no access to the Keychain. So every time Claude called `gws`, it tried to generate a new decryption key from scratch, failed, and gave up.

The login worked fine in my interactive terminal. Every command Claude ran in the background failed.

I tried a lot of things:
- `gws auth logout` and back in again — same error
- A separate profile directory via `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` — same error
- Creating a `.encryption_key` file before login so `gws` would use that instead — the file disappeared after login
- Extracting the key from the macOS Keychain via `security find-generic-password` — the key wasn't there

I even read the strings out of the compiled binary to understand what encryption library it was using. (`keyring-rs` v3, for the curious.)

Nothing worked.

---

## The fix: bypass the encryption entirely

`gws` has two credential modes: encrypted (`credentials.enc`) and plain (`credentials.json`). If the plain file exists, it uses that, with no Keychain needed.

So I wrote a small Python script to do the OAuth flow myself and save the token directly to `~/.config/gws/credentials.json` in the right format. No `gws` involved in the auth step at all.

It hit one more snag — macOS Python 3.13 doesn't ship with SSL certificates by default, so the token exchange request failed. Fixed by pointing it at the Homebrew OpenSSL cert bundle.

Then I deleted `credentials.enc` so `gws` would stop trying to decrypt it.

And it worked.

---

## The result

```bash
gws gmail users messages list \
  --params '{"userId": "me", "q": "invoice newer_than:7d"}'
```

Six emails. All there, all readable, straight from the terminal.

Total time: about two hours. For what should have been a five-minute setup.

---

## What I took away

**The Keychain is an interactive-only resource.** Any tool that encrypts credentials using the OS Keyring will fail silently in non-interactive contexts — background jobs, subprocesses, CI pipelines. If you're building something that needs to run unattended, use file-based secrets.

**"Created on a different machine" usually means "no Keychain access."** The error message implies your token is stale. It isn't. The decryption key just isn't available in that context.

**Read the binary if you have to.** When the docs don't explain the encryption mechanism, `strings` on the compiled binary at least tells you what library is being used and what Keychain service name to search for.

**Plain credentials beat encrypted ones when automation is involved.** The extra security of Keychain encryption isn't worth much if it breaks every automated workflow. Know how to opt out.

I did eventually check my email. The thing I was looking for was there.

Two hours for that. But now it works from anywhere.

This isn't the final answer though. Plain credentials are a workaround, not a fix. The encrypted flow is what `gws` is designed for, and it's clearly working — the login succeeds, the token is saved. Something in the Keychain handshake is just not translating across contexts. That's the next thing to figure out: why the key isn't where `gws` expects it, and whether there's a way to make the encrypted path work for subprocesses too.

When that's solved, I'll update this post.

