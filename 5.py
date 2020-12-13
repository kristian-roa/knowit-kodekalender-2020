import requests
import numpy as np
import matplotlib.pyplot as plt


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/5/attachments/rute.txt'
    code = requests.get(url).text
    directions = {'O': np.array([1, 0]), 'N': np.array([-1, 0]), 'H': np.array([0, 1]), 'V': np.array([0, -1])}

    new_code = []; count = 1; prev = code[0]
    for c in code[1:]:
        if prev == c: count += 1
        else: new_code.append((count, prev)); count = 1
        prev = c
    else: new_code.append((count, prev))

    start = np.array([0, 0])
    idxs = [start] + [(start := start + (c * directions[d])) for c, d in new_code]
    min_y, min_x = [min([idx[i] for idx in idxs]) for i in (0, 1)]
    idxs = [(y - min_y, x - min_x) for y, x in idxs]

    x, y = [x for _, x in idxs], [y for y, _ in idxs]
    plt.figure()
    plt.fill(x, y)
    plt.suptitle('Santas house')

    print('Area of house:', round(polyArea(x, y)))


def polyArea(x, y): return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


main()
plt.show()
