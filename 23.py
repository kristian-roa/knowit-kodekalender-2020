import requests
from math import floor
from collections import Counter


def main():
    url_base = 'https://julekalender-backend.knowit.no/challenges/23/attachments/basewords.txt'
    url_rap = 'https://julekalender-backend.knowit.no/challenges/23/attachments/rap_battle.txt'

    base = dict([((b := base.split())[0], int(b[1])) for base in requests.get(url_base).text.splitlines()])
    rap = [((r := rap.split(': '))[0], r[1].split()) for rap in requests.get(url_rap).text.splitlines()]

    c = Counter()
    for elf, line in rap:
        points = 0

        for i, word in enumerate(line):
            vocal = 0 if i == 0 else calc_vocal(word, line[i-1])
            points += floor((base[word.replace('jule', '')] + vocal) / rep_div(i, line))

        c[elf] += points

    winner = max(c.items(), key=lambda key: key[1])
    print(f'{winner[0]},{winner[1]}')


def calc_vocal(word, prev):
    wovels = set('aeiouyæøå')
    diff = sum(1 for l in word if l in wovels) - sum(1 for l in prev if l in wovels)

    if diff < 0: diff = 0
    if word.startswith('jule'): diff *= 2
    return diff


def rep_div(i, line):
    rep_div = 1; core = line[i].replace('jule', '')
    while i > 0 and (line[(i := i - 1)].replace('jule', '') == core): rep_div += 1
    return rep_div


main()
