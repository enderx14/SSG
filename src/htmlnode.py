from sys import exception
from typing import Any


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
        self.props = props

        # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        # children - A list of HTMLNode objects representing the children of this node
        # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def to_html(self) -> None:
        raise NotImplementedError("Subclass Should implement this")

    def props_to_html(self) -> str:
        attributes: str = ""
        for key, value in self.props.items():
            attributes += " " + key + "=" + '"' + value + '"'
        return attributes

    def __repr__(self) -> str:
        return f"HTMLNODE(\ntag: {self.tag}\n value: {self.value}\n Children: {self.children}\n Props: {self.props})"
