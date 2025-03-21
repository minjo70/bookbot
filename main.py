from stats import count_text_words, count_letters, sorted_charcount
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

script, book = sys.argv

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    file_contents = get_book_text(book)
    letter_count = count_letters(file_contents)
    sorted_count = sorted_charcount(letter_count)

    print('========== BOOKBOT ==========')
    print(f'Analyzing book found at {book}...')
    print('--------- Word Count --------')
    print(f'Found {count_text_words(file_contents)} total words')
    print('------- Character Count -----')
    for item in sorted_count:
        char = item['char']
        if char.isalpha():
            print(f"{char}: {item['count']}")
    print('============ END ============')

main()
