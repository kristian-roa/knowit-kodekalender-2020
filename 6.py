import requests


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/6/attachments/godteri.txt'
    gifts = [int(i) for i in requests.get(url).text.split(',')]
    elves = 127
    snacks = sum(gifts)

    while snacks % elves: snacks -= gifts.pop()
    print('Snack for each elf:', snacks // elves)


main()
