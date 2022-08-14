""" Lattice paths
Starting in the top left corner of a 2x2 grid, and only being 
able to move to the right and down, there are exactly 6 routes 
to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

def moveset(n: int, m: int) -> int:
    if (n == 0) or (m == 0):
        return 1
    return moveset(n-1, m) + moveset(n, m-1)

def trial(x: int) -> int:
    if x == 1:
        return 2
    return (8*x-4)/(2*x)*trial(x-1)


if __name__ == '__main__':
    testing = False
    
    if testing:
        print(1, moveset(1,1))
        print(moveset(1,2))
        print(moveset(2,1))
        print(2, moveset(2,2))
        print(3,moveset(3,3))
        print(4,moveset(4,4))
        print(5,moveset(5,5))
        print(6,moveset(6,6))
        print(7,moveset(7,7))
        print(8,moveset(8,8))
        print(9,moveset(9,9))
        print(10,moveset(10,10))

        for i in range(1,15):
            old = moveset(i-1,i-1)
            cur = moveset(i,i)
            print(i, cur, cur/old)
        
        print(moveset(20,20))

        for i in range(2,15):
            print(i, trial(i))
    else:
        print(int(trial(20)))
