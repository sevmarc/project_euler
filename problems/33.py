""" Digit cancelling fractions
The fraction 49/98 is a curious fraction, as an inexperienced 
mathematician in attempting to simplify it may incorrectly believe 
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common 
terms, find the value of the denominator.
"""


def curious_fraction(a: int, b: int) -> bool:
    frac = a / b
    common = ''.join(set(str(a)).intersection(str(b)))
    for l in common:
        cur_a = str(a).replace(l, '')
        cur_b = str(b).replace(l, '')
        if len(cur_a) > 0 and len(cur_b) > 0 and cur_a != '0' and cur_b != '0':
            if (float(cur_a) / float(cur_b) == frac):
                return True
    return False


def calc33():
    results = [[i, j] for i in range(1, 100) for j in range(1, 100) if i < j and (
        i % 10 != 0) and (j % 10 != 0) and curious_fraction(i, j)]
    print(results)

    num = denum = 1
    for r in results:
        num *= r[0]
        denum *= r[1]
    print(f"{num} / {denum}")


if __name__ == '__main__':
    testing = False

    if testing:
        print(curious_fraction(49, 98))
        print(curious_fraction(49, 41))
        print(curious_fraction(30, 50))
    else:
        calc33()
