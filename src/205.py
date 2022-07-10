""" Dice Game
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
"""

from itertools import permutations


def sum_options(num_of_dices: int, faces: int):
    """
    3 dices with 2 faces

    1 1 1
    1 1 2
    1 2 1
    1 2 2
    2 1 1
    2 1 2
    2 2 1
    2 2 2

    2 ^ 3 options
    """
    possibilities = range(1, faces + 1)
    poss = []
    for p in possibilities:
        for d in range(num_of_dices):
            poss.append(p)
    
    return sorted([sum(diceroll) for diceroll in list(set(permutations(poss, num_of_dices)))])

if __name__ == '__main__':
    print('d: 3, f: 2 -> ', sum_options(3, 2))
    print('d: 9, f: 4 -> ', sum_options(9, 4))
    print('d: 6, f: 6 -> ', sum_options(6, 6))