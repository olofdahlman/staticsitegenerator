#Unittest for the extract links/images functions
import unittest, re
from extract_things_fromtext import extract_markdown_images, extract_markdown_links, extract_title

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

#Third section checks for '#' but excludes '##' in order to extract h1 titles (main header). Does not check for '###' or larger since finding '##' already prevents this and '# #' also does not match
class   TextExtractTitle(unittest.TestCase):    
    def test_extract_title_simple(self):
        node1 = "# This is a simple h1 (title) header"
        node2 = "# Another simple h1 title header"
        outcome1 = "This is a simple h1 (title) header"
        outcome2 = "Another simple h1 title header"
        self.assertEqual(extract_title(node1), outcome1)
        self.assertEqual(extract_title(node2), outcome2)

    def test_extract_title_paragraph(self):
        node1 = """# This is a short string with this h1 title

It also has a second paragraph
with some largely pointless text"""
        node2 = """# This is another h1

With a second shorter paragraph"""

        outcome1 = "This is a short string with this h1 title"
        outcome2 = "This is another h1"
        self.assertEqual(extract_title(node1), outcome1)
        self.assertEqual(extract_title(node2), outcome2)
    
    def test_extract_title_improper_placement(self):
        node1 = """This is another document
# Where the h1 title is improperly placed on line 2"""
#Normally this is improper title placement in this context, but the code currently only finds the h1 syntax, nothing else
        outcome1 = "Where the h1 title is improperly placed on line 2"
        self.assertEqual(extract_title(node1), outcome1)

    def test_extract_title_multiple_h1(self):
        node1 = """# This is the first h1 in this text
# This is the second one, it should not be returned"""   #The function returns the first h1 found - the second is never processed since the function call is terminated before
        outcome1 = "This is the first h1 in this text"
        self.assertEqual(extract_title(node1), outcome1)

    def test_extract_title_no_h1_error(self):   #The node1 string is supposed to raise the exception in outcome1 since the function needs atleast one h1 to be found
        node1 = "This is a short text without any h1 tag"
        outcome1 = "No h1 title found in markdown string"
        with self.assertRaises(Exception) as context:
            block1 = extract_title(node1)
        self.assertEqual(str(context.exception), outcome1)


if __name__ == "__main__":
    unittest.main()