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
