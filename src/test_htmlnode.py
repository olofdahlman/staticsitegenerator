import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_to_html_parent_NO_nesting(self):
        node1 = LeafNode("b","This is sample text", None)
        node2 = LeafNode("i", "This is a link", {"href": "https://boot.dev"})
        node_p1 = ParentNode("p", [node1, node2], None)
        self.assertEqual(node_p1.to_html(), '<p><b>This is sample text</b><i href="https://boot.dev">This is a link</i></p>')

    def test_to_html_parent_nesting(self):
        node1 = LeafNode("b","This is sample text", None)
        node2 = LeafNode("i", "This is a link", {"href": "https://boot.dev"})
        node3 = LeafNode("b", "This is like other text, but not, with a pointless link", {"href": "https://www.youtube.com"})
        node4 = LeafNode("i", "Italics is slightly fancier text, sometimes used by those seeking to distract our meandering eyes", None)
        node_p1 = ParentNode("p", [node1, node2], None)
        node_p11 = ParentNode("p", [node_p1, node3, node4], None)
        self.assertEqual(node_p11.to_html(), ('<p><p><b>This is sample text</b><i href="https://boot.dev">This is a link</i></p>'
                         '<b href="https://www.youtube.com">This is like other text, but not, with a pointless link</b>'
                         '<i>Italics is slightly fancier text, sometimes used by those seeking to distract our meandering eyes</i></p>'
                         ))

    def test_to_html_parent_nesting_and_props(self):
        node1 = LeafNode("b","This is sample text", None)
        node2 = LeafNode("i", "This is a link", {"href": "https://boot.dev"})
        node3 = LeafNode("b", "This is like other text, but not, with a pointless link", {"href": "https://www.youtube.com"} )
        node4 = LeafNode("i", "Italics is slightly fancier text, sometimes used by those seeking to distract our meandering eyes", None)
        node_p1 = ParentNode("p", [node1, node2], None)
        node_p11 = ParentNode("p", [node_p1, node3, node4], {"href": "https://boot.dev"})
        self.assertEqual(node_p11.to_html(), ('<p href="https://boot.dev"><p><b>This is sample text</b><i href="https://boot.dev">This is a link</i></p>'
                         '<b href="https://www.youtube.com">This is like other text, but not, with a pointless link</b>'
                         '<i>Italics is slightly fancier text, sometimes used by those seeking to distract our meandering eyes</i></p>'
                         ))
        
    def test_to_html_parent_nochilderror(self):
        node_p1 = ParentNode("p", None, None)
        with self.assertRaises(ValueError) as context:
            node_p1 = ParentNode("p", None, None)
            node_p1.to_html()
        self.assertEqual(str(context.exception), "ParentNode requires a child node to be defined")


    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()