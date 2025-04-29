from stats import word_counter


def get_book_text(path):
    with open (path) as f:
        file_contents = f.read()
        return file_contents

def main():
    result = get_book_text("books/frankenstein.txt")
    result_counter = word_counter(result)
    print(f"{result_counter} words found in the document")

main()