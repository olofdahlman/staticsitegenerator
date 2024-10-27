#This file contains the functions that generate/regenerate directories and files in the home directory, being called mainly from main
#This file has no unit tests since it regenerates directories and files in the temporary public directory, rather than running internaly - is tested by checking the print outputs
from markdown_to_html_node import markdown_to_html_node
from extract_things_fromtext import extract_title
import shutil, os

def regenerate_public():
    path_public = r'./public'
    path_static = r'./static'

    if os.path.exists(path_public):
        print("Public directory exists, deleting...")
        shutil.rmtree(path_public)
     
    print("Copying files from static to public directory")
    log = []

    return copy_static_to_public(path_static, path_public, log)

def copy_static_to_public(static, public, logger):
    #This function returns a log of paths of each copy for tracking purposes, while copying the contents of static to public
    if not os.path.exists(public):
        os.mkdir(public)
    for entry in os.listdir(static):   #Scans the source directory, in this case the static directory for all entries
        entry_path = os.path.join(static, entry)
        destination_path = os.path.join(public, entry)
        if os.path.isfile(entry_path):
            logger.append(shutil.copy(entry_path, destination_path))
        else:
            copy_static_to_public(entry_path, destination_path, logger)

    return logger

def generate_page(from_path, template_path, dest_path):
    print(f"Generating webpage from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as file:
        content = file.read()
    with open(template_path) as file:
        template = file.read()

    markdown_to_html_content = markdown_to_html_node(content)
    html_content = markdown_to_html_content.to_html()
    page_title = extract_title(content)

    template_title = template.replace(r'{{ Title }}', page_title)
    final_html_page = template_title.replace(r'{{ Content }}', html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    html_file_path = os.path.join(dest_path, 'index.html')
    with open(html_file_path, 'w') as file:
        file.write(final_html_page)
    
    return "Generated index.html content document for webpage"