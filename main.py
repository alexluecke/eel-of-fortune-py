from __future__ import print_function
import threading
import time
import re
import itertools
import operator

class ThreadedProblem(threading.Thread):
    counts = {}
    dictionary = None
    offensives = None

    def __init__(self, dw, ow):
        threading.Thread.__init__(self)
        self.dictionary = dw
        self.offensives = ow

    def run(self):
        self.problem()

    def problem(self):

        for word in self.offensives:
            self.counts[word] = 0

        print("Starting[" + self.getName() + "]: " + time.ctime())
        for line in self.dictionary:
            for word in self.offensives:
                if problem(line, word):
                    self.counts[word] += 1
        print("Ending[" + self.getName() + "]: " + time.ctime())

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
    offensives = create_word_list(5)
    num_procs = 10
    counts = {}

    dict_words = open('enable.txt').read().split()[:5]

    lower_bound = 0
    for i in range(num_procs):
        # Split up the data:
        step = len(offensives)/num_procs
        upper_bound = min(len(offensives), i*step + step)
        #print("Giving (" + str(i) + ") range (" + str(lower_bound) + ":" + str(upper_bound) + ")")
        if i < num_procs-1:
            t = ThreadedProblem(dict_words, offensives[lower_bound:upper_bound])
        else: # Make sure we pass the remaining words to the last process
            t = ThreadedProblem(dict_words, offensives[lower_bound:])
        t.start()
        lower_bound = upper_bound + 1

    #return sorted(counts.items(), key=operator.itemgetter(1))[-10:]

find_max_problem_count()
#tops = find_max_problem_count()
#while bool(tops):
    #print tops.pop()
