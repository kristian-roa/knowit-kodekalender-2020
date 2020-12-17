import numpy as np


def main():
    try:
        kart = np.load('17_kart.npy')
    except:
        kart = np.genfromtxt('17_kart.txt', delimiter=1, dtype=np.str)
        np.save('17_kart.npy', kart)

    vacuume = '  sss  \n sssss \nsssssss\nsssXsss\nsssssss\n sssss \n  sss  '
    cleaning_area = 'kkk   kkk\nkkkkkkkkk\nkkkkkkkkk\n kkkkkkk \n kkkXkkk \n kkkkkkk \nkkkkkkkk \nkkkkkkkkk\nkkk   kkk'

    vacuume = np.array([list(word) for word in vacuume.splitlines()])
    cleaning_area = np.array([list(word) for word in cleaning_area.splitlines()])


main()
