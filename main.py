from stats import *

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    result_counter = word_counter(text)
    char_counter = character_counter(text)
    print(f"{result_counter} words found in the document")
    print(char_counter)


def get_book_text(path):
    with open (path) as f:
        file_contents = f.read()
        return file_contents


main()