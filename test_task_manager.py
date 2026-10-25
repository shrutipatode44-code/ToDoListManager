
import tempfile
import unittest
from pathlib import Path

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Use a temporary file so tests don't modify real tasks.
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(self.file_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task(self):
        task = self.manager.add_task("Learn Python")

        self.assertEqual(task["title"], "Learn Python")
        self.assertFalse(task["completed"])

    def test_empty_task_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task(" ")

    def test_complete_task(self):
        task = self.manager.add_task("Write documentation")

        completed = self.manager.complete_task(task["id"])

        self.assertTrue(completed["completed"])

    def test_remove_task(self):
        task = self.manager.add_task("Temporary task")

        self.manager.remove_task(task["id"])

        self.assertEqual(self.manager.get_tasks(), [])

    def test_tasks_are_saved(self):
        self.manager.add_task("Saved task")

        new_manager = TaskManager(self.file_path)

        self.assertEqual(
            new_manager.get_tasks()[0]["title"],
            "Saved task"
        )

    def test_invalid_task_id(self):
        with self.assertRaises(ValueError):
            self.manager.complete_task(999)


if __name__ == "__main__":
    unittest.main()
