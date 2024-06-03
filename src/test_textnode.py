import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "italic", "None")
        node4 = TextNode("This is a text node", "italic", "None")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)


if __name__ == "__main__":
    unittest.main()
