from pipes import quote

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown) -> list[str]:
    temp: list[str] = markdown.split("\n\n")
    final = []
    for block in temp:
        if block != "":
            t = block.strip()
            final.append(t)
    return final


def block_to_block_type(block: str) -> str:
    block_lines: list[str] = block.split("\n")
    quote: bool = False
    unordered: bool = False
    ordered: bool = False
    if block.startswith("1. "):
        lines = len(block_lines)
        i = 1
        for line in block_lines:
            if line.startswith(f"{i}. "):
                ordered = True
                i += 1
                continue
            ordered = False
    if len(block_lines) > 1:
        for line in block_lines:
            if line.startswith(">"):
                quote = True
            elif line.startswith("* ") or line.startswith("- "):
                unordered = True
            else:
                quote = False
                unordered = False
    if quote:
        return block_type_quote
    if ordered:
        return block_type_ordered_list
    if unordered:
        return block_type_unordered_list
    if block.startswith(("# ", "## ", "### ")) or block.startswith(
        ("#### ", "##### ", "###### ")
    ):
        return block_type_heading
    if block_lines[0].startswith("```") and block_lines[-1].startswith("```"):
        return block_type_code
    else:
        return block_type_paragraph
