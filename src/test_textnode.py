import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("blah blah balh", TextType.IMAGE, "https://www.github.com")
        node4 = TextNode("blah blah balh", TextType.IMAGE, "https://www.github.com")
        node5 = TextNode("blah blah balh", TextType.IMAGE)
        node6 = TextNode("test me", TextType.BOLD)
        node7 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node6, node)
        self.assertNotEqual(node3, node5)
        self.assertNotEqual(node, node7)

        print(node)
        print(node4)


if __name__ == "__main__":
    unittest.main()
