#Code to handle the blocks of the markdown text supplied - the inline_markdown handles the contents of each block
import re

def markdown_to_blocks(markdowntext):
    string_list = markdowntext.split("\n\n")
    clean_list = []
    for string in string_list:
        if not string:
            continue
        string_stripped = string.strip()
        clean_list.append(string_stripped)

    #This code splits the lists at each double newline - this is important, each string will have a newline at the end, then it MUST also have a second newline to denote an empty line
    #If it's just one newline, it's assumed to be the same block of strings still, and more than 2 is not accepted in our syntax - this code cannot handle that
    #It also does not append empty entries

    return clean_list

def block_to_block_type(markdowntext):
    #Returns the type of block of a markdown block - it is not supposed to consider inline type text
    #These patterns capture any instance of the corresponding formatting characters - it relies on there only being one in each block!
    #If there are more than one pattern match per block, the block splitting function is failing or this code needs to be updated to handle multiple types somehow
    #But the intended function of this is only to return a type, which should not be multiple things
    heading_pattern = (r"^(\#{1,6}\s{1})")   #This regex expression finds 1-6 hashtags followed by one whitespace - whitespace can be newlines and other things, so be wary of this
    code_pattern = (r"^(\`{3})(.*?)(\`{3})$")
    qoute_pattern = (r"^(\>)")
    unordered_list_pattern = (r"^([*-]\s{1}\S)") #This code matches either a * or a - character followed by a whitespace (can be newline and others!) followed by a non-whitespace character
    ordered_list_pattern = (r"^(\d\.\s{1}\S)")
    ordered_list_pattern_number = (r"^(\d)")  

    if not type(markdowntext) == str:
        raise Exception("Error: block_to_block_type only accepts string inputs")
    
    split_string = markdowntext.split("\n")  

    if not (re.findall( heading_pattern, markdowntext)) == []:
        return "Heading"
    if not (re.findall(code_pattern, markdowntext)) == []:
        return "Code"

    regex_result_list = []  
    for string in split_string:    
        if not (re.findall(qoute_pattern, string)) == []:
            regex_result_list.append(True)
        else:
            regex_result_list.append(False)
    if not False in regex_result_list:
        return "Quote"
    
    regex_result_list = []  #Function needs to be able to handle multiline lists, I didn't know how to do that with regex alone
    for string in split_string:    #By using a list and storing evaluated true/false statements, I can have have the code check so that each line matches the unordered list format
        regex_result_list.append(not (re.findall(unordered_list_pattern, string)) == []) #This statement appends the direct outcome of the check, True or False, simplifying
    if not False in regex_result_list:
        return "Unordered_list"
    
    regex_result_list = []
    list_number = 1
    for string in split_string:
        match = re.match(ordered_list_pattern, string)
        match_number = re.match(ordered_list_pattern_number, string)
        if match:
            line_number = int(match_number.group())  # Capture the number part
            if line_number == list_number:
                 regex_result_list.append(True)
                 list_number += 1
            else:
                regex_result_list.append(False)
        else:
            regex_result_list.append(False)
    if not False in regex_result_list:
        return "Ordered_list"
    
    else:
        return ("Paragraph")