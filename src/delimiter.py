from leafnode import LeafNode
from textnode import TextNode
from textnode import TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            parts = old_node.text.split(delimiter)
            for i, part in enumerate(parts):
                new_nodes.append(TextNode(part, text_type if i % 2 == 1 else TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes
