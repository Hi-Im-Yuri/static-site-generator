from splitter import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
import unittest

class TestSplitter(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com)", TextType.TEXT)
        node3 = TextNode("This is text with a link [to google](https://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        new_nodes2 = split_nodes_link([node2])
        self.assertListEqual(new_nodes, [])
        self.assertListEqual(
            [
             TextNode("This is text with a link ", TextType.TEXT),
                 TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                 TextNode(" and ", TextType.TEXT),
                 TextNode("to youtube", TextType.LINK, "https://www.youtube.com"),
            ],
            new_nodes2,
        )
        new_nodes3 = split_nodes_link([node3])
        self.assertListEqual(
            [
             TextNode("This is text with a link ", TextType.TEXT),
                 TextNode("to google", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes3,
        )

    def test_split_nodes_image(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode(
              "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
              TextType.TEXT,
          )
        node3 = TextNode("This is text with a ![cat picture](https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg)", TextType.TEXT)
        new_nodes2 = split_nodes_image([node2])
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes2,
        )
        new_nodes3 = split_nodes_image([node3])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("cat picture", TextType.IMAGE, "https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg"),
            ],
            new_nodes3,
        )

if __name__ == "__main__":
    unittest.main()
