def word_count(text):
    count = text.split()
    return len(count)

def char_count(text):
    char_dict = {}

    for char in text:
        lowered = char.lower()

        if lowered not in char_dict:
            char_dict[lowered] = 1

        else:
            char_dict[lowered] += 1

    return char_dict

def sort_dict(dict):

    sorted_list = []

    #Transform dictionary into a list of dictionaries
    for char, count in dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def sort_on(dict):
    return dict["num"]
