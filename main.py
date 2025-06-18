from stats import word_count, character_count, list_sorting
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    # path = 'books/frankenstein.txt'
    book = get_book_text(path)
    total_words = word_count(book)
    character_total = character_count(book)
    sorted_characters = list_sorting(character_total)
    print(book)
    print(f'{total_words} words found in the document.')
    print(character_total)
    # for char, count in character_total.items():
    #     # Show characters like newline, space, etc. clearly
    #     if char == ' ':
    #         display_char = "' ' (space)"
    #     elif char == '\n':
    #         display_char = "'\\n' (newline)"
    #     elif char == '\t':
    #         display_char = "'\\t' (tab)"
    #     else:
    #         display_char = f"'{char}'"
    #     print(f"{display_char}: {count}")
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        char = item["char"]
        count = item["num"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    print("============= END ==============")



def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


if __name__ == '__main__':
    main()