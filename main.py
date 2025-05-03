from stats import *
import sys

def main():
    # kontrola argumentů příkazového řádku
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # přiřazení argumentu příkazového řádku k proměnné
    path = sys.argv[1]
    # prirazeni obsahu souboru do proměnné
    text = get_book_text(path)
    # zavolání funkcí pro počítání slov a znaků
    result_counter = word_counter(text)
    # zavolání funkce pro počítání znaků
    char_counter = character_counter(text)
    # zavolání funkce pro seřazení znaků podle počtu
    sorted_char_count = get_sorted_list(char_counter)
    # vypsání výsledků
    print(f"Found {result_counter} total words")
    # vypsání počtu znaků
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

# funkce pro otevření souboru a načtení textu
def get_book_text(path):
    with open (path) as f:
        file_contents = f.read()
        return file_contents


main()