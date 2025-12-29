"""
Todo Manager Module
Handles all todo item operations and data management.
"""

class TodoItem:
    """Represents a single todo item."""
    
    def __init__(self, id, description, status="pending"):
        self.id = id
        self.description = description
        self.status = status
    
    def __repr__(self):
        return f"TodoItem(id={self.id}, description='{self.description}', status='{self.status}')"


class TodoManager:
    """Manages the collection of todo items."""
    
    def __init__(self):
        self.todos = []
        self.next_id = 1
    
    def generate_unique_id(self):
        """Generate a unique ID for a new todo item."""
        current_id = self.next_id
        self.next_id += 1
        return current_id
    
    def add_todo(self, description):
        """
        Create and store a new todo item.
        
        Args:
            description (str): The todo description
            
        Returns:
            TodoItem: The created todo item
            
        Raises:
            ValueError: If description is empty
        """
        if not description or not description.strip():
            raise ValueError("Todo description cannot be empty")
        
        todo_id = self.generate_unique_id()
        new_todo = TodoItem(todo_id, description.strip())
        self.todos.append(new_todo)
        return new_todo
    
    def get_all_todos(self):
        """
        Return all todo items.
        
        Returns:
            list: List of all TodoItem objects
        """
        return self.todos
    
    def get_todo_by_id(self, todo_id):
        """
        Find a todo item by ID.
        
        Args:
            todo_id (int): The ID to search for
            
        Returns:
            TodoItem or None: The found todo item or None
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def update_todo(self, todo_id, new_description):
        """
        Update a todo item's description.
        
        Args:
            todo_id (int): The ID of the todo to update
            new_description (str): The new description
            
        Returns:
            TodoItem: The updated todo item
            
        Raises:
            ValueError: If todo not found or description is empty
        """
        if not new_description or not new_description.strip():
            raise ValueError("Todo description cannot be empty")
        
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            raise ValueError(f"Todo with ID {todo_id} not found")
        
        todo.description = new_description.strip()
        return todo
    
    def delete_todo(self, todo_id):
        """
        Delete a todo item by ID.
        
        Args:
            todo_id (int): The ID of the todo to delete
            
        Returns:
            TodoItem: The deleted todo item
            
        Raises:
            ValueError: If todo not found
        """
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            raise ValueError(f"Todo with ID {todo_id} not found")
        
        self.todos.remove(todo)
        return todo
    
    def mark_todo_complete(self, todo_id):
        """
        Mark a todo item as complete.
        
        Args:
            todo_id (int): The ID of the todo to mark complete
            
        Returns:
            TodoItem: The updated todo item
            
        Raises:
            ValueError: If todo not found
        """
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            raise ValueError(f"Todo with ID {todo_id} not found")
        
        todo.status = "complete"
        return todo