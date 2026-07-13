---
title: I Built a Knowledge Graph of Comedy (And Found Some Uncomfortable Families)
author: amit
date: 2026-05-26
slug: comedy-knowledge-graph
tags:
  - data
  - comedy
  - knowledge-graphs
  - d3
  - visualization
  - NLP
topics:
  - Data Science
  - Network Analysis
  - Visualization
draft: true
type: "[[Project]]"
topic: "[[Knowledge Graphs]]"
---

<!-- SKELETON — very rough, fill in later -->
<!-- Full project plan: c:\o\boom\Stuff\Comedy Knowledge Graph Blog - Project Plan.md -->
<!-- Tech: yt-dlp + Ollama (llama3.1:8b) + networkx + Louvain + Scrollama.js + D3.js -->

## The Question Nobody Asked But I'm Going To Answer Anyway

<!-- Hook: comedy is studied academically, but nobody's measured its *shape* -->
<!-- Incongruity theory, Benign Violation, the three classic structures -->
<!-- What if we could actually map it? -->

## What Even Is A Joke (Structurally)

<!-- SETUP / PUNCHLINE / TAG / NON-JOKE — the four structural types -->
<!-- Example from a real transcript -->
<!-- Why this matters: setup density ≠ punchline density across comedians -->

## 50 Comedians, 50 Hours of Transcripts

<!-- The roster: American Classic, American Modern, British, Irish/Scottish/Australian -->
<!-- yt-dlp auto-captions; why transcripts beat asking an LLM what it thinks -->
<!-- The Robin Williams problem (non-linear delivery) — acknowledged, not solved -->

## What The LLM Actually Did (Two Jobs, Not One)

<!-- Task 1: structural segmentation — SETUP/PUNCHLINE/TAG/NON-JOKE -->
<!-- Task 2: multi-label topic classification — 18 topics (+ Meta/Self-referential TBD) -->
<!-- Why local Ollama, why two separate prompts, why not one big ask -->

## The Metrics: How Do You Actually Measure A Set

<!-- Setup density, punchline density, average punchline lag, tag rate -->
<!-- Topic diversity (entropy), dominant topic share -->
<!-- One table showing surprising outliers -->

## From Vectors To A Network

<!-- Topic vectors → cosine similarity → weighted graph -->
<!-- Why force-directed layout, what the edges mean -->
<!-- [Network graphic placeholder] -->

## The Comedy Families

<!-- Louvain community detection: the clusters that emerged -->
<!-- Named families (provisional): the subversives, the crowd workers, the observationalists, etc. -->
<!-- Era coloring: are the clusters era-based or style-based? -->

## What Actually Changed Over Time

<!-- Temporal line chart: topic % by decade -->
<!-- Did "observational" comedy peak and fall? Did self-referential rise? -->

## The Finding I Didn't Expect

<!-- The main surprising cluster / outlier / overlap -->
<!-- What this says about the shape of comedy -->

## This Is Obviously Not Science

<!-- Transcript quality varies, one special != career, threshold choices matter -->
<!-- But the patterns are real enough to be interesting -->

## Okay But So What

<!-- The broader point: you can measure creative structure -->
<!-- Same approach works for music, film, architecture — anything with grammar -->
<!-- Pointer to code/data repo (TBD) -->
