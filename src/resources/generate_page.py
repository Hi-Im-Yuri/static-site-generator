from .markdown_to_html import markdown_to_html
from .extract_title import extract_title
import os


def generate_page(from_path: str, template_path: str, dest_path: str, base_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as c:
        content = c.read()
    with open(template_path, "r") as t:
        template = t.read()
    resultHTML = markdown_to_html(content).to_html()
    title = extract_title(content)
    new_page = template.replace("{{ Title }}", title)
    new_page = new_page.replace("{{ Content }}", resultHTML)
    new_page = new_page.replace("href=\"/", f"href={base_path}")
    new_page = new_page.replace("src=\"/", f"src={base_path}")
    destination_folder = os.path.dirname(dest_path)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    with open(dest_path, "w") as f:
        f.write(new_page)
