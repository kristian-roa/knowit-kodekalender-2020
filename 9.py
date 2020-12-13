import numpy as np


def main():
    elves = np.genfromtxt('9_elves.txt', delimiter=1, dtype=np.str)

    days = 1
    while len((inf := infected(elves))) != 0:
        for i in inf: elves[i] = 'S'
        days += 1

    print('Dager før smittestopp:', days)


def sick_neighbours(idx, elves):
    sick = [(a, b) for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if 0 <= (a := idx[0]+y) < elves.shape[0] and 0 <= (b := idx[1]+x) < elves.shape[1] and elves[a, b] == 'S']
    return len(sick)


def infected(elves):
    return [idx for idx, val in np.ndenumerate(elves) if val != 'S' and sick_neighbours(idx, elves) >= 2]


main()
