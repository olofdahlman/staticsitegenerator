#unittest code for the markdown_to_blocks code
import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdown_to_blocks(unittest.TestCase):
    def test_simple_blocks(self):
        block1 = """Generic heading at the top.
This is the second line, with some `code text` in it.
It is followed by some closing text, and these three should end up in a single list entry.
"""

        block2 = """# This is another generic heading in block2.

It is followed by two newlines instead of one.

The last line is also a paragraph, as separated by two newlines."""



        outcome1 = ['''Generic heading at the top.
This is the second line, with some `code text` in it.
It is followed by some closing text, and these three should end up in a single list entry.'''
]
        
        outcome2 = ['# This is another generic heading in block2.',
                    'It is followed by two newlines instead of one.',
                    'The last line is also a paragraph, as separated by two newlines.'
                    ]
        self.assertEqual(markdown_to_blocks(block1), outcome1)
        self.assertEqual(markdown_to_blocks(block2), outcome2)

#    def test_list_blocks(self):
#        block1 = """# A generic heading
        
#* First entry of a list
        
#* This list has two newlines between first and second entry
#* But only one newline between second and third, so these two are in their own separate list because they are separated by block."""

#        outcome1 = ['# A generic heading',
#                    '* First entry of a list',
#                    '''* This list has two newlines between first and second entry
#                    * But only one newline between second and third, so these two are in their own separate list because they are separated by block.'''
#                    ]
#        self.assertEqual(markdown_to_blocks(block1), outcome1)

#    def test_basicblock_from_bootdev(self):
#        block1 = """# This is a heading.

#This is a paragraph of text. It has some **bold** and *italic* words inside of it.

#* This is the first list item in a list block
#* This is a list item
#* This is another list item"""
#        outcome1 = ['# This is a heading.', 
#                    'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
#                    '''* This is the first list item in a list block 
#                    * This is a list item 
#                    * This is another list item'''
#                    ]
    
#        self.assertEqual(markdown_to_blocks(block1), outcome1)

