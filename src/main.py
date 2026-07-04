from markdown_to_html import markdown_to_html
from htmlnode import HTMLNode
from parentnode import ParentNode
import os, shutil

def move_files(source: str, dest: str) -> None:
    if not os.path.exists(source):
        raise Exception("Source directory does not exist")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    copy_files(source, dest)


def copy_files(source: str, dest:str) -> None:
    current_entry = os.listdir(source)
    if not current_entry:
        return
    for entry in current_entry:
        current = os.path.join(source, entry)
        new_destination = os.path.join(dest, entry)
        if not os.path.isfile(current):
            if not os.path.exists(new_destination):
                os.makedirs(new_destination)
            copy_files(current, new_destination)
        else:
            shutil.copy(current, new_destination)
    return


def main():
    source = "./static"
    destination = "./public"
    move_files(source, destination)
    return






if __name__ == "__main__":
    main()
