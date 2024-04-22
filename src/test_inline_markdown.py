import unittest

from inline_markdown import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self) -> None:
        node = TextNode("This is a text with a **bolded** word", text_type_text)
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
        )

    def test_delim_doublebold(self) -> None:
        node = TextNode(
            "This is a text with a **double** **bolded** word", text_type_text
        )
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("double", text_type_bold),
                TextNode(" ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
        )

    def test_delim_italic(self) -> None:
        node = TextNode("This is a text with an *italic* word", text_type_text)
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
        )

    def test_delim_code(self) -> None:
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes: list[TextNode] = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
        )
