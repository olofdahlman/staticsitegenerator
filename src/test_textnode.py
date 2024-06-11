import unittest

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        node3 = TextNode("This is a text node", text_type_italic, "None")
        node4 = TextNode("This is a text node", text_type_italic, "None")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
    
    def test_NOT_eq(self):
        node = TextNode("This is text", text_type_bold)
        node1 = TextNode("This is text", text_type_code)
        self.assertNotEqual(node, node1)

    def test_NOT_eq_2(self):
        node = TextNode("This is text", text_type_code)
        node1 = TextNode("This is also some other text", text_type_code)
        self.assertNotEqual(node, node1)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_textnode_to_leafnode(self):
        txtnode = TextNode("This is another test node", text_type_italic)
        leafnode = LeafNode("i","This is another test node",None)
        self.assertEqual(print(text_node_to_html_node(txtnode)), print(leafnode))

if __name__ == "__main__":
    unittest.main()
