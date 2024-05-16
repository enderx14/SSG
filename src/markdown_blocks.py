from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node

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
    if block_lines[0].startswith("```") and block_lines[-1].endswith("```"):
        return block_type_code
    else:
        return block_type_paragraph


def block_head_to_htmlNode(block: str) -> HtmlNode:
    if block.startswith("# "):
        return ParentNode("h1", text_to_children(block.lstrip("# ")))
    elif block.startswith("## "):
        return ParentNode("h2", text_to_children(block.lstrip("## ")))
    elif block.startswith("### "):
        return ParentNode("h3", text_to_children(block.lstrip("### ")))
    elif block.startswith("#### "):
        return ParentNode("h4", text_to_children(block.lstrip("#### ")))
    elif block.startswith("##### "):
        return ParentNode("h5", text_to_children(block.lstrip("##### ")))
    else:
        return ParentNode("h6", text_to_children(block.lstrip("###### ")))


def block_quote_to_htmlNode(block: str) -> HtmlNode:
    lines: list[str] = block.split("\n")
    new_lines: list[str] = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid Quote Block")
        new_lines.append(line.lstrip(">").strip())
    quote: str = " ".join(new_lines)
    return ParentNode("blockquote", text_to_children(quote))


def block_code_to_htmlNode(block: str) -> HtmlNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid Code Block")
    text: str = block[4:-3]
    code = ParentNode("code", text_to_children(text))
    return ParentNode("pre", [code])


def block_ul_to_htmlNode(block: str) -> HtmlNode:
    lines: list[str] = block.split("\n")
    li: list[ParentNode] = []
    for line in lines:
        line = line.strip("* ")
        line = line.strip("- ")
        li.append(ParentNode("li", text_to_children(line)))
    return ParentNode("ul", li)


def block_ol_to_htmlNode(block: str) -> HtmlNode:
    lines: list[str] = block.split("\n")
    li: list[ParentNode] = []
    for line in lines:
        line = line[3:]
        li.append(ParentNode("li", text_to_children(line)))
    return ParentNode("ol", li)


def block_p_to_htmlNode(block: str) -> HtmlNode:
    lines: list[str] = block.split("\n")
    paragraph: str = " ".join(lines)
    children: list[HtmlNode] = text_to_children(paragraph)
    return ParentNode("p", children)


def text_to_children(text: str) -> list[HtmlNode]:
    text_nodes: list[TextNode] = text_to_textnodes(text)
    html_nodes: list[HtmlNode] = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def markdown_to_html_node(markdown) -> ParentNode:
    block_list: list[str] = markdown_to_blocks(markdown)
    html_node_list: list[HtmlNode] = []
    block_dict = {}
    for block in block_list:
        block_dict[block] = block_to_block_type(block)
        if block_to_block_type(block) == block_type_code:
            html_node_list.append(block_code_to_htmlNode(block))
        elif block_to_block_type(block) == block_type_heading:
            html_node_list.append(block_head_to_htmlNode(block))
        elif block_to_block_type(block) == block_type_ordered_list:
            html_node_list.append(block_ol_to_htmlNode(block))
        elif block_to_block_type(block) == block_type_paragraph:
            html_node_list.append(block_p_to_htmlNode(block))
        elif block_to_block_type(block) == block_type_quote:
            html_node_list.append(block_quote_to_htmlNode(block))
        elif block_to_block_type(block) == block_type_unordered_list:
            html_node_list.append(block_ul_to_htmlNode(block))
    return ParentNode("div", html_node_list)


def extract_title(markdown) -> str:
    blocks: list[str] = markdown_to_blocks(markdown)
    h1: str = ""
    for block in blocks:
        if block_to_block_type(block) == block_type_heading and block.startswith("# "):
            h1 = block.lstrip("#").strip()
    return h1
