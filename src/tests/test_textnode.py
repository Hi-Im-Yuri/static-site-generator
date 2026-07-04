import unittest

from resources.textnode import TextNode, TextType, text_node_to_html_node
from resources.leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("blah blah balh", TextType.IMAGE, "https://www.github.com")
        node4 = TextNode("blah blah balh", TextType.IMAGE, "https://www.github.com")
        node5 = TextNode("blah blah balh", TextType.IMAGE)
        node6 = TextNode("test me", TextType.BOLD)
        node7 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node6, node)
        self.assertNotEqual(node3, node5)
        self.assertNotEqual(node, node7)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.val, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.val, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.val, "This is bold")


if __name__ == "__main__":
    unittest.main()