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
    def test_simple_text(self):
        string1 = "This is just a short segment of text"
        string2 = "This is a short segment of text, with some commands and punctuations."
        outcome1 = [TextNode("This is just a short segment of text", text_type_text)]
        outcome2 = [TextNode("This is a short segment of text, with some commands and punctuations.", text_type_text)]

        self.assertEqual(text_to_textnode(string1), outcome1)
        self.assertEqual(text_to_textnode(string2), outcome2)

    def test_inline_text(self):
        string1 = "This is a string with **bolded** text"
        string2 = "This is another string with *italic* and **bolded** text"
        string3 = "This is a third string with `code` text"
        outcome1 = [TextNode("This is a string with ", text_type_text),
                    TextNode("bolded", text_type_bold),
                    TextNode(" text", text_type_text)
                    ]
        outcome2 = [TextNode("This is another string with ", text_type_text), 
                    TextNode("italic", text_type_italic), 
                    TextNode(" and ", text_type_text),
                    TextNode("bolded", text_type_bold),
                    TextNode(" text", text_type_text)
                    ]
        outcome3 = [TextNode("This is a third string with ", text_type_text),
                    TextNode("code", text_type_code),
                    TextNode(" text", text_type_text)
                    ]
        self.assertEqual(text_to_textnode(string1), outcome1)
        self.assertEqual(text_to_textnode(string2), outcome2)
        self.assertEqual(text_to_textnode(string3), outcome3)

    def test_linear_ordered_all(self):
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

    def test_unordered_all(self):
        string1 = "This is another `section of text` with all types like a link to [github](https://github.com/), *bold but actually it's italic*, **actually bolded**, and a repeat of the classic ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        outcome1 = [
    TextNode("This is another ", text_type_text),
    TextNode("section of text", text_type_code),
    TextNode(" with all types like a link to ", text_type_text),
    TextNode("github", text_type_link, "https://github.com/"),
    TextNode(", ", text_type_text),
    TextNode("bold but actually it's italic", text_type_italic),
    TextNode(", ", text_type_text),
    TextNode("actually bolded", text_type_bold),
    TextNode(", and a repeat of the classic ", text_type_text),
    TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")
    ]
        self.assertEqual(text_to_textnode(string1), outcome1)

    def test_asterisk_error(self):
        string1 = "This is a string with ****many**** improper ***asterisks***"
        with self.assertRaises(Exception) as context:
            string_to_text1 = text_to_textnode(string1)
        self.assertEqual(str(context.exception), "3 or more asterisks in a row, please separate bolded and italic parts by a space and use asterisks for nothing else")


if __name__ == "__main__":
    unittest.main()