class Testblock_to_block_type(unittest.TestCase):
        def test_block_to_block_type_heading(self):
            block1 = "### This is sample text starting with a heading marker"
            outcome1 = "Heading"
            self.assertEqual(block_to_block_type(block1), outcome1)

        def test_block_to_block_type_heading_incorrect(self):
            block1 = "######## This is sample text with too many heading indicators at the start in it"
            outcome1 = "Heading"
            self.assertNotEqual(block_to_block_type(block1), outcome1) 

        def test_block_to_block_type_code(self):
            block1 = "```This is sample text encased in a code block```"
            outcome1 = "Code"
            self.assertEqual(block_to_block_type(block1), outcome1)

        def test_block_to_block_type_code_incorrect(self):
            block1 = "This is sample text with ```code parts in an inline pattern``` instead of being a whole block"
            block2 = "```This is sample text where the code``` part ends too early"
            outcome1 = "Code"
            self.assertNotEqual(block_to_block_type(block1), outcome1)
            self.assertNotEqual(block_to_block_type(block2), outcome1)
            #This test is not equal because this code is supposed to treat whole blocks of text, where the type denominators are at the beginning
            #Code in the middle of the text is inline text and not treated by these functions

        def test_block_to_block_type_qoute(self):
            block1 = ">This is sample text starting with a qoute marker"
            outcome1 = "Qoute"
            self.assertEqual(block_to_block_type(block1), outcome1)
        
        def test_block_to_block_type_qoute_multiple(self):
            block1 = ">This a block of qoutes with multiple lines\n>To ensure that the program does not break\n>While handling it"
            outcome1 = "Qoute"
            self.assertEqual(block_to_block_type(block1), outcome1)
            #Test to ensure it can handle a block of qoutes with newlines in it - it should return qoute type as long as each line starts with the > character and no space

        def test_block_to_block_type_qoute_multiple_poor_formatting(self):
            block1 = ">This is sample text with too many>qoutemarks >in it"
            outcome1 = "Qoute"
            self.assertEqual(block_to_block_type(block1), outcome1) 
            #Regex should find only the first qoutemark, and if there are multiple the block isn't correctly constructed by the user - it will only find the first

        def test_block_to_block_type_unordered_list(self):
            block1 = "* This is an unordered list"
            block2 = "- This is an unordered list with the other character type"
            outcome1 = "Unordered list"
            self.assertEqual(block_to_block_type(block1), outcome1)
            self.assertEqual(block_to_block_type(block2), outcome1)

        def test_block_to_block_type_unordered_list_incorrect(self):
            block1 = "*This is sample text with improper unordered list syntax"
            block2 = "-This is another list with improper unordered list syntax and extra * characters in the text"
            outcome1 = "Unordered list"
            self.assertNotEqual(block_to_block_type(block1), outcome1) 
            self.assertNotEqual(block_to_block_type(block2), outcome1) 

        def test_block_to_block_type_unordered_list_multiple_incorrect(self):
           block1 = "*   This is another list with too many spaces at the beginning"
           block2 = "** This is another list with too many hashtags in the beginning"
           outcome1 = "Unordered list"
           self.assertNotEqual(block_to_block_type(block1), outcome1) 
           self.assertNotEqual(block_to_block_type(block2), outcome1)

        def test_block_to_block_type_ordered_list_single(self):
            block1 = "1. This is an ordered list entry"
            block2 = "1. This is another ordered list entry"
            outcome1 = "Ordered list"
            self.assertEqual(block_to_block_type(block1), outcome1)
            self.assertEqual(block_to_block_type(block2), outcome1)

        def test_block_to_block_type_ordered_list_multiple(self):
            block1 = "1. This is an ordered list entry\n2. With multiple lines\n3. To test that it can process it"
            block2 = "1. This is another ordered list\n2. With many shorter\n3. Lines.\n4. Interesting stuff goes here\n5. More stuff.\n6. Last line of stuff"
            outcome1 = "Ordered list"
            self.assertEqual(block_to_block_type(block1), outcome1)
            self.assertEqual(block_to_block_type(block2), outcome1)

        def test_block_to_block_type_ordered_list_single_incorrect(self):
            block1 = "1.This is an incorrect ordered list entry"
            block2 = "1 . This is another incorrect ordered list entry"
            outcome1 = "Ordered list"
            self.assertNotEqual(block_to_block_type(block1), outcome1)
            self.assertNotEqual(block_to_block_type(block2), outcome1)

        def test_block_to_block_type_ordered_list_multiple_incorrect(self):
            block1 = "1. This is an ordered list entry\n2.With multiple lines\n3. To test that it can process it"
            block2 = "1 . This is another ordered list\n2. With many shorter\n3. Lines.\n4. Interesting stuff goes here\n5. More stuff.\n6. Last line of stuff"
            outcome1 = "Ordered list"
            self.assertNotEqual(block_to_block_type(block1), outcome1)
            self.assertNotEqual(block_to_block_type(block2), outcome1)

        def test_block_to_block_text(self):
            block1 = "This is just some text"
            block2 = "This is some text with * other block type >denominators"
            block3 = "1.Another text block, where ```it should also``` register as text ### due to improper syntax formatting"
            outcome1 = "Paragraph"
            self.assertEqual(block_to_block_type(block1), outcome1)
            self.assertEqual(block_to_block_type(block2), outcome1)
            self.assertEqual(block_to_block_type(block3), outcome1)
        
        def test_block_to_block_type_error_list_input(self):
            block1 = ["This is a list with different block types", ">The code should return an error", "```Because we do not want it to accept anything other than strings```"]
            with self.assertRaises(Exception) as context:
                block_type = block_to_block_type(block1)
            self.assertEqual(str(context.exception), "Error: block_to_block_type only accepts string inputs")


if __name__ == "__main__":
    unittest.main()