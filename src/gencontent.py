from block_markdown import markdown_to_blocks, markdown_to_html_node
import os
from pathlib import Path

def extract_title(markdown):
    h1_title = markdown_to_blocks(markdown)[0]
    if h1_title.startswith("# "):
        return h1_title[2:].strip()
    else:
        raise Exception("The markdown doc does not start with '# '")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    md = read_file(from_path)
    template = read_file(template_path)

    nodes = markdown_to_html_node(md)
    html = nodes.to_html()
    title = extract_title(md)

    content = template.replace("{{ Title }}", title)
    content = content.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    dest_file = open(dest_path, 'w', encoding="utf-8")
    dest_file.write(content)

def read_file(file_path):
    file = open(file_path, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    return file_data

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
