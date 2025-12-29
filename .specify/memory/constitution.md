<!--
Sync Impact Report:
Version change: None (initial creation) → 0.1.0
Modified principles: None (all new)
Added sections: Project Vision
Removed sections: [SECTION_3_NAME] (no explicit content in user prompt)
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending (conceptual alignment for initial constitution)
- .specify/templates/spec-template.md: ⚠ pending (conceptual alignment for initial constitution)
- .specify/templates/tasks-template.md: ⚠ pending (conceptual alignment for initial constitution)
- .specify/templates/commands/*.md: ⚠ pending (conceptual alignment for initial constitution)
Follow-up TODOs: None
-->
# The Evolution of Todo Constitution

## Core Principles

### Spec-Driven Development Only
Every feature MUST originate from a written specification.
No implementation MAY occur without an approved spec.
Specs MUST be versioned and stored in `/specs/history`.

### Agentic Development Workflow
Follow this strict order: Specification → Plan generation → Task decomposition → Implementation via Claude Code.
No manual boilerplate code IS allowed.

### Clean Architecture & Code Quality
Clear separation of concerns.
Readable, testable, idiomatic Python.
Logical module boundaries.
Minimal complexity, maximum clarity.

### Phase Discipline
Phase I MUST remain: Console-based, In-memory only, Single-process, No persistence, No networking, No frameworks.
Future scalability SHOULD be considered but NOT implemented.

### Technology Constraints
Python 3.13+.
UV for environment management.
No external dependencies UNLESS explicitly justified in spec.
MUST run on a clean environment using documented steps.

### Functional Scope (Phase I)
The system MUST support exactly the following: Add Todo, Delete Todo, Update Todo, View Todos, Mark Todo as Complete.

### Observability of Process
Decisions MUST be explainable.
Specs, plans, and prompts ARE first-class artifacts.
The learning value of *how* the system was built IS as important as the code itself.

### Repository Structure Enforcement
The constitution MUST enforce: `/src` for application code, `/specs/history` for specifications, `CLAUDE.md` for Claude Code instructions, `README.md` for setup and usage, a constitution file at the root.

### AI Collaboration Rules
Claude Code IS treated as a co-developer.
Prompts, iterations, and refinements MUST align with this constitution.
No hallucinated features or scope creep.

## Project Vision

This project simulates the real-world evolution of software systems, starting from a minimal CLI-based in-memory todo application and gradually evolving into a distributed, cloud-native, AI-powered system.

In Phase I, the focus is on: Fundamental software architecture, Spec-driven development, Agentic workflows, Clean, maintainable Python code, Process transparency over manual coding.

Students act as **Product Architects**, not traditional programmers.

## Governance

This constitution supersedes all other project guidelines and documentation.
Amendments to this constitution MUST be proposed, documented, and approved by the Product Architect,
with a clear rationale for changes and an impact assessment on dependent artifacts.
All proposed changes to the project MUST be reviewed against the principles defined herein for compliance.

**Version**: 0.1.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29
