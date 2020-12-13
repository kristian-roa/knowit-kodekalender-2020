import requests
import numpy as np
direc = (-1, 0, 1)
directions = [(y, x) for y in direc for x in direc if not y == x == 0]


def main():
    url_wordlist = 'https://gist.githubusercontent.com/knowitkodekalender/9e1ba20cd879b0c6d7af4ccfe8a87a19/raw/b19ae9548a33a825e2275d0283986070b9b7a126/wordlist.txt'
    matrix = np.genfromtxt('3_matrix.txt', delimiter=1, dtype=np.str)
    wordlist = requests.get(url_wordlist).text.split()

    for y, x in np.ndindex(matrix.shape):
        letter = matrix[y, x]
        for word in wordlist:
            if word[0] == letter:
                found = search(word, matrix, y, x)
                if found: wordlist.remove(word)

        if len(wordlist) == 3: break

    wordlist.sort()
    print(','.join(wordlist))


def search(word, matrix, y0, x0):
    for y_dir, x_dir in directions:
        for i in range(1, len(word)):
            y = y0 + i*y_dir; x = x0 + i*x_dir
            if y < 0 or x < 0 or y >= matrix.shape[0] or x >= matrix.shape[1]: break

            letter = matrix[y, x]
            if letter != word[i]: break

        else: return True
    return False


main()
