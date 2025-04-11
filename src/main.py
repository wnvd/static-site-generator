from textnode import TextNode, TextType
import os
from gencontent import (
    extract_title,
    generate_page,
    generate_pages_recursive,
)

from copy_static import copy_static

DIR_PATH_STATIC = "static/"
DIR_PATH_PUBLIC = "public/"
DIR_PATH_CONTENT = "content/"
TEMPLATE_PATH = "template.html"


def main():

    copy_static(DIR_PATH_STATIC, DIR_PATH_PUBLIC)
    print("Generating pages...")
    generate_pages_recursive(
        DIR_PATH_CONTENT,
        TEMPLATE_PATH,
        DIR_PATH_PUBLIC,
    )

if __name__ == "__main__":
    main()

