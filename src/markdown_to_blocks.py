#Code to handle the blocks of the markdown text supplied - the inline_markdown handles the contents of each block


def markdown_to_blocks(markdowntext):
    string_list = markdowntext.split("\n")
    clean_list = []
    for string in string_list:
        string_stripped = string.strip()
        if not string_stripped:
            continue
        clean_list.append(string_stripped)

    #This code splits the lists at each newline, and it is assumed that only proper markdown blocks with one newline between each is in the markdowntext
    #It also does not append empty entries

    return clean_list

def block_to_block_type(markdowntext):
    pass #Add stuff here to identify block types