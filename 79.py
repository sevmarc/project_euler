# Passcode derivation
import time
from collections import Counter


def read_info(filename):
    return [data.strip('\n') for data in open(filename, 'r')]


def combine(inputlist):
    result = ''
    for code in inputlist:
        for letter in code:
            if letter not in result:
                pass


start_time = time.time()

entries = sorted(read_info("inputfiles/79.txt"))
print(entries)
combine([entries[0], entries[1]])
combine(entries)

print(time.time() - start_time)
