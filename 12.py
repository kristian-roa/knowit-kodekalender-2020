import requests
import re
from anytree import Node, PreOrderIter


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/12/attachments/family.txt'
    tree_str = requests.get(url).text
    elves = re.sub(r'\)', r' )', re.sub(r'\(', r'( ', tree_str)).split()

    tree = prev = Node(elves[0])
    parents = []
    for elf in elves[1:]:
        if elf == '(': parents.append(prev)
        elif elf == ')': parents.pop()
        else: prev = Node(elf, parent=parents[-1])

    print(max(nodes_per_level(tree)))


def nodes_per_level(tree):
    nodes_per_level = [0 for _ in range(tree.height + 1)]
    for n in PreOrderIter(tree): nodes_per_level[n.depth] += 1
    return nodes_per_level


main()
