# Names scores
import time

def read_names():
    f_open = open("inputfiles/22.txt", "r")
    for block in f_open:
        names = block.split("\",\"")
    prop_names = [n.replace('\"', '') for n in names]
    return sorted(prop_names)

def add_letters(name):
    return sum([(ord(l) - 96) for l in str(name).lower()])

def calculate_name_values(list_of_names):
    return sum([(add_letters(name) * (i + 1)) for i,name in enumerate(list_of_names)])

start_time = time.time()

names = read_names()
print(calculate_name_values(names))

print(time.time() - start_time)