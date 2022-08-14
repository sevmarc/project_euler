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

from collections import Counter
from function_collection.main import timer_wrapper
from function_collection.utils import handle_filepath


def read_info(filename):
    return [data.strip('\n') for data in open(filename, 'r')]

def order_digits(inputlist, digitnum):
    digits = [i[digitnum] for i in inputlist]
    c = Counter(digits)
    sorted_digits = sorted(c.items(), key=lambda item: (-item[1], item[0]))
    if digitnum == 2:
        sorted_digits = reversed(sorted_digits)
    digit_strip = ""
    for i in sorted_digits:
        digit_strip += i[0]
    print(c, digits, digit_strip)
    return digit_strip

def remove_unnecessary(inputlist, result):
    for ind_ in range(len(result)):
        result_short = result[:ind_ - len(result)] + result[ind_ -len(result) + 1:]  # remove ind_ character
        
def check_input(input_, current_result):
    pass


def check_inputlist(inputlist, current_result):
    for input_ in inputlist:
        pass

def algo1(inputlist):
    pass


def combine(inputlist):
    """
    123
    456 -> 123456
    1442536

    458
    354 -> 34548
    111
    112 -> 1121 / 1112 (?)
             |      |
    121 -> 1121 / 11121 <- we can only decide in the next step
           ^^^^
    
    Most basic solution:
    1234567890 1234567890 1234567890
    Need to find an optimal way
    order it based on digit occurence -
        most common first digit, second...
    """

    result = ""
    result += order_digits(inputlist, 0)
    result += order_digits(inputlist, 1)
    result += order_digits(inputlist, 2)
    
    print(result)
    return result


entries = sorted(read_info(handle_filepath("inputfiles/79.txt")))
combine([entries[0], entries[1]])

timer_wrapper(combine, entries)
