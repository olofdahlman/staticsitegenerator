# Use ./main.sh to run from terminal
#print("hello world")
from textnode import TextNode
import os, shutil

def main():
    log = regenerate_public()
    print(f"Log of copies generated: {log}")

def regenerate_public():
    path_public = r'./public'
    path_static = r'./static'

    if os.path.exists(path_public):
        print("Public directory exists, deleting...")
        shutil.rmtree(path_public)
     
    print("Printing files from static to public directory")
    log = []

    return copy_static_to_public(path_static, path_public, log)

def copy_static_to_public(static, public, logger):
    #This function returns a log of paths of each copy for tracking purposes, while copying the contents of static to public
    if not os.path.exists(public):
        os.mkdir(public)
    for entry in os.listdir(static):   #Scans the source directory, in this case the static directory for all entries
        entry_path = os.path.join(static, entry)
        destination_dir = os.path.join(public, entry)
        if os.path.isfile(entry_path):
            logger.append(shutil.copy(entry_path, destination_dir))
        else:
            copy_static_to_public(entry_path, destination_dir, logger)

    return logger


if __name__ == "__main__":
    main()
#main()