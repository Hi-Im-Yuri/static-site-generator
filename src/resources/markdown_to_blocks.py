def markdown_to_blocks(markdown: str) -> list[str]:
    new_blocks = []
    if not markdown:
        return []
    blocks = markdown.split("\n\n")
    for block in blocks :
        if not block:
            continue
        block = block.strip()
        new_lines = []
        lines = block.split("\n")
        for line in lines:
            line = line.strip()
            new_lines.append(line)
        new_blocks.append("\n".join(new_lines))
    return new_blocks