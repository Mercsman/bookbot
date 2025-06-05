from stats import word_count, character_count


def main():
    path = 'books/frankenstein.txt'
    book = get_book_text(path)
    total_words = word_count(book)
    character_total = character_count(book)
    # print(book)
    # print(f'{total_words} words found in the document.')
    print(character_total)
    for char, count in character_total.items():
        # Show characters like newline, space, etc. clearly
        if char == ' ':
            display_char = "' ' (space)"
        elif char == '\n':
            display_char = "'\\n' (newline)"
        elif char == '\t':
            display_char = "'\\t' (tab)"
        else:
            display_char = f"'{char}'"
        print(f"{display_char}: {count}")



def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


if __name__ == '__main__':
    main()