#unittest code for the markdown_to_blocks code
import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdown_to_blocks(unittest.TestCase):
    def test_simple_blocks(self):
        block1 = """# Generic heading at the top
This is the first paragraph, with some `code text` in it.
It is followed by some closing text, and these three should end up in three strings in a list."""

        block2 = """# This is another generic heading in block2
        
It is followed by two newlines instead of one.
        
The last paragraph is also separated by two newlines, but only these three strings should be in the final list."""



        outcome1 = ['# Generic heading at the top', 
                    'This is the first paragraph, with some `code text` in it.', 
                    'It is followed by some closing text, and these three should end up in three strings in a list.'
                    ]
        
        outcome2 = ['# This is another generic heading in block2',
                    'It is followed by two newlines instead of one.',
                    'The last paragraph is also separated by two newlines, but only these three strings should be in the final list.'
                    ]
        self.assertEqual(markdown_to_blocks(block1), outcome1)
        self.assertEqual(markdown_to_blocks(block2), outcome2)

    def test_list_blocks(self):
        block1 = """# A generic heading
        
* First entry of a list
        
* This list has two newlines between first and second entry
* But only one newline between second and third, and they should all be unique entries in the list - the extra newline should not matter"""

        outcome1 = ['# A generic heading',
                    '* First entry of a list',
                    '* This list has two newlines between first and second entry',
                    '* But only one newline between second and third, and they should all be unique entries in the list - the extra newline should not matter'
                    ]
        self.assertEqual(markdown_to_blocks(block1), outcome1)

    def test_basicblock_from_bootdev(self):
        block1 = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        outcome1 = ['# This is a heading', 
                    'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                    '* This is the first list item in a list block', 
                    '* This is a list item', 
                    '* This is another list item'
                    ]
    
        self.assertEqual(markdown_to_blocks(block1), outcome1)



if __name__ == "__main__":
    unittest.main()