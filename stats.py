def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

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

    return letter_counts

