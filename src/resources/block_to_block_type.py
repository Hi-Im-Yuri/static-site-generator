from enum import Enum
import string

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    HEADING5 = "heading5"
    HEADING6 = "heading6"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if block.startswith("# "):
        return BlockType.HEADING1
    if block.startswith("## "):
        return BlockType.HEADING2
    if block.startswith("### "):
        return BlockType.HEADING3
    if block.startswith("#### "):
        return BlockType.HEADING4
    if block.startswith("##### "):
        return BlockType.HEADING5
    if block.startswith("###### "):
        return BlockType.HEADING6
    if block.startswith("```"):
        return BlockType.CODE
    if block.startswith("> "):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH