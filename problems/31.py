""" Coin sums
In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?
"""

from function_collection.main import timer_wrapper


if __name__ == '__main__':
    counter_ = 1  # counter for couting number of possibilities, 1 for 200p case

    for a in range(3):  # number of 100p coins
        for b in range(int(1+(200-100*a)/50)):  # number of 50p coins
            for c in range(int(1+(200-100*a-50*b)/20)):  # number of 20p coins
                for d in range(int(1+(200-100*a-50*b-20*c)/10)):  # number of 10p coins
                    for e in range(int(1+(200-100*a-50*b-20*c-10*d)/5)):  # number of 5p coins
                        # number of 2p coins
                        for _ in range(int(1+(200-100*a-50*b-20*c-10*d-5*e)/2)):
                            counter_ += 1
    print(counter_)
