def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    text = text.lower()
    dictionary = {}

    for letter in text:        
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    return dictionary

if __name__ == "__main__":
    print(get_num_characters("Hello my friend! I am counting characters."))