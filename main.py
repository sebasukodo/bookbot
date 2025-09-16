def get_book_text(filepath):
    with open(filepath) as path:
        return path.read()

def number_of_words_in_string(text):
    return len(text.split())

def main():
    num_words = number_of_words_in_string(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()