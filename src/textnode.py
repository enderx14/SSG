class TextNode:
    def __init__(self, text: str, text_type: str, url: str) -> None:
        self.text: str = text
        self.text_type: str = text_type
        self.url: str = url or None

    def __eq__(self, node) -> bool:
        if isinstance(node, TextNode):
            return (
                self.text == node.text
                and self.text_type == node.text_type
                and self.url == node.url
            )
        else:
            return False

    def __repr__(self) -> str:
        return f'TextNode("{self.text}","{self.text_type}",{self.url})'
