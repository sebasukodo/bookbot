from stats import get_num_words, get_num_characters

def get_book_text(filepath):
    with open(filepath) as path:
        return path.read()

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein)
    num_characters = get_num_characters(frankenstein)
    print(f"{num_words} words found in the document")
    print(num_characters)

main()