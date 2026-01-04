from stats import word_count, char_count, sort_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)
    sorted_dicts = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in sorted_dicts:
        char = dict["char"]
        count = dict["num"]

        print(f"{char}: {count}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
