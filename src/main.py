# Use ./main.sh to run from terminal
#Uses functions from other files to construct the required home directories/files from repositories like static to generate the webpage from content and style files
#print("hello world")

from textnode import TextNode
from generated_directories import regenerate_public, generate_page

def main():
    log = regenerate_public()
    print(f"Log of copies generated: {log}")
    source_path = './content/index.md'
    template_path = './template.html'
    destination_path = './public'

    html_log = generate_page(source_path, template_path, destination_path)
    print(html_log)


if __name__ == "__main__":
    main()