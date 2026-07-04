from resources.delimiter import split_nodes_delimiter
from resources.textnode import TextNode, TextType
import unittest

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertIsNotNone(nodes)
        self.assertIsInstance(nodes, list)
        self.assertEqual(len(nodes), 3)
        self.assertIsInstance(nodes[0], TextNode)
        self.assertEqual(nodes[0].text, "This is text with a ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertIsInstance(nodes[1], TextNode)
        self.assertEqual(nodes[1].text, "code block")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertIsInstance(nodes[2], TextNode)
        self.assertEqual(nodes[2].text, " word")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        old_nodes2 = [TextNode("This is text with no delimiter", TextType.TEXT)]
        nodes2 = split_nodes_delimiter(old_nodes2, "`", TextType.CODE)
        self.assertIsNotNone(nodes2)
        self.assertIsInstance(nodes2, list)
        self.assertEqual(len(nodes2), 1)
        self.assertIsInstance(nodes2[0], TextNode)
        self.assertEqual(nodes2[0].text, "This is text with no delimiter")
        self.assertEqual(nodes2[0].text_type, TextType.TEXT)

        old_nodes3 = [TextNode("This is text with a **bold** word", TextType.TEXT)]
        nodes3 = split_nodes_delimiter(old_nodes3, "**", TextType.BOLD)
        self.assertIsNotNone(nodes3)
        self.assertIsInstance(nodes3, list)
        self.assertEqual(len(nodes3), 3)
        self.assertIsInstance(nodes3[0], TextNode)
        self.assertEqual(nodes3[0].text, "This is text with a ")
        self.assertEqual(nodes3[0].text_type, TextType.TEXT)
        self.assertIsInstance(nodes3[1], TextNode)
        self.assertEqual(nodes3[1].text, "bold")
        self.assertEqual(nodes3[1].text_type, TextType.BOLD)
        self.assertIsInstance(nodes3[2], TextNode)
        self.assertEqual(nodes3[2].text, " word")
        self.assertEqual(nodes3[2].text_type, TextType.TEXT)

        old_nodes4 = [TextNode("This is text with an *italic* word", TextType.TEXT)]
        nodes4 = split_nodes_delimiter(old_nodes4, "*", TextType.ITALIC)
        self.assertIsNotNone(nodes4)
        self.assertIsInstance(nodes4, list)
        self.assertEqual(len(nodes4), 3)
        self.assertIsInstance(nodes4[0], TextNode)
        self.assertEqual(nodes4[0].text, "This is text with an ")
        self.assertEqual(nodes4[0].text_type, TextType.TEXT)
        self.assertIsInstance(nodes4[1], TextNode)
        self.assertEqual(nodes4[1].text, "italic")
        self.assertEqual(nodes4[1].text_type, TextType.ITALIC)
        self.assertIsInstance(nodes4[2], TextNode)
        self.assertEqual(nodes4[2].text, " word")
        self.assertEqual(nodes4[2].text_type, TextType.TEXT)


        old_nodes5 = [TextNode("This is also text with an _italic_ word", TextType.TEXT)]
        nodes5 = split_nodes_delimiter(old_nodes5, "_", TextType.ITALIC)
        self.assertIsNotNone(nodes5)
        self.assertIsInstance(nodes5, list)
        self.assertEqual(len(nodes5), 3)
        self.assertIsInstance(nodes5[0], TextNode)
        self.assertEqual(nodes5[0].text, "This is also text with an ")
        self.assertEqual(nodes5[0].text_type, TextType.TEXT)
        self.assertIsInstance(nodes5[1], TextNode)
        self.assertEqual(nodes5[1].text, "italic")
        self.assertEqual(nodes5[1].text_type, TextType.ITALIC)
        self.assertIsInstance(nodes5[2], TextNode)
        self.assertEqual(nodes5[2].text, " word")
        self.assertEqual(nodes5[2].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()