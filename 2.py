import sympy as sp


def main():
    n = 5433000

    gift_counter = i = 0
    while i <= n:
        if '7' in str(i):
            prime = i if sp.isprime(i) else sp.prevprime(i)
            i += prime
        else:
            gift_counter += 1
        i += 1

    print('Antall pakker:', gift_counter)


main()
