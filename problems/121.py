""" Disc game prize fund
A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.
"""

from function_collection.main import binomial_coefficient


def nth_game(n: int) -> int:
    return sum([binomial_coefficient(n, i) for i in range(0, int((n - 1)/2) + 1)])


def win_n_game(n: int) -> int:
    return sum([nth_game(i) for i in range(1, n + 1)])


if __name__ == '__main__':
    result = win_n_game(15)
    print(f"{result = }")
