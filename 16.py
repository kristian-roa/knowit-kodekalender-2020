from sympy import divisors
from math import isqrt


def main():
    counter = 0

    for n in range(1000000):
        diff = sum(divisors(n)) - 2*n
        if diff > 0 and diff == isqrt(diff)**2: counter += 1

    print(counter)


main()
