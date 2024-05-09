import unittest

from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
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

    def test_extract_images(self) -> None:
        matches: list[str] = extract_markdown_images(
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

    def test_extract_links(self) -> None:
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

    def test_text_to_textnodes_simple(self) -> None:
        text: str = (
            "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        )

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", text_type_text, None),
                TextNode("text", text_type_bold, None),
                TextNode(" with an ", text_type_text, None),
                TextNode("italic", text_type_italic, None),
                TextNode(" word and a ", text_type_text, None),
                TextNode("code block", text_type_code, None),
                TextNode(" and an ", text_type_text, None),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and a ", text_type_text, None),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
        )

    def test_text_to_textnodes_complex(self) -> None:
        text: str = (
            "This is **bold text 1** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and *another italic* and a [link](https://boot.dev) and **bold 2**"
        )

        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", text_type_text, None),
                TextNode("bold text 1", text_type_bold, None),
                TextNode(" with an ", text_type_text, None),
                TextNode("italic", text_type_italic, None),
                TextNode(" word and a ", text_type_text, None),
                TextNode("code block", text_type_code, None),
                TextNode(" and an ", text_type_text, None),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and ", text_type_text, None),
                TextNode("another italic", text_type_italic, None),
                TextNode(" and a ", text_type_text, None),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text, None),
                TextNode("bold 2", text_type_bold, None),
            ],
        )
