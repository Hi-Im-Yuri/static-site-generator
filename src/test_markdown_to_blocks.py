import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text.

This is another paragraph of text."""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [
            "# This is a heading",
            "This is a paragraph of text.",
            "This is another paragraph of text."
        ])

        markdown2 = """    # This is a heading

        This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

        - This is the first list item in a list block
        - This is a list item
        - This is another list item"""
        blocks2 = markdown_to_blocks(markdown2)
        self.assertEqual(blocks2, [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ])

    def test_markdown_to_blocks_empty(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, [])
