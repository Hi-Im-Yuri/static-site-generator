import unittest
from extractor import extract_markdown_images, extract_markdown_links

class TestExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![alt text](url)"
        text2 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text2)
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        images2 = extract_markdown_images(text)
        self.assertEqual(images2, [("alt text", "url")])

    def test_extract_markdown_links(self):
        text = "[anchor text](url)"
        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text2)
        self.assertEqual(links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        links2 = extract_markdown_links(text)
        self.assertEqual(links2, [("anchor text", "url")])

if __name__ == '__main__':
    unittest.main()
