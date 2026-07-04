def extract_title(markdown: str) -> str:
    header = markdown.split("# ", 1)
    title = header[1].split("\n", 1)
    return title[0]