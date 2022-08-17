from math import sqrt
from math import gcd as bltin_gcd
import time


#-------------------------functional-------------------------
def timer_wrapper(f, args=None):
    """ A function that prints how long f(args) ran for """
    start_time = time.time()
    if args:
        if isinstance(args, list):
            a = f(*args)
        else:
            a = f(args)
    else:
        a = f()
    print('Elapsed time: ', time.time() - start_time)
    return a

#-------------------------primes-------------------------
def is_prime(x: int) -> bool:
    """ Checks if a number is prime """
    if x <= 1:
        return False
    check = 0
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            check += 1
            if check > 0:
                return False
    return True

def next_prime(n: int) -> int:
    """ First prime after n"""
    while True:
        n += 1
        if is_prime(n):
            return n

def unique_prime_divisors(x, primes=[]):
    """ Returns a set of all prime divisors """
    if primes:
        temp = primes
    else:
        temp = []
    if is_prime(x):
        temp.append(x)
        return set(temp)
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            temp.append(i)
            return unique_prime_divisors(int(x / i), temp)

def generate_primes(x: int) -> list:
    """ Return a list of primes up to input (x) """
    return [i for i in range(1,x) if is_prime(i)]

#-------------------------exponents-------------------------
def exp_by_squaring(x, n):
    """ Faster method for exponents, using squaring """
    if n < 0:
        return exp_by_squaring(1 / x, -n)
    elif n == 0:
        return  1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_squaring(x * x,  n / 2)
    else:
        return x * exp_by_squaring(x * x, (n - 1) / 2)

def is_square(x: int) -> bool:
    """ Function for checking if an integer is a square """
    return sqrt(x).is_integer()

def is_power(x: int, n: int):
    """ Function for checking if an integer is nth power """
    return (x ** (1/float(n))).is_integer()

#-------------------------divisors-------------------------
def proper_divisors(x:int) -> list:
    """ Naive method for divs """
    return [i for i in range(1, int(x/2 + 1)) if x % i == 0]

def proper_divisors_fast(x:int) -> list:
    div = [1]  # everything is divisible by 1
    looking_limit = int(x / 2 + 1)
    current = 2

    while current < looking_limit:
        if x % current == 0:
            div.append(current)
            other_div = int(x / current)
            div.append(other_div)
            looking_limit = other_div
        current += 1
    return list(set(div))

def is_perfect(x: int) -> bool:
    return sum(proper_divisors_fast(x)) == x

def prime_divisors_with_quotients(x: int) -> dict:
    pass

#-------------------------strings--------------------------
def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


#----------------------factorization--------------------------
def fact_recursive(n: int) -> int:
    """ Recursive factorization, n > 0 """
    if n == 0:
        return 1
    return n * fact_recursive(n-1)

def fact_linear(n: int) -> int:
    """ Linear factorization, n > 0 """
    if n == 0:
        return 1
    prod_ = 1
    for i in range(1, n+1):
        prod_ *= i
    return prod_

def binomial_coefficient(n: int, k: int) -> int:
    return int(fact_linear(n) / (fact_linear(k) * fact_linear(n-k)))

#-----------------------pythagorean triples---------------------
def generate_all_pairs(max_num: int) -> list:
    """ Used to generate imaginary numbers with whole coordinates
    4 -> [[2, 1], [3, 1], [3, 2], [4, 1], [4, 2], [4, 3]] """
    pairs = []
    for i in range(1, max_num + 1):
        for j in range(1, i):
            pairs.append([i, j])
    return pairs

def generate_pythagorean_triple(imaginary_coords: list) -> list:
    """ Method involving imaginary numbers:
    (u+vi)^2 = (u^2 - v^2) + (2uv)i
    len(u+vi) =(u^2 + v^2)
    """
    u, v = imaginary_coords
    a = u**2 - v**2
    b = 2*u*v
    c = u**2 + v**2
    return [a,b,c]

def generate_all_pyth_triplets(max_val: int) -> list:
    pairs = generate_all_pairs(max_val)
    pyth_triplets = []
    for p in pairs:
        print(p, ': ', generate_pythagorean_triple(p))
        pyth_triplets.append(generate_pythagorean_triple(p))
    return pyth_triplets

def check_pyth(a: int, b: int, c: int) -> bool:
    """ Might be unused for now, may be useful """
    s = sorted([a, b, c])
    a, b, c = s[0], s[1], s[2]
    return a*a + b*b == c*c

#--------------------imaginary numbers--------------------------
class Imaginary():
    """
    Imaginary Number

    Help for overloading operators in python:
    +	__add__(self, other)
    –	__sub__(self, other)
    *	__mul__(self, other)
    /	__truediv__(self, other)
    //	__floordiv__(self, other)
    %	__mod__(self, other)
    **	__pow__(self, other)
    >>	__rshift__(self, other)
    <<	__lshift__(self, other)
    &	__and__(self, other)
    |	__or__(self, other)
    ^	__xor__(self, other)

    <	__LT__(SELF, OTHER)
    >	__GT__(SELF, OTHER)
    <=	__LE__(SELF, OTHER)
    >=	__GE__(SELF, OTHER)
    ==	__EQ__(SELF, OTHER)
    !=	__NE__(SELF, OTHER)

    -=	__ISUB__(SELF, OTHER)
    +=	__IADD__(SELF, OTHER)
    *=	__IMUL__(SELF, OTHER)
    /=	__IDIV__(SELF, OTHER)
    //=	__IFLOORDIV__(SELF, OTHER)
    %=	__IMOD__(SELF, OTHER)
    **=	__IPOW__(SELF, OTHER)
    >>=	__IRSHIFT__(SELF, OTHER)
    <<=	__ILSHIFT__(SELF, OTHER)
    &=	__IAND__(SELF, OTHER)
    |=	__IOR__(SELF, OTHER)
    ^=	__IXOR__(SELF, OTHER)

    –	__NEG__(SELF, OTHER)
    +	__POS__(SELF, OTHER)
    ~	__INVERT__(SELF, OTHER)
    """
    def __init__(self, a, b) -> None:
        self.re = a
        self.im = b
        self.len = self.calculate_length()

    def square(self):
        return self * self

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self + Imaginary(other, 0)
        elif isinstance(other, Imaginary):
            real = self.re + other.re
            imaginary = self.im + other.im
            return Imaginary(real, imaginary)
        else:
            print(f"{other} can't be multiplied with an imaginary!")
            return self  # do nothing

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Imaginary(self.re * other, self.im * other)
        elif isinstance(other, Imaginary):
            """
            (a + bi)(c + di) becomes (ac-bd)+(bc+ad)i
            """
            real = self.re * other.re - self.im * other.im
            imaginary = self.im * other.re + self.re * other.im
            return Imaginary(real, imaginary)
        else:
            print(f"{other} can't be multiplied with an imaginary!")
            return self  # do nothing

    def __rmul__(self, other):
        # commutative
        return self * other

    def calculate_length(self):
        return sqrt((self.re)**2 + (self.im)**2)

    def __repr__(self):
        return f"{self.re} + {self.im}i"

    def __str__(self):
        return f"{self.re} + {self.im}i"
    
