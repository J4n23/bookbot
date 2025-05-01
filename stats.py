def word_counter(text):
    words = text.split()
    return len(words)


def character_counter(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def get_sorted_list(char_dict):
    # Vytvoreni listu tuples z char_dict a seřazení podle hodnoty
    sorted_items = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    # Vytvoreni listu slovniku s klíči "char" a "num" s hodnotamy z char_dict
    result = [{"char": char, "num": count} for char, count in sorted_items]
    return result