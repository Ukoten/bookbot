from stats import get_num_words
from stats import get_count_char
from stats import sort_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    text=get_book_text("books/frankenstein.txt")
    wordnr=get_num_words(text)
    print("Found {} total words".format(wordnr))
    char_list=get_count_char(text)
    char_list=sort_list(char_list)
    for entry in char_list:
        print(entry["char"]+":",entry["num"])
main()