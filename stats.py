import string

def get_num_words(text):
    num_words = len(text.split())
    return f"{num_words} words found in the document"

def count_char_occurrences(book):
    # start with empty dictionary
    letter_counts = {}

    # go through each character
    for char in book:
        if char.isalpha(): # check if it's a letter
            char_lower = char.lower() # make lowercase 
            if char_lower in letter_counts:
                letter_counts[char_lower] += 1
            else:
                letter_counts[char_lower] = 1 # first time seeing this letter

    # alphabetical order
    sorted_counts = dict(sorted(letter_counts.items()))

    return sorted_counts

