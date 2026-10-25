import json
from pathlib import Path
from datetime import datetime


class TaskManager:
    """Manages tasks and stores them in a JSON file."""

    def __init__(self, file_path="tasks.json"):
        self.file_path = Path(file_path)
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load existing tasks when the application starts."""
        if not self.file_path.exists():
            self.tasks = []
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                self.tasks = json.load(file)

            if not isinstance(self.tasks, list):
                raise ValueError("Task data must be a list.")

            for task in self.tasks:
                if not isinstance(task, dict):
                    raise ValueError("Invalid task format.")

                if not {"id", "title", "completed", "created_at"}.issubset(task):
                    raise ValueError("A task is missing required fields.")

        except (json.JSONDecodeError, OSError, ValueError) as error:
            raise RuntimeError(f"Could not load tasks: {error}") from error

    def save_tasks(self):
        """Save the current task list."""
        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)

            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=4)

        except OSError as error:
            raise RuntimeError(f"Could not save tasks: {error}") from error

    def add_task(self, title):
        """Create a new task."""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task description cannot be empty.")

        task_id = max(
            (task["id"] for task in self.tasks),
            default=0
        ) + 1

        task = {
            "id": task_id,
            "title": title.strip(),
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.tasks.append(task)

        try:
            self.save_tasks()
        except RuntimeError:
            self.tasks.pop()
            raise

        return task.copy()

    def get_tasks(self):
        """Return a copy of all tasks."""
        return [task.copy() for task in self.tasks]

    def find_task(self, task_id):
        """Find a task using its unique ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task

        raise ValueError(f"No task exists with ID {task_id}.")

    def complete_task(self, task_id):
        """Mark a task as completed."""
        task = self.find_task(task_id)

        if task["completed"]:
            return task.copy()

        task["completed"] = True

        try:
            self.save_tasks()
        except RuntimeError:
            task["completed"] = False
            raise

        return task.copy()

    def remove_task(self, task_id):
        """Delete a task using its ID."""
        task = self.find_task(task_id)
        index = self.tasks.index(task)

        removed_task = self.tasks.pop(index)

        try:
            self.save_tasks()
        except RuntimeError:
            self.tasks.insert(index, removed_task)
            raise

        return removed_task
