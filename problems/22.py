""" Names scores
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out 
the alphabetical value for each name, multiply this value by 
its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

from function_collection.main import timer_wrapper
from function_collection.utils import handle_filepath


def read_names() -> list[str]:
    f_open = open(handle_filepath("inputfiles/22.txt"), "r")
    for block in f_open:
        names = block.split("\",\"")
    prop_names = [n.replace('\"', '') for n in names]
    return sorted(prop_names)


def add_letters(name: str) -> int:
    return sum([(ord(l) - 96) for l in str(name).lower()])


def calculate_name_values(list_of_names: list[str]) -> int:
    return sum([(add_letters(name) * (i + 1)) for i,name in enumerate(list_of_names)])


if __name__ == '__main__':    
    names = read_names()
    print(timer_wrapper(calculate_name_values, names))
