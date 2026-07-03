from textnode import TextNode, TextType
from extractor import extract_markdown_images, extract_markdown_links
import re

def split_nodes_image(nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r"(!\[(?:.*?)\]\((?:.*?)\))", node.text)
        for part in parts:
            if not part:
                continue
            image = extract_markdown_images(part)
            if image:
                new_nodes.append(TextNode(image[0][0], TextType.IMAGE, image[0][1]))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes

def split_nodes_link(nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r"(\[(?:.*?)\]\((?:.*?)\))", node.text)
        for part in parts:
            if not part:
                continue
            link = extract_markdown_links(part)
            if link:
                new_nodes.append(TextNode(link[0][0], TextType.LINK, link[0][1]))
            else:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes
