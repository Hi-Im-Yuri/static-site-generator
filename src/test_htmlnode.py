import unittest

from htmlnode import HTMLNode, LeafNode
from src import htmlnode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode = HTMLNode()
        htmlnode2 = HTMLNode("img")
        htmlnode3 = HTMLNode("img", "this is an HTML node")
        htmlnode4 = HTMLNode(
            "img", "this is an HTML node", [htmlnode, htmlnode2, htmlnode3]
        )
        htmlnode5 = HTMLNode(
            "a",
            "this is an HTML node",
            [htmlnode, htmlnode2, htmlnode3],
            {"href": "https://www.google.com"},
        )
        htmlnode6 = HTMLNode(
            "img",
            "cute cat picture",
            [htmlnode, htmlnode2, htmlnode3],
            {
                "class": "fit-picture",
                "src": "https://wallpapers.com/images/hd/cute-pictures-67n2v527n1nhtady.jpg",
                "alt": "cat picture",
            },
        )
        self.assertIsInstance(htmlnode, HTMLNode)
        self.assertIsInstance(htmlnode5, HTMLNode)
        print(htmlnode6.props_to_html())
        print(htmlnode5.props_to_html())

        print(htmlnode)
        print(htmlnode5)


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("h1", "Welcome to Boot.dev")
        self.assertEqual(node2.to_html(), "<h1>Welcome to Boot.dev</h1>")

        node3 = LeafNode(None, "hello moto")
        print(node)
        print(node3)


if __name__ == "__main__":
    unittest.main()
