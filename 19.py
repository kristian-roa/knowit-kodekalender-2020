from collections import deque, Counter
import requests
import re


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/19/attachments/input.txt'
    games = [re.match(r'(\d+) (\d+) \[(.*)]', game).groups() for game in requests.get(url).text.splitlines()]
    games = [(int(game[0])-1, int(game[1]), deque(game[2].split(', '))) for game in games]

    def rule_2(elves):
        nonlocal i
        if i >= len(elves): i = 0
        del elves[i]
        i += 1

    def rule_3(elves):
        l = len(elves)
        if l == 2: elves.popleft()
        elif l % 2: del elves[l // 2]
        else: del elves[(l // 2) - 1]; del elves[(l // 2) - 1]

    rules = [deque.popleft, rule_2, rule_3, deque.pop]

    count = Counter()
    for rule, shift, elves in games:
        i = 0
        while len(elves) > 1:
            elves.rotate(shift)
            rules[rule](elves)
        count[elves.pop()] += 1

    print(max(count, key=lambda key: count[key]))


main()
