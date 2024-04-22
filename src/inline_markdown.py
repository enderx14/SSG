from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
    node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            node_list.append(node)
            continue
        temp: list = node.text.split(delimiter)
        if len(temp) % 2 == 0:
            raise ValueError(
                "This is not valid Markdown Syntax, formatted section not closed"
            )
        for i in range(len(temp)):
            if temp[i] == "":
                continue
            if i % 2 == 0:
                node_list.append(TextNode(temp[i], text_type_text))
            else:
                node_list.append(TextNode(temp[i], text_type))
    return node_list
