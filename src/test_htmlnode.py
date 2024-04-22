import unittest
from lib2to3.pytree import Leaf

from htmlnode import HtmlNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self) -> None:
        node = HtmlNode(
            "a", "GOOGLE", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HtmlNode(
            "a", "GOOGLE", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node, node2)

    def test_noteq_tag(self) -> None:
        node = HtmlNode(
            "a", "GOOGLE", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        node2 = HtmlNode(
            "p", "GOOGLE", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertNotEqual(node, node2)

    def test_repr(self) -> None:
        node = HtmlNode(
            "a", "GOOGLE", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            "HTMLNODE(\ntag: a\n value: GOOGLE\n Children: None\n Props: {'href': 'https://www.google.com', 'target': '_blank'})",
            repr(node),
        )

    def test_props_to_html(self) -> None:
        node = HtmlNode(
            "div",
            "Hellooo Wooorld!!",
            None,
            {"class": "centered 1col", "id": "greeting"},
        )
        self.assertEqual(node.props_to_html(), ' class="centered 1col" id="greeting"')

    def test_toHtml(self) -> None:
        node = LeafNode(
            "a", "GOOGLE", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">GOOGLE</a>',
        )

    def test_toHtml_no_tag(self) -> None:
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_toHtml_parent(self) -> None:
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_toHtml_ul(self) -> None:
        node = ParentNode(
            "ul",
            [
                LeafNode("li", "first item"),
                LeafNode("li", "second item"),
                LeafNode("li", "third item"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<ul><li>first item</li><li>second item</li><li>third item</li></ul>",
        )

    def test_toHtml_nested_parents(self) -> None:
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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
