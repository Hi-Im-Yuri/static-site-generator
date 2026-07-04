import unittest
from resources.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        with open("content/index.md", "r") as f:
            markdown = f.read()
            title = extract_title(markdown)
            self.assertEqual(title, "Tolkien Fan Club")
