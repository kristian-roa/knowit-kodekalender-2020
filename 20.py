import requests
from anytree import Node, PostOrderIter


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/20/attachments/elves.txt'
    inp = requests.get(url).text.splitlines()
    elves = set([line.split('🎄')[-1] for line in inp])
    hierarchy = [[elf for elf in line.split('🎄') if elf in elves] for line in inp]

    elves = {}
    santa = Node('Santa')

    hierarchy.sort(key=lambda key: len(key))
    for branch in hierarchy:
        if len(branch) == 1:
            elves[elf] = Node((elf := branch[0]), parent=santa)
        else:
            elf, superior = branch[-1], branch[-2]
            elves[elf] = Node(elf, parent=elves[superior])

    for elf in PostOrderIter(santa):
        if len(elf.children) == 1 and (child := elf.children[0]).children:
            child.parent = elf.parent
            elf.parent = None

    workers = superiors = 0
    for elf in PostOrderIter(santa):
        if elf.children: superiors += 1
        else: workers += 1

    print(workers - superiors + 1)


main()
