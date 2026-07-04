from typing import Any
from .htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, val: str | None, props: dict[str, str] | None = None):
        super().__init__(tag, val, None, props)

    def to_html(self) -> str:
        if not self.val and not self.tag:
            raise ValueError
        elif not self.tag:
            return self.val
        if self.tag == "img":
            props_string = "".join([f' {key}="{value}"' for key, value in self.props.items()])
            return f"<{self.tag}{props_string}>"
        if self.tag == "a":
            props_string = "".join([f' {key}="{value}"' for key, value in self.props.items()])
            return f"<{self.tag}{props_string}>{self.val}</{self.tag}>"
        return f"<{self.tag}>{self.val}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode {self.tag} has value {self.val} and props {self.props}"
