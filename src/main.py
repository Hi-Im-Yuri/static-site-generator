from resources.generate_page import generate_page
import os
import shutil
import sys


## moves files from source directory to destination directory
def move_files(source: str, dest: str) -> None:
    if not os.path.exists(source):
        raise Exception("Source directory does not exist")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    copy_files(source, dest)


## helper function for move_files that recursively copies and
## copies files from a source directory to the target.
def copy_files(source: str, dest: str) -> None:
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
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    source = "./static"
    destination = "./docs"
    move_files(source, destination)
    for root, _, files in os.walk("./content"):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                to_path = from_path.replace("./content", "./docs").replace(
                    ".md", ".html"
                )
                generate_page(from_path, "./template.html", to_path, base_path)
    return


if __name__ == "__main__":
    main()
