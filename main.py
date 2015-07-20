import time
import re
import itertools
import operator

def problem(word, offensive):
    new_word = ""
    idx = 0
    for ch in word:
        if ch in offensive[idx:]:
            new_word += ch
    return new_word == offensive

def create_word_list(length):
    sigma = list('abcdefghijklmnopqrstuvwxyz')
    return [''.join(i) for i in itertools.product(sigma, repeat=length)]

def chunk(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

def find_max_problem_count():
    words = create_word_list(5)
    num_procs = 10
    counts = {}

    for word in words:
        counts[word] = 0

    # TODO: Going to break the word list into k parts and pass these parts to
    # their own thread to try and get some better performance.
    #chunks = chunk(words, num_procs)

    for line in open('one-word.txt').read().split():
        print str(time.ctime())
        for word in words:
            if problem(line, word):
                counts[word] += 1
        print str(time.ctime())

    return sorted(counts.items(), key=operator.itemgetter(1))[-10:]

#tops = find_max_problem_count()
#while bool(tops):
    #print tops.pop()
