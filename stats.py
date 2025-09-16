def sort_on(items):
    return items["num"]

def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    text = text.lower()
    dictionary = {}

    for letter in text:        
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    return dictionary

def get_sorted_character_count(dictionary):
    sorted_list = []

    for element in dictionary:
        sorted_list.append({
            "char": element,
            "num" : dictionary[element]
        })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

if __name__ == "__main__":
    dictionary = get_character_count("Hello my friend! I am counting characters.")
    print(get_sorted_character_count(dictionary))