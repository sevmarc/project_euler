""" Perfect Square Collection
Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
"""

"""
x>y>z>0
x   -----------------
y   -------------
z   ----------

x+y ------------------------------
x-y ----
x+z ---------------------------
x-z -------
y+z -----------------------
y-z ---
"""

from function_collection.main import timer_wrapper, is_square
from math import sqrt


def generate_xyz_upto_x(x: int) -> list:
    starter = 1
    xyz_list = []
    for i in range(starter, x):
        for j in range(starter, i):
            xyz_list.append([x, i, j])
    return xyz_list

def check_xyz_squares(xyz: list) -> bool:
    x,y,z = xyz
    to_check = [x + y,
                x - y,
                x + z,
                x - z,
                y + z,
                y - z]
    for elem_ in to_check:
        if not is_square(elem_):
            return False
    return True

def naive_solution():
    found = False
    iter_ = 1
    while not found:
        xyzs = generate_xyz_upto_x(iter_)
        for xyz in xyzs:
            if check_xyz_squares(xyz):
                found = True
                print("Found: ", xyz)
        iter_ += 1

def create_yz_pairs(yzs: list):
    """
    From a list of numbers, creates all distinct pairs.
    """
    combinations = []
    yzs_removing = [i for i in yzs]  # this is to avoid repetition
    for yz in yzs:
        yzs_removing.remove(yz)
        for yz_ in yzs_removing:
            combinations.append([yz, yz_])
    # print(yzs, combinations)
    return combinations


def check_yz(yz: list) -> bool:
    """
    Checks a 'y' - 'z' pair, whether y+z and y-z are squares
    """
    y,z = max(yz), min(yz)
    return is_square(y-z) and is_square(y+z)


def solution():
    """
    X is equidistant from two sets of squares
    <---<---x--->--->
     -y  -z  +z  +y
    This is rather rare, so 'x' has to be looked for first.
    Then, the rest of the conditions are checkd:
        -z<---y--->+z
        These two are also squares.
    For this, we need a list of squares up to x.
    Then, we can search for y, z. And check, if found.
    Increase x, repeat.
    """

    x = 1  # starting value
    found = False  # condition for while statement
    while not found:
        # 1- generate list of squares up to x
        sq_list = [i*i for i in range(1, int(sqrt(x)))] 
        equi = []  # list to store equidistant squares
        # 2. check for equidistant squares
        for sq in sq_list:
            if is_square(x + (x-sq)):
                # rewrite: x - y = x - (x-sq) = sq
                equi.append(x - sq)
        # 3. check if y and z are correct
        for yz in create_yz_pairs(equi):
            if check_yz(yz):
                found = True
                y,z = yz[0], yz[1]
                print(f"x: {x}, y: {y}, z: {z}, sum: {x+y+z}, squares: {sqrt(x-y)}, {sqrt(x+y)}, {sqrt(x-z)}, {sqrt(x+z)}, {sqrt(y-z)}, {sqrt(y+z)}")
        x += 1  # iterate
    return x + y + z  #  sum in question


print(timer_wrapper(solution))