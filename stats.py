def sort_on(words):
    return words["num"]

def count_words(content):
    num_words = len(content.split())
    return num_words

def count_chars(content):
    char_count = {}
    char_list = []

    for char in content:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1

    for key, value in char_count.items():
        # print(f"key: {key}, value: {value}");
        char_list.append({ "char": key, "num": value })

    char_list.sort(reverse=True, key=sort_on)
    return char_list
