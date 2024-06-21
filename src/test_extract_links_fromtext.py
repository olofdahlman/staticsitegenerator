#Unittest for the extract links/images functions
import unittest, re
from extract_links_fromtext import (extract_markdown_images, extract_markdown_links)

#Section of teststrings for the unittests - many are tested at once to ensure specific behaviour
teststring1 = "Test text with ![Image flavour text](www.someimagehostingsite.com)"
teststring2 = "Test text without an image"
teststring3 = "Random text with exclamation ! and some parentheses (test) to check."
teststring4 = "Test text with [link flavour text](www.somerandomsite.com)"
teststring5 = "Random text with only [stuff] and some parentheses (test) to check."
teststring6 = "[Incomplete link] and missing the URL part"
teststring7 = "A text with multiple images ![This is a good image](www.goodimagesite.com) and ![This is a bad image](www.badimagesite.com)"
teststring8 = "A text with multiple links [This is a fun link](www.funsite.com) and [This is a boring link](www.boringsite.com)"

#First section tests image extraction by looking for ![ and then ](
class TestExtractImage(unittest.TestCase):

    def test_extract_image_correct_text(self):
        node1 = [('Image flavour text', 'www.someimagehostingsite.com')]
        self.assertEqual(node1, extract_markdown_images(teststring1))

    def test_extract_image_incorrect_function(self):
        node1 = []
        self.assertEqual(node1, extract_markdown_images(teststring4))
        self.assertEqual(node1, extract_markdown_images(teststring6))

    def test_extract_image_incorrect_text(self):
        node1 = [('Image flavour text', 'www.someimagehostingsite.com')]
        self.assertNotEqual(node1, extract_markdown_images(teststring4))
        self.assertNotEqual(node1, extract_markdown_images(teststring5))
        self.assertNotEqual(node1, extract_markdown_images(teststring2))
        self.assertNotEqual(node1, extract_markdown_images(teststring3))
        self.assertNotEqual(node1, extract_markdown_images(teststring6))

    def test_extract_image_multiple_entries(self):
        node1 = [('This is a good image', 'www.goodimagesite.com'), ('This is a bad image', 'www.badimagesite.com')]
        self.assertEqual(node1, extract_markdown_images(teststring7))




#Second section tests link extraction by looking for [ and then ](
class TestExtractLink(unittest.TestCase):

    def test_extract_link_correct_text(self):
        node1 = [('link flavour text', 'www.somerandomsite.com')]
        self.assertEqual(node1, extract_markdown_links(teststring4))
         
    def test_extract_link_incorrect_function(self):
        node1 = []
        self.assertEqual(node1, extract_markdown_links(teststring1))     
        self.assertEqual(node1, extract_markdown_images(teststring3))

    def test_extract_link_incorrect_text(self):
        node1 = [('Link flavour text', 'www.somerandomsite.com')]
        self.assertNotEqual(node1, extract_markdown_links(teststring1))
        self.assertNotEqual(node1, extract_markdown_links(teststring5))
        self.assertNotEqual(node1, extract_markdown_links(teststring2))   
        self.assertNotEqual(node1, extract_markdown_links(teststring3))
        self.assertNotEqual(node1, extract_markdown_links(teststring6))

    def test_extract_link_multiple_entries(self):
        node1 = [('This is a fun link', 'www.funsite.com'), ('This is a boring link', 'www.boringsite.com')]
        self.assertEqual(node1, extract_markdown_links(teststring8))



if __name__ == "__main__":
    unittest.main()