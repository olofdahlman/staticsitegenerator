import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is some sample text", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is some sample text", None, {"href": "https://www.google.com", "target": "_blank"})
        node3 = HTMLNode("a", "Another set of test text", None, {"target": "_blank"})
        node4 = HTMLNode("h1", "HEADER test", [node3],{"href": "https://www.google.com", "target": "_blank"})

        print(node, node2, node3, node4)
        print(node.props_to_html(), node2.props_to_html())

if __name__ == "__main__":
    unittest.main()