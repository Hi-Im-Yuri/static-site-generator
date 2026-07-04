import unittest

from resources.htmlnode import HTMLNode
from resources.leafnode import LeafNode
from resources.parentnode import ParentNode


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
        self.assertEqual(htmlnode5.props_to_html(), ' href=https://www.google.com')
        self.assertEqual(htmlnode6.props_to_html(), ' class=fit-picture src=https://wallpapers.com/images/hd/cute-pictures-67n2v527n1nhtady.jpg alt=cat picture')


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("h1", "Welcome to Boot.dev")
        self.assertEqual(node2.to_html(), "<h1>Welcome to Boot.dev</h1>")
        node3 = LeafNode("b", "This is bold text")
        self.assertEqual(node3.to_html(), "<b>This is bold text</b>")

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        grandchild_node = LeafNode("b", "grandchild")
        child_node1 = ParentNode("span", [grandchild_node])
        parent_node1 = ParentNode("div", [child_node1])
        self.assertEqual(
            parent_node1.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
    unittest.main()