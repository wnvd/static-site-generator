from block_markdown import markdown_to_blocks, markdown_to_html_node

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

    dest_file = open(dest_path, 'w', encoding="utf-8")
    dest_file.write(content)

def read_file(file_path):
    file = open(file_path, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    return file_data

