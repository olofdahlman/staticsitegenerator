#This code returns tuples with links or images/imagelinks separated from the text supplied to it
import re

def extract_markdown_images(rawtext):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", rawtext)


def extract_markdown_links(rawtext):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)" , rawtext)