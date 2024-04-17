import unittest

from htmlnode import HtmlNode, LeafNode


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


if __name__ == "__main__":
    unittest.main()
