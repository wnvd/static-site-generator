from textnode import TextNode, TextType
from gencontent import extract_title, generate_page
import os, shutil

def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item) 
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} to {dst_path}")
        else:
            copy_static(src_path, dst_path)

def main():

    copy_static("static/", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty.html")
    generate_page("content/contact/index.md", "template.html", "public/contact.html")

if __name__ == "__main__":
    main()

