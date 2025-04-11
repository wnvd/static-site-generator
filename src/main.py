from textnode import TextNode, TextType
from gencontent import extract_title, generate_page
from copy_static import copy_static

def genereate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    pass


def main():

    copy_static("static/", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty.html")
    generate_page("content/contact/index.md", "template.html", "public/contact.html")

if __name__ == "__main__":
    main()

