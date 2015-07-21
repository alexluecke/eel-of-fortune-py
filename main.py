from __future__ import print_function
import threading
import time
import re
import itertools
import operator

result = {}
lock = threading.Lock()

class ThreadedProblem(threading.Thread):
    dictionary = None
    offensives = None
    ID = 0

    def __init__(self, ID, dw, ow):
        threading.Thread.__init__(self)
        self.dictionary = dw
        self.offensives = ow
        self.ID = ID

    def run(self):
        self.check_words()

    def check_words(self):

        global lock
        global result

        this_count = {}

        for word in self.offensives:
            this_count[word] = 0

        start_time = time.time()
        print("Starting[" + self.getName() + "]")
        for line in self.dictionary:
            for word in self.offensives:
                if problem(line, word):
                    this_count[word] += 1
        end_time = time.time()
        print("Ending[" + self.getName() + "]: " + time_delta(start_time, end_time))

        culled = dict((k,v) for k, v in this_count.iteritems() if v > 0)

        lock.acquire()
        try:
            for (key,value) in culled.iteritems():
                result[key] = value
        finally:
            lock.release() # release lock, no matter what.

def time_delta(start, end):
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    return "Elapsed: {:0>2}:{:0>2}:{:05.2f}".format(
        int(hours)
        , int(minutes)
        , seconds
    )

def problem(word, offensive):
    new_word = ""
    for ch in word:
        if ch in offensive:
            new_word += ch
    return new_word == offensive

def create_word_list(length):
    sigma = list('abcdefghijklmnopqrstuvwxyz')
    return [''.join(i) for i in itertools.product(sigma, repeat=length)]

def find_max_problem_count():
    offensives = create_word_list(5)
    num_procs, upper_bound, lower_bound = 1, 0, 0

    dict_words = open('enable.txt').read().split()[1485:1490]

    jobs = []
    for i in range(num_procs):
        # Split up the data:
        step = len(offensives)/num_procs
        upper_bound = min(len(offensives), i*step + step)
        if i < num_procs-1:
            jobs.append(ThreadedProblem(i, dict_words, offensives[lower_bound:upper_bound]))
        else: # Make sure we pass the remaining words to the last process
            jobs.append(ThreadedProblem(i, dict_words, offensives[lower_bound:]))
        lower_bound = upper_bound + 1

    for job in jobs:
        job.start()

    # Wait for threads to finish
    while threading.active_count() > 1:
        for job in jobs:
            job.join(1)


start_time = time.time()
find_max_problem_count()
end_time = time.time()
print("Total time: " + time_delta(start_time, end_time))

# Print results after threads finish:
lock.acquire()
try:
    result
    print("Words with most possible offensive combinations: ")
    print(sorted(result.items(), key=operator.itemgetter(1))[-10:])
finally:
    lock.release() # release lock, no matter what.
