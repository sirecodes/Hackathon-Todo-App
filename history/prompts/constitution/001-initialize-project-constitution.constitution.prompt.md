---
id: 001
title: Initialize Project Constitution
stage: constitution
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-physical-ai-book
user: UNKNOWN
command: sp.constitution
labels: ["constitution", "initialization", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:

---

## Prompt

You are acting as the Constitution Architect for this project.

Project Name: The Evolution of Todo
Phase: I — In-Memory Python Console Application

Your task is to generate a PROJECT CONSTITUTION that will govern all future specifications, plans, tasks, and implementations for this repository.

### Project Vision
This project simulates the real-world evolution of software systems, starting from a minimal CLI-based in-memory todo application and gradually evolving into a distributed, cloud-native, AI-powered system.

In Phase I, the focus is on:
- Fundamental software architecture
- Spec-driven development
- Agentic workflows
- Clean, maintainable Python code
- Process transparency over manual coding

Students act as **Product Architects**, not traditional programmers.

### Core Principles (Must Be Enforced)
1. **Spec-Driven Development Only**
   - Every feature must originate from a written specification.
   - No implementation may occur without an approved spec.
   - Specs must be versioned and stored in `/specs/history`.

2. **Agentic Development Workflow**
   - Follow this strict order:
     1. Specification
     2. Plan generation
     3. Task decomposition
     4. Implementation via Claude Code
   - No manual boilerplate code is allowed.

3. **Clean Architecture & Code Quality**
   - Clear separation of concerns
   - Readable, testable, idiomatic Python
   - Logical module boundaries
   - Minimal complexity, maximum clarity

4. **Phase Discipline**
   - Phase I must remain:
     - Console-based
     - In-memory only
     - Single-process
     - No persistence
     - No networking
     - No frameworks
   - Future scalability should be considered but NOT implemented.

5. **Technology Constraints**
   - Python 3.13+
   - UV for environment management
   - No external dependencies unless explicitly justified in spec
   - Must run on a clean environment using documented steps

6. **Functional Scope (Phase I)**
   The system MUST support exactly the following:
   - Add Todo
   - Delete Todo
   - Update Todo
   - View Todos
   - Mark Todo as Complete

7. **Observability of Process**
   - Decisions must be explainable
   - Specs, plans, and prompts are first-class artifacts
   - The learning value of *how* the system was built is as important as the code itself

8. **Repository Structure Enforcement**
   The constitution must enforce:
   - `/src` for application code
   - `/specs/history` for specifications
   - `CLAUDE.md` for Claude Code instructions
   - `README.md` for setup and usage
   - A constitution file at the root

9. **AI Collaboration Rules**
   - Claude Code is treated as a co-developer
   - Prompts, iterations, and refinements must align with this constitution
   - No hallucinated features or scope creep

### Output Requirements
- Produce a formal **PROJECT CONSTITUTION**
- Use clear sections and enforceable rules
- Write in authoritative but instructional tone
- This constitution should remain valid for all future phases unless explicitly amended

Generate only the constitution. Do not generate sp

## Response snapshot

The project constitution for "The Evolution of Todo, Phase I — In-Memory Python Console Application" has been generated and written to `.specify/memory/constitution.md`. It outlines 9 core principles, defines the project vision, and establishes governance rules. The constitution is versioned as `0.1.0`, ratified and last amended on 2025-12-29. Follow-up is needed to ensure alignment with existing templates.

## Outcome

- ✅ Impact: Project constitution initialized.
- 🧪 Tests: None
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: Continue with spec-driven development.
- 🧠 Reflection: The constitution was successfully created based on user input, defining the foundational principles for the project.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): None
- Prompt variant (if applicable): Initial constitution generation
- Next experiment (smallest change to try): Automate template alignment checks.
