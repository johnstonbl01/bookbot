import sys
from stats import count_words, count_chars

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    char_count = count_chars(book_content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
