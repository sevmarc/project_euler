""" Concealed Square
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

from math import sqrt
from function_collection.main import timer_wrapper


# unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0
def check_pattern(n: int) -> bool:
    nword = str(n)
    # 1_2_3_4_5_6_7_8_9_0
    return nword[0] == '1' and \
            nword[2] == '2' and \
            nword[4] == '3' and \
            nword[6] == '4' and \
            nword[8] == '5' and \
            nword[10] == '6' and \
            nword[12] == '7' and \
            nword[14] == '8' and \
            nword[16] == '9'


def solution():
    """
    last digit must be 0 <- roots last digit must also be 0
    can the second to last digit of root be not 0?
    no, it has to be 0 as well (10^2=100)
    -> last three digits: ...900
    -> roots last two digits: .30 or .70
    as 30^2=900 and 70^2=4900
    """
    min_ = 1020304050607080900
    max_ = 1929394959697989900  # last digit 0
    init_root = int(sqrt(min_))
    end_root = int(sqrt(max_)) + 1
    # root cant have 00 ending
    # then square would have 0000 ending
    
    for i in range(init_root, end_root, 10):
        if str(i)[-2:] == '30' or \
           str(i)[-2:] == '70':
            sq_ = i * i
            if check_pattern(sq_):
                print(i, sq_)

if __name__ == '__main__':
    # guess()
    timer_wrapper(solution)
