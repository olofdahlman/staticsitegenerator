This is a simple training project as a part of the bootdev online course, aimed at making a static site generator.

Content in here is likely not of any particular interest, but you are free to use the code at your own discretion though without responsibility or guarantee on my part.
 
The code is functional and converts markdown files into html files and launches these with a template html file and any images.
Markdown files are stored in the contents directory - this directory is scanned for either folders or files, but can only process .md (markdown) files - 
do not add other file types to this directory, for the code will likely not be able to process them.

Images and other non-markdown stuff goes in the static directory, which is copied directly into the public directory upon code activation. 
These contents are not processed beyond copying, so file compatability is higher here, though if you wish to use the contents in webpage generation it needs to be compatible with html.

