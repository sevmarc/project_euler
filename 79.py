""" Passcode derivation
A common security method used for online banking is to 
ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for 
the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in 
order, analyse the file so as to determine the shortest 
possible secret passcode of unknown length.
"""

import time
from collections import Counter


def read_info(filename):
    return [data.strip('\n') for data in open(filename, 'r')]


def combine(inputlist):
    """
    123
    456 -> 123456
    458
    354 -> 34548
    111
    112 -> 1121 / 1112 (?)
             |      |
    121 -> 1121 / 11121 <- we can only decide in the next step
           ^^^^
    """

    results = []
    for result in results:
        for code in inputlist:
            for letter in code:
                if letter not in result:
                    result += letter
        


start_time = time.time()

entries = sorted(read_info("inputfiles/79.txt"))
print(entries)
combine([entries[0], entries[1]])
combine(entries)

print(time.time() - start_time)
