import unittest
from block_to_block_type import block_to_block_type, BlockType
class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# "), BlockType.HEADING1)
        self.assertEqual(block_to_block_type("```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> "), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- "), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. "), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("This is a paragraph of text"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("- This is the first list item in a list block\n- This is a list item\n- This is another list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("```if cat != hungry:   return \"fake cat\" ```"), BlockType.CODE   )
