from enum import Enum

from textnode import TextNode, TextType


def main():
    node1 = TextNode("blah blah balh", "image", "https://www.github.com")
    node2 = TextNode("blah blah balh", "image", "https://www.github.com")
    node3 = TextNode("test me", "bold")

    print(node1)
    if node1 == node2:
        print("node1 equals node2")
    if node2 == node3:
        print("node2 equals node3")


main()
