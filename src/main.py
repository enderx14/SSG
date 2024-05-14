from multiprocessing import dummy

from htmlnode import HtmlNode, LeafNode, ParentNode
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    text_to_textnodes,
)
from markdown_blocks import (
    block_code_to_htmlNode,
    block_head_to_htmlNode,
    block_ol_to_htmlNode,
    block_p_to_htmlNode,
    block_quote_to_htmlNode,
    block_to_block_type,
    block_ul_to_htmlNode,
    markdown_to_blocks,
    markdown_to_html_node,
)
from textnode import TextNode, text_node_to_html_node, text_type_code, text_type_text
from utils import copy_dir


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
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    # print(text_to_textnodes(text))
    markdown = """This is **bolded** paragraph

    ## This is a Heading 2


    ```print("hello world");
       print("")
    ```

> THIS IS A QUOTE FROM MJ
> THE GIRL IS SO DANGEROUS    

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line


* This is a list
* with items
* multiple years worth
"""
    # print(markdown_to_blocks(markdown))
    # print("\n")
    # print(markdown_to_html_node(markdown).to_html())

    for block in markdown_to_blocks(markdown):
        if block_to_block_type(block) == "paragraph":
            pass
            # print(block_p_to_htmlNode(block).to_html())
        # print(block_to_block_type(block))

    root_src_dir = "/home/ender/Projects/BootDev/SSG/static"  # Path/Location of the source directory
    root_dst_dir = (
        "/home/ender/Projects/BootDev/SSG/public"  # Path to the destination folder
    )

    copy_dir(root_src_dir, root_dst_dir)


if __name__ == "__main__":
    main()
