import sys
from stats import (
    num_words,
    character_count,
    make_report
)
def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        contents = f.read()
    return contents



def main():
    if len(sys.argv)!= 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    word_count = num_words(contents)
    # print(f'{word_count} words found in the document')
    # print(character_count(contents))
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
""",end = "")
    for item in make_report(character_count(contents)):
        if item['char'].isalpha():
            print(f'{item['char']}: {item['num']}')
    print("============= END ===============",end="")



main()
