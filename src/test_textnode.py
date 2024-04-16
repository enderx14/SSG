import unittest

from textnode import TextNode, text_type_bold, text_type_text


class TestTextNode(unittest.TestCase):
    def test_eq(self) -> None:
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_url_none(self) -> None:
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text, None)
        self.assertEqual(node, node2)

    def test_url_diff(self) -> None:
        node = TextNode("This is a text node", text_type_text, "aa")
        node2 = TextNode("This is a text node", text_type_text, None)
        self.assertNotEqual(node, node2)

    def test_textType_diff(self) -> None:
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_text_diff(self) -> None:
        node = TextNode("This is not a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertNotEqual(node, node2)

    def test_repr(self) -> None:
        node = TextNode("This is a text node", text_type_bold, "https://www.paypal.com")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.paypal.com)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
