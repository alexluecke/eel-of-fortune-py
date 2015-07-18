import time
import re
import itertools
import operator

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
    return [''.join(i) for i in itertools.product(sigma, repeat=length)]

def find_max_problem_count():
    words = create_word_list(5)
    counts = {}

    for word in words:
        counts[word] = 0

    with open('one-word.txt') as f:
        for line in f:
            print str(time.ctime())
            for word in words:
                if problem(line, word):
                    counts[word] += 1
            print str(time.ctime())


    ordered = sorted(counts.items(), key=operator.itemgetter(1))
    return ordered[-10:]


tops = find_max_problem_count()
while bool(tops):
    print tops.pop()

