from multiprocessing import dummy

from textnode import TextNode


def main() -> None:
    dummy = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(dummy)


if __name__ == "__main__":
    main()
