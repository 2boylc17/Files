def cwd():
    import os
    path = os.getcwd()
    print(f"Current Working Directory: {path}")
    print(f"The directory contains the following files")
    for file in os.listdir(path):
        print(file)


def display_chars(filepath, chars):
    with open(filepath) as file:
        partial_data = file.read(chars)
        print(partial_data)


def display_line(filepath):
    with open(filepath) as file:
        line = file.readline().strip()
        print(line)


def display_text(filepath):
    with open(filepath) as file:
        filetext = file.read()
        print(filetext)


def run_task2():
    print("-----")
    display_chars("library.txt", 5)
    print("-----")
    display_line("library.txt")
    print("-----")
    display_text("library.txt")
    print("-----")


def search(filepath):
    print(f"Searching...")
    with open(filepath) as file:
        for line in file:
            text = file.readline().strip()
            print(f"Looked in {text}")


search("library.txt")
