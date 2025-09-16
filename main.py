import sys
from stats import get_num_words, get_character_count, get_sorted_character_count


def get_book_text(filepath):
    with open(filepath) as path:
        return path.read()

def print_stats(filepath):
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_characters = get_character_count(text)
    character_count = get_sorted_character_count(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for element in character_count:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    print_stats(sys.argv[1])

main()