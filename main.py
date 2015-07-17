import re
import itertools

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


def create_word_list(length):
    sigma = list('abcdefghijklmnopqrstuvwxyz')
    words = [''.join(i) for i in itertools.product(sigma, repeat=length)]

def find_max_problem_count():
    words = create_word_list(5)
    counts = []
    with open('enable.txt') as f:
        for line in f:
            if problem(line, 'snond'):
                max_count += 1

    print max_count

find_max_problem_count();
