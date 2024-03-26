#!/usr/bin/env python3
def main():
    books = ["books/frankenstein.txt"]
    for book_path in books:
        print(f"--- Begin report of {book_path} ---")
        text = get_book_text(book_path)
        word_count = count_words(text)
        print(f"{word_count} words found in the document\n")

        letter_count = sorted_count_letters(text)
        for ch, count in letter_count.items():
            print(f"The '{ch}' character was found {count} times")

        print("--- End report ---")
        
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def sorted_count_letters(book_text):
    unsorted = count_letters(book_text)
    result = {ch: count for ch, count in sorted(unsorted.items(), key=lambda ele: ele[1], reverse=True)}
    return result

def count_letters(book_text):
    result = {}
    for word in book_text.lower().split():
        for letter in word:
            if not letter.isalpha():
                continue
            if letter not in result:
                result[letter] = 0
                
            result[letter] += 1
    return result

def letter_count_sorter(letter_count_result):
    print(letter_count_result)
    return letter_count_result["count"]

main()