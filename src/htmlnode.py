from typing import Any

# from textnode import TextNode


class HtmlNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list | None = None,
        props: dict | None = None,
    ) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[Any] | None = children
        self.props: dict[Any, Any] | None = props

        # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        # children - A list of HTMLNode objects representing the children of this node
        # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def __eq__(self, other) -> bool:
        if not isinstance(other, HtmlNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and sorted(self.props.items()) == sorted(other.props.items())
        )

    def to_html(self) -> None:  # type: ignore
        raise NotImplementedError("Subclass Should implement this")

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        attributes: str = ""
        # for key, value in self.props.items():
        #     attributes += " " + key + "=" + '"' + value + '"'
        for prop in sorted(self.props):
            attributes += f' {prop}="{self.props[prop]}"'
        return attributes

    def __repr__(self) -> str:
        return f"HTMLNODE(\ntag: {self.tag}\n value: {self.value}\n Children: {self.children}\n Props: {self.props})"


class LeafNode(HtmlNode):
    def __init__(
        self,
        tag: str | None,
        value: str | None,
        props: dict | None = None,
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:  # type: ignore
        if self.value is None:
            raise ValueError("Invalid HTML: Leaf Nodes must have a Value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return (
            f"LEAFNODE(\ntag: {self.tag}\n value: {self.value}\n Props: {self.props})"
        )


class ParentNode(HtmlNode):
    def __init__(
        self,
        tag: str,
        children: list[Any],
        props: dict | None = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:  # type: ignore
        if self.tag is None:
            raise ValueError("Invalid HTML: Parent Nodes must have a Tag")
        if self.children is None:
            raise ValueError("Invalid HTML: Parent Nodes must have children nodes")
        html_output: str = f"<{self.tag}>"
        for child in self.children:
            html_output += child.to_html()
        html_output += f"</{self.tag}>"
        return html_output

    def __repr__(self) -> str:
        return f"PARENTNODE(\ntag: {self.tag}\n children: {self.children}\n Props: {self.props})"
