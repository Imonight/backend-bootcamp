import unittest
from bulk_rename import parse_new_name


class TestFileNameParser(unittest.TestCase):
    def test_add_prefix(self):
        result = parse_new_name("image1.jpg", r"^(.*)$", r"new_\1")
        self.assertEqual(result, "new_image1.jpg")

    def test_replace_number(self):
        result = parse_new_name("file_123.txt", r"\d+", "999")
        self.assertEqual(result, "file_999.txt")

    def test_no_change(self):
        result = parse_new_name("test.txt", r"abc", "xyz")
        self.assertEqual(result, "test.txt")


if __name__ == "__main__":
    unittest.main()
