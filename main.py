from __future__ import print_function
import threading
import time
import re
import itertools
import operator

result = {}
lock = threading.Lock()

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

        global lock
        global result

        for word in self.offensives:
            self.counts[word] = 0

        start_time = time.time()
        print("Starting[" + self.getName() + "]")
        for line in self.dictionary:
            for word in self.offensives:
                if problem(line, word):
                    lock.acquire()
                    try:
                        self.counts[word] += 1
                    finally:
                        lock.release() # release lock, no matter what.

        end_time = time.time()
        print("Ending[" + self.getName() + "]: " + self.time_delta(start_time, end_time))

        lock.acquire()
        try:
            culled = dict((k,v) for k, v in self.counts.iteritems() if v > 0)
            for (key,value) in culled.iteritems():
                result[key] = value
        finally:
            lock.release() # release lock, no matter what.

    def time_delta(self, start, end):
        hours, rem = divmod(end-start, 3600)
        minutes, seconds = divmod(rem, 60)
        return "Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(
            int(hours)
            , int(minutes)
            , seconds
        )

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
    counts = {}
    num_procs = 10
    upper_bound = 0
    lower_bound = 0

    dict_words = open('enable.txt').read().split()[1489:1490]

    jobs = []
    for i in range(num_procs):
        # Split up the data:
        step = len(offensives)/num_procs
        upper_bound = min(len(offensives), i*step + step)
        if i < num_procs-1:
            jobs.append(ThreadedProblem(dict_words, offensives[lower_bound:upper_bound]))
        else: # Make sure we pass the remaining words to the last process
            jobs.append(ThreadedProblem(dict_words, offensives[lower_bound:]))
        lower_bound = upper_bound + 1

    for job in jobs:
        job.start()

    while threading.active_count() > 1:
        for job in jobs:
            job.join(1)

    #return sorted(counts.items(), key=operator.itemgetter(1))[-10:]

find_max_problem_count()
lock.acquire()
try:
    result
    print(sorted(result.items(), key=operator.itemgetter(1))[-10:])
finally:
    lock.release() # release lock, no matter what.

#tops = find_max_problem_count()
#while bool(tops):
    #print tops.pop()
