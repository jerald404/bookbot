import string


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    list_dicc = [{'name': clave, 'num': valor} for clave, valor in count_chars(text).items()]
    list_dicc.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    print()
    for dicc in list_dicc:
        print(f"The {dicc['name']} character was found {dicc['num']} times")
    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_chars(text):
    dicc = {letra: 0 for letra in string.ascii_lowercase}
    for char in text.lower():
        if char in dicc:
            dicc[char] += 1
    return dicc


def sort_on(dict):
    return dict["num"]





main()
