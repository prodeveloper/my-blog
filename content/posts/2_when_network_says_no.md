+++
title = 'When Network Says no'
date = 2025-08-21T13:27:52+01:00
draft = false
+++


I recently found myself in a troubleshooting session that taught me an important lesson about assumptions we make in our development workflows. What started as a simple "why won't this application start?" quickly became a deeper conversation about how we approach dependency management in enterprise environments.

## The Problem Unfolds

One of our engineers was struggling with a Spring Boot application that wouldn't start on an Azure VM. The error was frustratingly vague - just a "connection reset" message that gave us little to work with initially. But as we dug deeper, the real issue became clear.

"I think it's like a blocker for Internet," the engineer explained, pointing to the build logs. "All these libraries - Spring Framework, Spring Boot, Java-related dependencies - everything needs to download to our local machine before it can start working."

The application was trying to pull dependencies at runtime, but our Azure VM was sitting within a hardened subscription with restricted internet access. Only whitelisted URLs could be reached, and we didn't have access to the Maven repositories and dependency sources our application needed.

![alt text](https://storage.googleapis.com/blog-chenchatech-images/2_failed_connection.jpg)

## The Lightbulb Moment

This is where the real learning happened. My initial instinct was to think about network exceptions and whitelisting - the typical "ask IT to open up access" approach. But as we talked through the problem, a different solution emerged.

"What if we built this locally first?" I found myself asking. "Once we have all the dependencies pulled and we have something like a JAR file, then it stops being a problem, right?"

The engineer paused. "We haven't tried that approach before. We never had this kind of access issue."

And there it was - the assumption we'd been making without realizing it. We'd been designing our deployment process assuming internet access would always be available at runtime. We'd never questioned whether that was the best approach.

## Rethinking Our Build Strategy

This conversation shifted my thinking about how we approach builds and deployments, especially in enterprise environments. Here are the key insights:

**Runtime dependency resolution is a luxury, not a requirement.** Many of us have gotten comfortable with build tools that fetch dependencies on-demand. It's convenient during development, but it creates a hidden dependency on network access that may not always be available.

**Pre-built artifacts are more portable.** When you build everything locally (or in a build environment with internet access) and create a single deployable artifact, you eliminate the network dependency entirely. Your JAR file contains everything it needs to run.

**Infrastructure constraints drive better architectural decisions.** What initially felt like a frustrating limitation actually pushed us toward a more robust deployment strategy. Self-contained artifacts are generally more reliable and predictable than builds that depend on external resources at runtime.

## The Broader Lesson

This experience reminded me that as engineering managers, we need to regularly examine our assumptions about the environments our applications will run in. Network access, package repositories, even basic internet connectivity - these aren't guaranteed in every deployment scenario.

The solution wasn't to fight the infrastructure constraints or spend weeks getting security exceptions. It was to adapt our build process to work within those constraints. Sometimes the "limitation" points us toward a better approach we hadn't considered.

## Moving Forward

We're now implementing a build strategy that creates fully self-contained artifacts before deployment. It's actually made our deployment process more predictable and faster - no more waiting for dependency downloads during startup.

The next time you encounter what feels like an infrastructure roadblock, ask yourself: "What if this constraint is actually pushing us toward a better solution?" Sometimes the network saying "no" is exactly what you need to hear.