from nturl2path import url2pathname
import re

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    images = []
    while True:
        altText = re.search(r"!\[(.*?)\]", text)
        url = re.search(r"\((.*?)\)", text)
        if not altText or not url:
            break
        images.append((altText.group(1), (url.group(1))))
        text = text[url.end():]
    return images

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    links = []
    while True:
        anchorText = re.search(r"\[(.*?)\]", text)
        url = re.search(r"\((.*?)\)", text)
        if not anchorText or not url:
            break
        links.append((anchorText.group(1), url.group(1)))
        text = text[url.end():]
    return links
