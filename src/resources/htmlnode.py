from asyncio.taskgroups import TaskGroup
from signal import valid_signals
from typing import Any


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        val: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.val = val
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        result = "".join(f" {key}={value}" for key, value in self.props.items())
        return result

    def __repr__(self) -> str:
        return f"HTMLNode {self.tag} has value {self.val}, children {self.children} and props {self.props}"