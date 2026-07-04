from resources.generate_page import generate_page
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
    for root, dirs, files in os.walk("./content"):
        for file in files:
            if file.endswith(".md"):
              from_path = os.path.join(root, file)
              to_path = from_path.replace("./content", "./public").replace(".md", ".html")
              generate_page(from_path, "./template.html", to_path)
    return

if __name__ == "__main__":
    main()
