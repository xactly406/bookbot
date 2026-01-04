from stats import word_count, char_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)

    print(f"Found {num_words} total words")
    print(num_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
