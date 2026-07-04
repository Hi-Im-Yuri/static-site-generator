from .htmlnode import HTMLNode
from .leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children: list[HTMLNode] | None, props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError(f"no tag detected for parent node {self}")
        elif not self.children:
            raise ValueError(f"no children for parent node {self}")
        html_string = f"<{self.tag}>"
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"
        return html_string