import unittest
from resources.text_to_textnode import text_to_textnodes
from resources.textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [])

        text2 = "This is **bold** and *italic* and `code`"
        nodes = text_to_textnodes(text2)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ])

        text3 = "This is **bold** text before an image ![alt text](https://example.com/image.jpg) and an *italic* link [link text](https://example.com)"
        nodes = text_to_textnodes(text3)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text before an image ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" link ", TextType.TEXT),
            TextNode("link text", TextType.LINK, "https://example.com"),
        ])

        text4 = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text4)
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])