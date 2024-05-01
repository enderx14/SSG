from multiprocessing import dummy

from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
)
from textnode import TextNode, text_node_to_html_node, text_type_code, text_type_text


def main() -> None:
    dummynode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(dummynode)
    dummyhtmlnode = HtmlNode(
        "a", "PayPal", None, {"href": "https://www.paypal.com", "target": "_blank"}
    )
    # print("\n\n")
    # print(dummyhtmlnode)
    # print("\n\n")
    # print(dummyhtmlnode.props_to_html())
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            ParentNode(
                "ul",
                [
                    LeafNode("li", "first item"),
                    LeafNode("li", "second item"),
                    LeafNode("li", "third item"),
                ],
            ),
        ],
    )
    # print(node.to_html())
    # print(text_node_to_html_node(dummynode).to_html())
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    # print(new_nodes)
    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    # print(extract_markdown_images(text))

    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    # print(extract_markdown_links(text))
    node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        text_type_text,
    )
    new_nodes: list[TextNode] = split_nodes_image([node])


if __name__ == "__main__":
    main()
