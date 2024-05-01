import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)
from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
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

    def test_extract_links(self) -> None:
        matches: list[str] = extract_markdown_links(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        )
        self.assertEqual(
            matches,
            [
                (
                    "image",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                (
                    "another",
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png",
                ),
            ],
        )

    def test_extract_image(self) -> None:
        matches: list[str] = extract_markdown_links(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        )
        self.assertEqual(
            matches,
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )

    def test_split_image_nodes(self) -> None:
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
        )
        new_nodes: list[TextNode] = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,  # type: ignore
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image",
                    text_type_image,  # type: ignore
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
            ],
        )

    def test_split_link_nodes(self) -> None:
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another) with text that follows",
            text_type_text,
        )
        new_nodes: list[TextNode] = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_link, "https://www.example.com/another"),
                TextNode(" with text that follows", text_type_text),
            ],
        )
