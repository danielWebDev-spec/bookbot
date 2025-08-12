
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_num_words(text):
    num_words = len(text.split())
    return f"{num_words} words found in the document"
    
    
def main():
    text = get_book_text("books/frankenstein.txt")
    print(get_num_words(text))

main()

