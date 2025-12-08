import unittest
from todo import add_todo, create_todo


class function_that_test(unittest.TestCase):

    def test_add_todo(self):
        add_todo("test task")
        todos = create_todo()
        self.assertIn("test task", todos)


if __name__ == "__main__":
    unittest.main()
