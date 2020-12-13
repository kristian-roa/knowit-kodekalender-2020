import numpy as np


def main():
    try:
        forest = np.load('7_forest.npy')
    except:
        forest = np.genfromtxt('7_forest.txt', delimiter=1, dtype=np.str, comments='!')
        np.save('7_forest.npy', forest)

    space = np.argwhere(np.all(forest[..., :] == ' ', axis=0)).squeeze()
    trees = [forest[:, space[i]+1:space[i+1]] for i in range(1, len(space)-1, 2)]

    counter = 0
    for tree in trees:
        root = tree.shape[1] // 2
        l = tree[:, :root]; r = tree[:, root+1:]
        if np.array_equal(l, np.flip(r, axis=1)): counter += 1

    print('Symmetrical trees:', counter)


main()
