from multiprocessing import dummy

from htmlnode import HtmlNode, LeafNode, ParentNode
from textnode import (
    TextNode,
    split_nodes_delimiter,
    text_node_to_html_node,
    text_type_code,
    text_type_text,
)


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
    print(new_nodes)


if __name__ == "__main__":
    main()
