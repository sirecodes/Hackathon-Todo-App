"""
In-Memory Python Console Todo App
Main application entry point with CLI interaction.
"""
try:
    import readline  # Linux / macOS
except ImportError:
    import pyreadline3 as readline  # Windows

from todo_manager import TodoManager


# ANSI Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    DIM = '\033[2m'


# Command autocomplete setup
class CommandCompleter:
    def __init__(self, options):
        self.options = sorted(options)
    
    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options if s.startswith(text.lower())]
            else:
                self.matches = self.options[:]
        
        try:
            return self.matches[state]
        except IndexError:
            return None


def setup_autocomplete():
    """Setup tab completion for commands."""
    commands = ['add', 'view', 'update', 'delete', 'complete', 'exit', 'help']
    completer = CommandCompleter(commands)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')


def print_banner():
    """Print the application banner."""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ████████╗ ██████╗ ██████╗  ██████╗     █████╗ ██████╗ ██████╗  ║
║  ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗   ██╔══██╗██╔══██╗██╔══██╗ ║
║     ██║   ██║   ██║██║  ██║██║   ██║   ███████║██████╔╝██████╔╝ ║
║     ██║   ██║   ██║██║  ██║██║   ██║   ██╔══██║██╔═══╝ ██╔═══╝  ║
║     ██║   ╚██████╔╝██████╔╝╚██████╔╝   ██║  ██║██║     ██║      ║
║     ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝  ╚═╝╚═╝     ╚═╝      ║
║                                                              ║
║              {Colors.YELLOW}✨ Your Ultimate Task Manager ✨{Colors.CYAN}               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}"""
    print(banner)


def display_menu():
    """Display the main menu options."""
    menu = f"""
{Colors.BLUE}┌────────────────────────────────────────────────────────────┐
│                      {Colors.BOLD}MAIN MENU{Colors.END}{Colors.BLUE}                          │
├────────────────────────────────────────────────────────────┤{Colors.END}
{Colors.GREEN}│  {Colors.BOLD}add{Colors.END}       {Colors.DIM}→{Colors.END}  Add a new todo item                        {Colors.BLUE}│{Colors.END}
{Colors.GREEN}│  {Colors.BOLD}view{Colors.END}      {Colors.DIM}→{Colors.END}  View all your todos                        {Colors.BLUE}│{Colors.END}
{Colors.GREEN}│  {Colors.BOLD}update{Colors.END}    {Colors.DIM}→{Colors.END}  Update an existing todo                    {Colors.BLUE}│{Colors.END}
{Colors.GREEN}│  {Colors.BOLD}delete{Colors.END}    {Colors.DIM}→{Colors.END}  Delete a todo                              {Colors.BLUE}│{Colors.END}
{Colors.GREEN}│  {Colors.BOLD}complete{Colors.END}  {Colors.DIM}→{Colors.END}  Mark a todo as complete                    {Colors.BLUE}│{Colors.END}
{Colors.GREEN}│  {Colors.BOLD}help{Colors.END}      {Colors.DIM}→{Colors.END}  Show this menu                             {Colors.BLUE}│{Colors.END}
{Colors.YELLOW}│  {Colors.BOLD}exit{Colors.END}      {Colors.DIM}→{Colors.END}  Exit the application                       {Colors.BLUE}│{Colors.END}
{Colors.BLUE}└────────────────────────────────────────────────────────────┘{Colors.END}
{Colors.DIM}💡 Tip: Use TAB to autocomplete commands{Colors.END}
"""
    print(menu)


def parse_command(user_input):
    """
    Parse user input to extract command and arguments.
    
    Args:
        user_input (str): Raw user input
        
    Returns:
        tuple: (command, args_list)
    """
    parts = user_input.strip().split(maxsplit=1)
    if not parts:
        return None, []
    
    command = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return command, args


def display_todos(todos):
    """
    Display todos in a formatted list.
    
    Args:
        todos (list): List of TodoItem objects
    """
    if not todos:
        print(f"\n{Colors.YELLOW}┌────────────────────────────────────────────────────────────┐")
        print(f"│  📭 No todos found. Your list is empty!                   │")
        print(f"│     {Colors.DIM}Use 'add' to create your first todo{Colors.END}{Colors.YELLOW}                     │")
        print(f"└────────────────────────────────────────────────────────────┘{Colors.END}\n")
        return
    
    print(f"\n{Colors.CYAN}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗")
    print(f"║                      YOUR TODOS                            ║")
    print(f"╚════════════════════════════════════════════════════════════╝{Colors.END}\n")
    
    for i, todo in enumerate(todos, 1):
        if todo.status == "complete":
            status_symbol = f"{Colors.GREEN}✓{Colors.END}"
            status_text = f"{Colors.GREEN}COMPLETE{Colors.END}"
            box_color = Colors.DIM
        else:
            status_symbol = f"{Colors.YELLOW}○{Colors.END}"
            status_text = f"{Colors.YELLOW}PENDING{Colors.END}"
            box_color = Colors.BLUE
        
        print(f"{box_color}┌─ Todo #{i} ───────────────────────────────────────────────┐{Colors.END}")
        print(f"{box_color}│{Colors.END} {status_symbol}  {Colors.BOLD}ID:{Colors.END} {todo.id}")
        print(f"{box_color}│{Colors.END} {Colors.BOLD}Task:{Colors.END} {todo.description}")
        print(f"{box_color}│{Colors.END} {Colors.BOLD}Status:{Colors.END} {status_text}")
        print(f"{box_color}└────────────────────────────────────────────────────────────┘{Colors.END}\n")
    
    print(f"{Colors.CYAN}{'─' * 62}{Colors.END}")
    print(f"{Colors.BOLD}Total: {len(todos)} todo(s){Colors.END} | {Colors.GREEN}Complete: {sum(1 for t in todos if t.status == 'complete')}{Colors.END} | {Colors.YELLOW}Pending: {sum(1 for t in todos if t.status == 'pending')}{Colors.END}")
    print(f"{Colors.CYAN}{'─' * 62}{Colors.END}\n")


def handle_add_todo(manager):
    """Handle the add todo command."""
    print(f"\n{Colors.CYAN}┌────────────────────────────────────────────────────────────┐")
    print(f"│  ➕  Add New Todo                                          │")
    print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")
    description = input(f"{Colors.BOLD}Enter todo description:{Colors.END} ").strip()
    
    if not description:
        print(f"{Colors.RED}✗ Error: Description cannot be empty!{Colors.END}")
        return
    
    try:
        todo = manager.add_todo(description)
        print(f"\n{Colors.GREEN}┌────────────────────────────────────────────────────────────┐")
        print(f"│  ✓ Todo added successfully!                               │")
        print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")
        print(f"{Colors.DIM}ID: {todo.id} | Description: {todo.description}{Colors.END}\n")
    except ValueError as e:
        print(f"{Colors.RED}✗ Error: {e}{Colors.END}")


def handle_view_todos(manager):
    """Handle the view todos command."""
    todos = manager.get_all_todos()
    display_todos(todos)


def handle_update_todo(manager):
    """Handle the update todo command."""
    print(f"\n{Colors.CYAN}┌────────────────────────────────────────────────────────────┐")
    print(f"│  ✏️  Update Todo                                            │")
    print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")
    
    try:
        todo_id = input(f"{Colors.BOLD}Enter todo ID to update:{Colors.END} ").strip()
        if not todo_id:
            print(f"{Colors.RED}✗ Error: ID cannot be empty!{Colors.END}")
            return
        
        todo_id = int(todo_id)
        new_description = input(f"{Colors.BOLD}Enter new description:{Colors.END} ").strip()
        
        if not new_description:
            print(f"{Colors.RED}✗ Error: Description cannot be empty!{Colors.END}")
            return
        
        todo = manager.update_todo(todo_id, new_description)
        print(f"\n{Colors.GREEN}┌────────────────────────────────────────────────────────────┐")
        print(f"│  ✓ Todo updated successfully!                             │")
        print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")
        print(f"{Colors.DIM}ID: {todo_id} | New description: {todo.description}{Colors.END}\n")
    except ValueError as e:
        if "invalid literal" in str(e):
            print(f"{Colors.RED}✗ Error: Invalid ID format. Please enter a number.{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Error: {e}{Colors.END}")


def handle_delete_todo(manager):
    """Handle the delete todo command."""
    print(f"\n{Colors.RED}┌────────────────────────────────────────────────────────────┐")
    print(f"│  🗑️  Delete Todo                                            │")
    print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")
    
    try:
        todo_id = input(f"{Colors.BOLD}Enter todo ID to delete:{Colors.END} ").strip()
        if not todo_id:
            print(f"{Colors.RED}✗ Error: ID cannot be empty!{Colors.END}")
            return
        
        todo_id = int(todo_id)
        confirm = input(f"{Colors.YELLOW}⚠️  Are you sure you want to delete todo {todo_id}? (yes/no):{Colors.END} ").strip().lower()
        
        if confirm in ['yes', 'y']:
            todo = manager.delete_todo(todo_id)
            print(f"\n{Colors.GREEN}┌────────────────────────────────────────────────────────────┐")
            print(f"│  ✓ Todo deleted successfully!                             │")
            print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")
            print(f"{Colors.DIM}Deleted: {todo.description}{Colors.END}\n")
        else:
            print(f"{Colors.YELLOW}ℹ️  Delete operation cancelled.{Colors.END}")
    except ValueError as e:
        if "invalid literal" in str(e):
            print(f"{Colors.RED}✗ Error: Invalid ID format. Please enter a number.{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Error: {e}{Colors.END}")


def handle_complete_todo(manager):
    """Handle the mark complete command."""
    print(f"\n{Colors.GREEN}┌────────────────────────────────────────────────────────────┐")
    print(f"│  ✓ Mark Todo as Complete                                  │")
    print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")
    
    try:
        todo_id = input(f"{Colors.BOLD}Enter todo ID to mark complete:{Colors.END} ").strip()
        if not todo_id:
            print(f"{Colors.RED}✗ Error: ID cannot be empty!{Colors.END}")
            return
        
        todo_id = int(todo_id)
        todo = manager.mark_todo_complete(todo_id)
        print(f"\n{Colors.GREEN}┌────────────────────────────────────────────────────────────┐")
        print(f"│  ✓ Todo marked as complete! 🎉                            │")
        print(f"└────────────────────────────────────────────────────────────┘{Colors.END}")
        print(f"{Colors.DIM}Task: {todo.description}{Colors.END}\n")
    except ValueError as e:
        if "invalid literal" in str(e):
            print(f"{Colors.RED}✗ Error: Invalid ID format. Please enter a number.{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Error: {e}{Colors.END}")


def main():
    """Main application loop."""
    manager = TodoManager()
    setup_autocomplete()
    
    print_banner()
    print(f"{Colors.CYAN}{Colors.BOLD}Welcome! {Colors.END}Manage your tasks efficiently with style! 🚀\n")
    
    while True:
        display_menu()
        user_input = input(f"{Colors.BOLD}{Colors.CYAN}➜{Colors.END} {Colors.BOLD}Command:{Colors.END} ").strip()
        
        command, args = parse_command(user_input)
        
        if command == "add":
            handle_add_todo(manager)
        elif command == "view":
            handle_view_todos(manager)
        elif command == "update":
            handle_update_todo(manager)
        elif command == "delete":
            handle_delete_todo(manager)
        elif command == "complete":
            handle_complete_todo(manager)
        elif command == "help":
            continue  # Menu is displayed at the start of loop
        elif command == "exit":
            print(f"\n{Colors.CYAN}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗")
            print(f"║                                                            ║")
            print(f"║          {Colors.YELLOW}Thank you for using Todo App! 👋{Colors.CYAN}                ║")
            print(f"║              {Colors.GREEN}Keep being productive! ✨{Colors.CYAN}                     ║")
            print(f"║                                                            ║")
            print(f"╚════════════════════════════════════════════════════════════╝{Colors.END}\n")
            break
        elif command is None or command == "":
            print(f"{Colors.RED}✗ Error: No command entered. Please try again.{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Error: Command '{command}' not recognized.{Colors.END}")
            print(f"{Colors.YELLOW}💡 Tip: Type 'help' to see available commands or use TAB to autocomplete.{Colors.END}")


if __name__ == "__main__":
    main()