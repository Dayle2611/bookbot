from stats import get_num_words
from stats import get_unique_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    bookAsString = get_book_text("./books/frankenstein.txt")
    wordCount = get_num_words(bookAsString)
    print(f'{wordCount} words found in the document')

if __name__=="__main__":
    main()