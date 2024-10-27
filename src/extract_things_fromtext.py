#This code returns tuples with links or images/imagelinks separated from the text supplied to it
#Renamed with this name to add extract_title to store functions in a more sensible way
import re

def extract_markdown_images(rawtext):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", rawtext)


def extract_markdown_links(rawtext):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)" , rawtext)

def extract_title(markdown):
    lines = markdown.split('\n')
    h1_regex_pattern = (r"(^#(?!#))")
    for line in lines:
        if re.findall(h1_regex_pattern, line):
            return line.replace('# ', '')
        
    raise Exception("No h1 title found in markdown string")