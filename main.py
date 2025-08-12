import sys
from stats import get_num_words, count_char_occurrences


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def sorted_list_of_dict(my_dict):
    sorted_list = []

    def sort_on(items):
        return items["num"]

    for key, value in my_dict.items():
        sorted_list.append({"char": key, "num": value })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

    
def print_stats(my_list):
    for item in my_list:
        print(f"{item["char"]}: {item["num"]}") 
    
def main():
     if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

     else:
        book_path = sys.argv[1]  # Get path from command line
    
        text = get_book_text(book_path)
        
        char_count = count_char_occurrences(text)
        sorted_list = sorted_list_of_dict(char_count)
    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(get_num_words(text))
        print("--------- Character Count -------")
        print_stats(sorted_list)

main()

