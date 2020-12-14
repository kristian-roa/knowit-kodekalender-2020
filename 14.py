import sympy


def main():
    n = 1800813
    print(count_primes_in_sequence(n))


def count_primes_in_sequence(n):
    sequence = set()
    primes = 0

    lag_two, lag_one = 0, 1
    for i in range(n+1):
        if i == 0 or i == 1: sequence.add(i)
        else:
            v = v_min if (v_min := lag_two - i) > 0 and v_min not in sequence else lag_two + i
            sequence.add(v)
            lag_two = lag_one
            lag_one = v

            if sympy.isprime(v): primes += 1

    return primes


main()
