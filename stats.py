def get_num_words(file_contents):
    return len(file_contents.split())

def get_num_chars(file_contents):
    num_chars = {}
    for char in file_contents.lower():
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars



def sort_on(items):
    return items["num"]

def get_sorted_list_chars(num_chars):
    list_chars = []
    for item in num_chars:
        char_num = {"char": item, "num": num_chars[item]}
        list_chars.append(char_num)
    list_chars.sort(reverse=True, key=sort_on)
    return list_chars
