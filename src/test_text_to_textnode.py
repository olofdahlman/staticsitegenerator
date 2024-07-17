#Test code for the text_to_textnode function
from text_to_textnode import text_to_textnode
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)
import unittest

class TestText_to_Textnode(unittest.TestCase):
    def test_text_to_textnode_positive_all(self):
        text1 = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        outcome1 = [
    TextNode("This is ", text_type_text),
    TextNode("text", text_type_bold),
    TextNode(" with an ", text_type_text),
    TextNode("italic", text_type_italic),
    TextNode(" word and a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" and an ", text_type_text),
    TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", text_type_text),
    TextNode("link", text_type_link, "https://boot.dev"),
]
        self.assertEqual(text_to_textnode(text1), outcome1)

    def test_text_to_textnode_asterisk_error(self):
        string1 = "This is a string with ****many**** improper ***asterisks***"
        with self.assertRaises(Exception) as context:
            string_to_text1 = text_to_textnode(string1)
        self.assertEqual(str(context.exception), "3 or more asterisks in a row, please separate bolded and italic parts by a space and use asterisks for nothing else")


if __name__ == "__main__":
    unittest.main()