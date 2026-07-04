from stat import UF_NODUMP

from htmlnode import HTMLNode
from textnode import TextNode, TextType
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from leafnode import LeafNode
from parentnode import ParentNode
from text_to_textnode import text_to_textnodes

def markdown_to_html(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode("div", [])
    for block in blocks:
        block_type = block_to_block_type(block)
        node = block_to_node(block_type, block)
        parent.children.append(node)
    return parent

def text_to_children(text: str) -> list[LeafNode]:
    textnodes = text_to_textnodes(text)
    childNodes = []
    for textnode in textnodes:
        match textnode.text_type:
            case TextType.TEXT:
                childNodes.append(LeafNode(None, textnode.text))
            case TextType.BOLD:
                childNodes.append(LeafNode("b", textnode.text))
            case TextType.ITALIC:
                childNodes.append(LeafNode("i", textnode.text))
            case TextType.CODE:
                childNodes.append(LeafNode("code", textnode.text))
            case TextType.LINK:
                childNodes.append(LeafNode("a", textnode.text, {"href": textnode.url}))
            case TextType.IMAGE:
                childNodes.append(LeafNode("img", "", {"src": textnode.url, "alt": textnode.text}))
    return childNodes

def block_to_node(block_type: BlockType, block: str) -> ParentNode:
    match block_type:
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_children(block.replace("\n", " ")))
        case BlockType.HEADING1:
            return ParentNode("h1", text_to_children(block))
        case BlockType.HEADING2:
            return ParentNode("h2", text_to_children(block))
        case BlockType.HEADING3:
            return ParentNode("h3", text_to_children(block))
        case BlockType.HEADING4:
            return ParentNode("h4", text_to_children(block))
        case BlockType.HEADING5:
            return ParentNode("h5", text_to_children(block))
        case BlockType.HEADING6:
            return ParentNode("h6", text_to_children(block))
        case BlockType.CODE:
            return ParentNode("pre", [LeafNode("code", block.strip("```"))])
        case BlockType.QUOTE:
            return ParentNode("blockquote", text_to_children(block))
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul", list_to_children(block))
        case BlockType.ORDERED_LIST:
            return ParentNode("ol", list_to_children(block))

def textnode_to_html_node(textnode: TextNode) -> HTMLNode:
    match textnode.text_type:
        case TextType.TEXT:
            return LeafNode(None, textnode.text)
        case TextType.BOLD:
            return LeafNode("b", textnode.text)
        case TextType.ITALIC:
            return LeafNode("i", textnode.text)
        case TextType.CODE:
            return LeafNode("code", textnode.text)
        case TextType.LINK:
            return LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})

def list_to_children(block: str, ordered: bool) -> list[ParentNode]:
    children = []
    list_items = block.split("\n")
    for list_item in list_items:
        if ordered:
            ordered_items = list_item.split(". ", 1)
            list_children = text_to_children(ordered_items[1].strip())
            children.append(ParentNode("li", list_children))
        else:
            unordered_items = list_item.split("- ", 1)
            list_children = text_to_children(unordered_items[1].strip())
            children.append(ParentNode("li", list_children))
    return children
