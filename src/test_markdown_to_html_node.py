#This is the code for the unit tests for the markdown_to_html_node code
#It tests the codes functionality of being able to accept a markdown document and converting it into a tree of parent and child nodes in html format

import unittest
from markdown_to_blocks import markdown_to_blocks
from markdown_to_html_node import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote,
)
class TestMarkdown_to_html_node(unittest.TestCase):
#These tests have specific markdown text features to ensure specific functions are working as intended
        def test_single_line(self):
                md = """
        This is a very simple single paragraph
        """
                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(
                html,
                "<div><p>This is a very simple single paragraph</p></div>"
        )

#        def test_two_lines(self):
#               md = """
#               This is a slightly more complex task
#               with two lines of text
#               """

#               node = markdown_to_html_node(md)
#               html = node.to_html()
#               self.assertEqual(
#                      html,
#                      "<div><p>This is a slightly more complex task with two lines of text</p></div>"
#               )

#        def test_two_paragraphs(self):
#               md = """
#                This is a test with
#                two lines
                
#                And then a further two
#                in a second paragraph
#                """
#               node = markdown_to_html_node(md)
#               html = node.to_html()
#               self.assertEqual(
#                      html,
#                      "<div><p>This is a test with two lines</p><p>And then a further two in a second paragraph</p></div>"
#               )

#        def test_single_line_bold_insert(self):
#               md = """
#                This is a single line with **bold** text in the middle
#                """
               
#               node = markdown_to_html_node(md)
#               html = node.to_html()
#               self.assertEqual(
#                      html,
#                      "<div><p>This is a single line with <b>bold</b> text in the middle</p></div>"
#               )

#        def test_paragraphs(self):
#                md = """
#        This is **bolded** paragraph
#        text in a p
#        tag here

#        This is another paragraph with *italic* text and `code` here

#       """

#                node = markdown_to_html_node(md)
#                html = node.to_html()
#                self.assertEqual(
#                html,
#                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#        )

#test_paragraphs_simple is a heavily commented test so I can track what the function call tree looks like
#Everything is done when 'node' is created by calling markdown_to_html_node first with 'md', the markdown text - the following html = node.to_html is not called immediately
#The first thing markdown_to_html_node does is create 'blocks' variable by calling markdown_to_blocks with the markdown text supplied as an argument
#markdown_to_blocks creates a list of strings by splitting at newline and stripping trailing and leading whitespaces, returned to markdown_to_html_node
#markdown_to_html_node then for loop iterates over each item in the new list, calling block_to_html_node on each and appending the result to a new list
#block_to_html_node in turn finds which type each line (each entry from the block list) is by calling block_to_block_type function
#block_to_block_type captures ONE of the formatting type characters: heading, code, qoute, ordered list and unordered list. Anything else returns text.
#Depending on the type, block_to_html_node then calls the corresponding subfunction to treat that particular type of function, in this case it is paragraph_to_html_node
#This function once again turns the supplied string into a list by splitting on newline (far as I can tell, this should have already been done?) and joins them together again with ' '
#This function then calls text_to_children on the paragraph string
#text_to_children immediately generates a textnode by calling text_to_textnode on the supplied string argument and stores it in a variable
#text_to_textnode first checks if there are issues with the string, like three asterisks '*' or more in a row - this would fuck things up later. Done using regex
#It then creates a TextNode class instance with the raw string and the (in this case) text_type_text supplied and saves this instance to a new list
#The function then uses a key:value for loop to check over each of the three formatting types of inline text here (bold, italic and code) and calls delimiter functions on any found
#Here, the bold and italic delimiter functions will be called at different points in the text. They check if the text is formatted properly (splitting by * generates an uneven number of strings)
#There are also delimiter functions that split off link and image/imaginelink types of strings, though none of those activate with plain text like this
#The TextNode generated is returned to the text_to_children function, which then iterates over each entry in the list (which is one or more TexNode class instances and all links/images)
#On each item of the list, text_node_to_html node is called, which creates a LeafNode class from each entry dependent on its class and appends it to a list
#The paragraph_to_html_node creates an instance of the Parent class instance with "p" as a string denoting paragraph (for other types it'd be different) and the list containing the children leafnodes
#This ParentNode instance is collected in a list in markdown_to_html_node which creates a new ParentNode class with "div" as the string, the list and "None"
#"div" represents the start and end of the document, which is held in the main ParentNode generated by the main function
#The main ParentNode contains a list of children, of which each is a ParentNode in its own regard, though of different types if the text demands it, this is what "p" and "b" represent
#Each one of these ParentNodes in turn contain children LeafNodes which contain the actual strings held within each ParentNode depending on type
#These LeafNodes will also contain links/images and other smaller features
#        def test_simple_paragraphs(self):
#                md = """
#        This is a second paragraph
#        it has some **bold* text too,
#        the intent is that *I* track exactly which functions are called

#        """

#                node = markdown_to_html_node(md)
#                html = node.to_html
#                self.assertEqual(
#                html,
#                "<div><p>This is a second paragraph it has some <b>bold</b> text too, the intent is that <i>I</i> track exactly which functions are called</p><div>"
#        )

#        def test_lists(self):
#                md = """
#        - This is a list
#        - with items
#        - and *more* items

#        1. This is an `ordered` list
#        2. with items
#        3. and more items

#        """

#                node = markdown_to_html_node(md)
#                html = node.to_html()
#                self.assertEqual(
#                html,
#                "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
#        )

#        def test_headings(self):
#                md = """
#        # this is an h1

#        this is paragraph text

        ## this is an h2
#        """

#                node = markdown_to_html_node(md)
#                html = node.to_html()
#                self.assertEqual(
#                html,
#                "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
#                )

#        def test_blockquote(self):
#                md = """
#        > This is a
#        > blockquote block

#        this is paragraph text

#        """

#                node = markdown_to_html_node(md)
#                html = node.to_html()
#                self.assertEqual(
#                html,
#                "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
#                )

#        def test_block_block_type_error(self):
#                incorrect_text_type = 1
#                with self.assertRaises(Exception) as context:
#                        block_type = block_to_block_type(incorrect_text_type)
#                self.assertEqual(
#                        str(context.exception),
#                        "Error: block_to_block_type only accepts string inputs"
#                )

#        def test_block_block_type_error2(self):
#                incorrect_text_type = "Text"  #block_to_block_type should simply process this as a text and return "Paragraph", hence the "Invalid block type" error will not appear
#                with self.assertRaises(ValueError) as context:
#                        block_type = block_to_block_type(incorrect_text_type)
#                self.assertNotEqual(
#                        str(context.exception),
#                        "Invalid block type"
#                )
       

if __name__ == "__main__":
    unittest.main()