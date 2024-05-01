import re

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
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


def extract_markdown_images(text) -> list[str]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text) -> list[str]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes) -> list[TextNode]:
    node_list: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            node_list.append(old_node)
            continue
        original_text: str = old_node.text
        image_list: list[str] = extract_markdown_images(original_text)
        if len(image_list) == 0:
            node_list.append(old_node)
            continue
        for image in image_list:
            sections: list[str] = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                node_list.append(TextNode(sections[0], text_type_text))
            node_list.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            node_list.append(TextNode(original_text, text_type_text))
    return node_list


def split_nodes_link(old_nodes) -> list[TextNode]:
    node_list: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            node_list.append(old_node)
            continue
        original_text: str = old_node.text
        link_list: list[str] = extract_markdown_links(original_text)
        if len(link_list) == 0:
            node_list.append(old_node)
            continue
        for link in link_list:
            sections: list[str] = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                node_list.append(TextNode(sections[0], text_type_text))
            node_list.append(
                TextNode(
                    link[0],
                    text_type_link,
                    link[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            node_list.append(TextNode(original_text, text_type_text))
    return node_list
