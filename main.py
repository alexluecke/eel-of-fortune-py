import re

def problem(word, offensive):
    char_list = set(offensive)
    regex_pattern = "[^" + "".join(char_list) + "]+"
    new_word = []

    for ch in list(word):
        if ch in char_list:
            new_word.append(ch)

    if "".join(new_word) == offensive:
        return True
    else:
        return False

max_count = 0
with open('enable.txt') as f:
    for line in f:
        if problem(line, 'snond'):
            count += 1

print count
