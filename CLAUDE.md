# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## What this repository is

This is a **curriculum / course-content repository**, not a software project. It holds the teaching
materials Alexander Booth (the Head Program Instructor) uses to run cohorts of **Implementing Agentic
AI: Building Your Organizational Playbook**, an MIT Sloan Executive Education / MIT Schwarzman College
of Computing program delivered with GetSmarter. There is no build, lint, test, or CI. "Doing work" here
means one of:

- Writing or refining a `Module_NN/README.md` summary for a module.
- Standing up a new cohort folder (extracting downloads, organizing them into the standard layout).
- Writing a `Live_Session/README.md` once a cohort's live session has actually happened.

## Directory taxonomy

```
MIT-AGAI-<START_DATE>/             cohort, e.g. MIT-AGAI-2026-07-20
  README.md                        cohort overview (module map, live-session status)
  Module_00/                       Orientation
  Module_01/                       Module 1: Understanding Agentic AI
  Module_02/                       Module 2: Designing and Deploying Agentic Systems
  Module_03/                       Module 3: Scaling Agentic AI Responsibly
    README.md                      authored module summary (the main maintained artifact)
    Downloads/                     lesson/media/podcast transcript PDFs and supporting readings
  Live_Session/                    live-session slides (PPTX + PDF) and recap README
```

- The program is fixed: an orientation module plus three content modules (explore, implement, scale).
  Every cohort runs the same underlying lesson content, so **module READMEs can usually be reused across
  cohorts almost verbatim**, with only the `**Date:**` and `**Cohort:**` header lines changed to match
  that cohort's actual delivery dates. Check the file timestamps in `Downloads/` (or the cohort's known
  schedule) to figure out the right month for each module's header.
- `Live_Session/README.md` only gets written once that cohort's live session has actually happened. Until
  then, leave the folder as a placeholder (it may just hold a `.gitkeep`).
- New cohorts sometimes arrive as a pile of zip files (`Module N Downloads-*.zip`,
  `Orientation module Downloads-*.zip`) plus loose webinar files at the folder root instead of the
  `Module_NN/Downloads/` + `Live_Session/` layout above. Extract and reorganize into the standard layout,
  then delete the zips.

## The module README is the primary authored artifact

Each `Module_NN/README.md` is a summary of that module's actual lesson, media-set, and podcast content,
**synthesized from the transcripts in `Downloads/`**, not invented. When asked to create or update one:

1. Read every PDF in `Module_NN/Downloads/` directly (the Read tool handles PDFs natively; they're
   normally short, 2-6 page transcripts, except the occasional standalone academic reading, which can run
   longer).
2. Use the existing module READMEs (any cohort) as the template: a header block (`**Author:** Alexander
   Booth`, `**Date:**`, `**Cohort:**`), then `## Overview`, `## Why This Module Matters`, `## What This
   Module Covers` (numbered concept sections), `## Units and Materials` (per-unit breakdown citing
   transcript filenames), `## Supporting Materials` (for standalone readings, if any), `## Key
   Takeaways`.
3. If a PDF won't extract to readable text, say so rather than fabricating its contents.

Since a module's content is shared across cohorts, once one cohort's module README is written well, copy
it to the sibling cohort and only touch the header dates rather than re-deriving it from scratch.

## Voice and tone

This repo is student-facing. Keep that in mind:

- **No meta-commentary about how the repo itself was organized.** Don't write things like "these files
  were originally zipped and have been extracted" or reference how content got reorganized. That's
  process trivia for whoever's doing the file management, not something a student or instructor needs to
  read in a course README.
- **Don't reference other repos** (e.g. the sibling `ibm_data_science` repo) in this repo's content. Each
  repo should read as self-contained.
- **Write like a person, not like an AI.** Avoid em dashes; use commas, periods, colons, or parentheses
  instead. Avoid the reflexive "not X, but Y" contrast construction when it's not doing real work. Match
  the plainspoken, direct register of the actual course material (see the transcripts) rather than
  defaulting to dense, hedge-everything academic prose.

## Git conventions

No established commit-message convention yet (this repo is new). Keep messages short and tied to
teaching milestones rather than code changes, similar to the sibling `ibm_data_science` repo's style
(e.g. `M1 launch`, `live session content`) unless Alexander says otherwise.
