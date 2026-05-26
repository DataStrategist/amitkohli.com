---
title: AI-First Is Addictive (And Your Todo List Is Already Dead)
author: amit
date: 2026-03-13
slug: ai-first-todolist-is-dead
tags:
  - AI
  - Productivity
  - Workflow
  - Tools
topics:
  - AI Coding Assistants
  - Developer Experience
  - Workflow
draft: true
type: "[[Article]]"
topic: "[[AI Workflow]]"
---

There's a moment in the early stages of developing an AI-first workflow where something clicks. You stop writing things down "to do later" and you just... do them. Not because you've become some productivity monk. Because the cost of doing them NOW dropped to basically zero.

That's the drug. And I can't stop.

## The Old World: Todo Lists as Execution Proxies

Here's something I never really examined before: **todo lists exist because execution has friction**.

The reason you write "refactor the config module" on a sticky note instead of just doing it - that's friction. It takes a while, it might break things, you need to find the right files, understand the context, remember what you were trying to do. So you defer. You write it down instead. The note becomes a proxy for future-you having the time/energy/context to actually execute.

This is normal. This is how knowledge work has functioned for decades. You have a brain for ideation and tools for capture, and maybe 30% of what you capture actually gets executed. The rest sits in Todoist purgatory, slowly becoming irrelevant.

I have notebooks going back years. Physical ones. Full of ideas that took longer to find again than they would have taken to just implement.

## What Changed

I now live almost entirely in VS Code with GitHub Copilot. My Obsidian vault is AI-assisted. My meeting notes get processed by agents. My data scripts get written in conversation. And something weird happened to my relationship with todo lists.

They started feeling pointless.

Not because I got more disciplined. Because the moment I finished articulating what I wanted to do, I'd already done it.

Here's the actual experience:

> "I should add a date picker to this dashboard... actually, let me just describe that to Copilot."

And three minutes later, date picker exists. No ticket. No Trello card. No "add date picker" sticky note. The thought became a thing.

## The Prompt IS the Note

This is the mechanism and it's subtle: **writing a prompt takes the same effort as writing a todo**.

I mean this almost literally. The mental act of capturing "I need to do X" is nearly identical to the mental act of describing "please do X". Both require you to clarify what you actually want (harder than it sounds). Both require some specification. Both require you to spend 20-40 seconds writing something down.

The difference: one of them gets done immediately.

So the question becomes: why would you ever write the note?

For the first few months of working this way I kept doing it out of habit. "Write it down, do it later." Then I started noticing the graveyard of tasks I'd written down and could have just... executed. The todo list became a monument to friction that no longer existed.

## Near-Zero Tech Debt Execution

There's another thing happening here beyond just speed. It's not just that things get done faster - it's that they get done *cleaner*.

Old workflow:
- Have idea
- Write it down
- Come back to it later
- Have lost context
- Reconstruct what you meant
- Execute it in a hurry because you have other things
- Leave a bit of mess because "good enough"
- Repeat

AI-first workflow:
- Have idea
- Describe it while the context is hot
- Execute now, with full clarity
- The output is actually coherent because you gave it proper instructions while you still remembered why you cared

The tech debt accumulation drops dramatically. Not to zero - you still have to be thoughtful, you still make architectural choices that age badly. But the *casual* debt, the "I'll clean this up later", the "this is temporary" code that becomes permanent - that shrinks a lot when "later" becomes "now".

## The Addiction Loop

Here's why it's specifically addictive and not just "nice":

1. You articulate something you want
2. It exists within minutes
3. Your brain registers a small win
4. The cognitive reward pathway for "completing tasks" fires
5. You look around for the next thing to execute

This is the same loop as any productivity system, except the loop runs 10x faster. You get the dopamine hit of completion without the deferred gratification tax. And because the execution is immediate, you carry less mental load. No list of half-finished thoughts rattling around. No guilt about undone todos. Just: think it, say it, it exists.

I've started noticing when I'm ABOUT to write something down rather than just doing it, and asking myself: "could I describe this to an AI right now?" Usually yes. Usually I'm writing it down out of pure habit, not necessity.

## The Tasks That Survive

Some things still go on a list. Things involving:
- **Other people** - Can't execute a "have a conversation with X about Y" via AI agent (yet)
- **External dependencies** - Waiting on a response, a file, access to a system
- **Multi-day compounding** - Long projects with phases where context needs to survive across sessions
- **Physical world** - "Buy more coffee" is resolutely offline

But even some of these are shrinking. Meeting prep? Done immediately when I schedule the meeting. Follow-up actions? Processed the same day by an agent that reads my notes. Background research? "Researcher" agent handles it while I do something else.

The surviving todo list is genuinely lean in a way it never was before. Tasks that are on it are there because something external is blocking them, not because I haven't got around to them yet.

## OK But Does This Scale?

Look, I'm not going to pretend this is frictionless. Some caveats:

- **Context management is a skill** - The quality of what gets executed depends on how well you describe the task. Vague prompt, vague output. You still need to think.
- **Verification is still work** - You have to check that what was executed is actually correct. AI is confident and sometimes wrong.
- **Not everything is "describable"** - Creative and strategic work still requires the slow, foggy, exploratory process that can't be shortcut.

And honestly, sometimes the "write it down, think about it more, execute it properly" loop is *correct*. Not all friction is waste. Some friction is your brain telling you: this deserves more thought.

But for the large category of tasks that were on todo lists purely because of execution friction? Those are gone. And good riddance.

## The Actual Takeaway

If you're building an AI-first workflow and you still have a 47-item backlog of "things to do," check how many of those things you could just... describe right now.

Not because your AI assistant is magic. Because most of those tasks are fully specified in your head already. You know what you want. You wrote it down. The only thing stopping you was the cost of execution, and that cost just dropped through the floor.

The todo list isn't dead because we got more productive. It's dead because the thing that made it necessary - the gap between ideation and execution - is closing fast.

Watch this space. I'll be updating as the graveyard keeps shrinking.

---

*BLOG_VOICE_APPLIED | TECHNICAL_ACCESSIBLE | HONEST_LIMITATIONS*
