from stats import *

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    #text = "Ahoj, tohle ..."
    result_counter = word_counter(text)
    char_counter = character_counter(text)
    sorted_char_count = get_sorted_list(char_counter)
    print(f"Found {result_counter} total words")
    #print(sorted_char_count)
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

def get_book_text(path):
    with open (path) as f:
        file_contents = f.read()
        return file_contents


main()