from multiprocessing import dummy

from htmlnode import HtmlNode
from textnode import TextNode


def main() -> None:
    dummynode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(dummynode)
    dummyhtmlnode = HtmlNode(
        "a", "PayPal", None, {"href": "https://www.paypal.com", "target": "_blank"}
    )
    # print("\n\n")
    print(dummyhtmlnode)
    print("\n\n")
    print(dummyhtmlnode.props_to_html())


if __name__ == "__main__":
    main()
