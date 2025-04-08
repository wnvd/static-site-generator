def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    f_blocks = []
    for block in blocks:
        if block == "":
            continue
        f_blocks.append(block.strip())
    return f_blocks
