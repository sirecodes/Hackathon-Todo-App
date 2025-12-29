# Todo App - CLI Task Manager

A lightweight, in-memory command-line todo application built with Python 3.13+. Manage your tasks efficiently with a beautiful, color-coded terminal interface.

## Features

- ✅ Add, view, update, and delete todos
- ✅ Mark todos as complete
- ✅ Tab autocomplete for commands
- ✅ Color-coded output with ASCII art
- ✅ Zero external dependencies
- ✅ Fast and responsive CLI

## Requirements

- Python 3.13 or higher
- No external dependencies required

## Installation

### Option 1: Using UV (Recommended)

[UV](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

1. **Install UV** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd Hackathon-Todo-App
   ```

3. **Run with UV**:
   ```bash
   uv run src/app.py
   ```

UV will automatically handle Python version compatibility and run the application.

### Option 2: Standard Python

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd Hackathon-Todo-App
   ```

2. **Verify Python version**:
   ```bash
   python --version  # Should be 3.13+
   ```

3. **Run the application**:
   ```bash
   python src/app.py
   ```

## Usage

### Commands

Once the application is running, use these commands:

| Command    | Description                    |
|------------|--------------------------------|
| `add`      | Add a new todo                 |
| `view`     | View all todos                 |
| `update`   | Update an existing todo        |
| `delete`   | Delete a todo                  |
| `complete` | Mark a todo as complete        |
| `help`     | Show the command menu          |
| `exit`     | Exit the application           |

**Tip**: Use TAB to autocomplete commands!

### Example Workflow

```bash
# Start the app
python src/app.py

# Add a todo
Command: add
Enter todo description: Buy groceries

# View all todos
Command: view

# Mark as complete
Command: complete
Enter todo ID to mark complete: 1

# Exit
Command: exit
```

## Project Structure

```
Hackathon-Todo-App/
├── src/
│   ├── app.py           # Main CLI interface
│   └── todo_manager.py  # Todo data management
├── specs/               # Feature specifications
├── .specify/            # Development templates
└── README.md
```

## Technical Details

- **Storage**: In-memory (data is lost when app closes)
- **ID System**: Auto-incrementing integers
- **Status Types**: `pending` | `complete`
- **Python Version**: 3.13+
- **Dependencies**: None (uses only standard library)

## Development

This project follows Spec-Driven Development (SDD) principles. See the `specs/` directory for detailed specifications, plans, and task breakdowns.

### Documentation

- **Specification**: `specs/001-cli-todo-app/spec.md`
- **Implementation Plan**: `specs/001-cli-todo-app/plan.md`
- **Task Breakdown**: `specs/001-cli-todo-app/tasks.md`
- **Implementation Report**: `specs/001-cli-todo-app/implement.md`

## Limitations

- No data persistence (Phase I by design)
- Single-user only
- Terminal-based interface only
- Tab autocomplete may not work on all Windows terminals

## Future Enhancements (Phase II)

- File-based or database persistence
- Categories and tags
- Due dates and priorities
- Search and filter functionality
- Export to CSV/JSON

## License

[Your License Here]

## Contributing

Contributions are welcome! Please follow the Spec-Driven Development workflow outlined in `.specify/`.

---

**Version**: Phase I (In-Memory)  
**Status**: Production Ready  
**Last Updated**: 2025-12-29
