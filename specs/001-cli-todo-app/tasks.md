# Tasks: In-Memory Python Console Todo App (Phase I)

**Branch**: `001-cli-todo-app` | **Date**: 2025-12-29 | **Plan**: specs/001-cli-todo-app/plan.md
**Input**: Implementation plan from `/specs/001-cli-todo-app/plan.md`

**Note**: This template is filled in by the `/sp.tasks` command. See `.specify/templates/commands/tasks.md` for the execution workflow.

## Summary

This document outlines the detailed tasks for implementing the In-Memory Python Console Todo App, Phase I, based on the approved implementation plan. The tasks are broken down into small, actionable steps covering project scaffolding, core data structures, CLI interaction, feature implementation (add, delete, update, view, mark complete), and basic error handling.

## Task Breakdown

### Phase 1: Setup

- [x] T001 Create `app.py` for the main application entry point.
- [x] T002 Create `todo_manager.py` to encapsulate todo item management.

### Phase 2: Core Todo Data Structure

- [x] T003 Define `TodoItem` class (or dictionary structure) in `todo_manager.py` with `id`, `description`, `status`.
- [x] T004 Implement in-memory collection for `TodoItem` objects in `todo_manager.py`.
- [x] T005 Implement `generate_unique_id` function in `todo_manager.py`.

### Phase 3: CLI Interaction Flow

- [x] T006 Implement main application loop in `app.py` to display menu and prompt for commands.
- [x] T007 Implement `parse_command` function in `app.py` to extract command and arguments.

### Phase 4: Implement Features

#### User Story: Add Todo

- [ ] T008 [US1] Implement `add_todo` function in `todo_manager.py` to create and store new todo items.
- [ ] T009 [US1] Integrate `add_todo` into `app.py` CLI flow, prompting for description.

#### User Story: View Todos

- [ ] T010 [US2] Implement `get_all_todos` function in `todo_manager.py` to return the list of todos.
- [ ] T011 [US2] Integrate `get_all_todos` into `app.py` CLI flow, displaying formatted todo list.

#### User Story: Update Todo

- [ ] T012 [US3] Implement `update_todo` function in `todo_manager.py` to modify a todo's description by ID.
- [ ] T013 [US3] Integrate `update_todo` into `app.py` CLI flow, prompting for ID and new description.

#### User Story: Delete Todo

- [ ] T014 [US4] Implement `delete_todo` function in `todo_manager.py` to remove a todo by ID.
- [ ] T015 [US4] Integrate `delete_todo` into `app.py` CLI flow, prompting for ID.

#### User Story: Mark Todo as Complete

- [ ] T016 [US5] Implement `mark_todo_complete` function in `todo_manager.py` to change a todo's status by ID.
- [ ] T017 [US5] Integrate `mark_todo_complete` into `app.py` CLI flow, prompting for ID.

### Phase 5: Basic Error Handling

- [ ] T018 Implement invalid command handling in `app.py` (e.g., "Command not recognized.").
- [ ] T019 Implement "Todo not found" error handling in `todo_manager.py` functions and integrate into `app.py`.
- [ ] T020 Implement basic input validation for `add`, `update`, `delete`, `complete` commands in `app.py`.

## Dependencies

- Phase 1 (Setup) must be completed before other phases.
- Phase 2 (Core Todo Data Structure) must be completed before feature implementation phases.
- Feature implementation phases (Add, View, Update, Delete, Mark Complete) can be tackled in any order after foundational phases.

## Parallel Execution Examples

- Once `app.py` and `todo_manager.py` are created (T001, T002), tasks within different feature user stories can be worked on in parallel (e.g., T008 and T010).
- Within a user story, the `todo_manager.py` implementation (e.g., T008) can be done in parallel with the `app.py` integration (e.g., T009) if carefully coordinated, though sequential is often safer for CLI applications.

## Implementation Strategy

The implementation will follow an MVP-first approach, focusing on delivering core functionality incrementally. It is recommended to implement the "Add Todo" and "View Todos" user stories first to establish a basic functional application, followed by "Update Todo", "Delete Todo", and "Mark Todo as Complete". Error handling will be integrated as features are implemented.

## Acceptance Criteria for All Tasks

- Each task results in functional, testable code.
- All code adheres to Python 3.13+ syntax.
- No external dependencies are introduced.
- All data is handled in-memory.
- The application remains console-based.

## Follow-ups and Risks

- **Follow-up**: Consider adding a persistent storage mechanism (e.g., file-based, simple database) in a future phase.
- **Follow-up**: Explore options for more robust input parsing (e.g., using `argparse`).
- **Risk**: Potential for `id` collisions if the unique ID generation is not sufficiently robust for long-term use (though less critical for in-memory). This will be mitigated by a simple incrementing integer ID for Phase I.

