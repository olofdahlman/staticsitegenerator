#Overarching function to employ textnode, inline_markdown and extract_links_fromtext to turn raw markdown into a list of textnodes of each inline text type
import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)
from inline_markdown import (
    split_nodes_delimiter, 
    split_nodes_image, 
    split_nodes_link
)
regex_error_pattern = (r"(\*{3,})")
delimiter_dict = {"**":text_type_bold, "*":text_type_italic, "`":text_type_code}
#Delimiter dict with bold, italic and code formatting characters

def text_to_textnode(rawtext):
    if not (re.findall(regex_error_pattern, rawtext)) == []: #Basic check to ensure there isn't more than two * in a row, because this would cause errors with the text extraction functions
        raise Exception("3 or more asterisks in a row, please separate bolded and italic parts by a space and use asterisks for nothing else")
    text = TextNode(rawtext, text_type_text)
    textnode_list = [text]
    for delimiter, text_type in delimiter_dict.items():
        textnode_templist = split_nodes_delimiter(textnode_list, delimiter, text_type)
        textnode_list = textnode_templist
    
    textnode_templist = split_nodes_image(textnode_list)
    textnode_list = textnode_templist
    textnode_templist = split_nodes_link(textnode_list)
    textnode_list = textnode_templist
    return textnode_list


    



