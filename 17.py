import numpy as np


def main():
    try:
        kart = np.load('17_kart.npy')
    except:
        kart = np.genfromtxt('17_kart.txt', delimiter=1, dtype=np.str)
        np.save('17_kart.npy', kart)

    vacuume = '  sss  \n sssss \nsssssss\nsssXsss\nsssssss\n sssss \n  sss  '
    cleaning_area = 'kkk   kkk\nkkkkkkkkk\nkkkkkkkkk\n kkkkkkk \n kkkXkkk \n kkkkkkk \nkkkkkkkkk\nkkkkkkkkk\nkkk   kkk'

    vacuume = np.array([list(word) for word in vacuume.splitlines()])
    cleaning_area = np.array([list(word) for word in cleaning_area.splitlines()])

    y0, x0 = (kart.shape[i] - vacuume.shape[i] + 1 for i in range(2))
    for y, x in np.ndindex((y0, x0)):
        vac = slice(y, y+7), slice(x, x+7)

        clean = slice(y-1 if y > 0 else y, y+8 if y < y0-1 else y+7), \
                slice(x-1 if x > 0 else x, x+8 if x < x0-1 else x+7)

        c = slice(0 if y > 0 else 1, 9 if y < y0-1 else 8), slice(0 if x > 0 else 1, 9 if x < x0-1 else 8)

        if len(np.nonzero(np.where(np.logical_and(vacuume != ' ', kart[vac] == 'x'), 1, 0))[0]) == 0:
            kart[vac] = np.where(vacuume == ' ', kart[vac], 's')
            kart[clean] = np.where(np.logical_and(cleaning_area[c] != ' ', kart[clean] == ' '), '.', kart[clean])

    dirty = np.count_nonzero(kart == ' ')
    print(dirty)


main()
