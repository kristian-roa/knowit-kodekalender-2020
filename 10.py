import requests


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/10/attachments/leker.txt'
    games = [results.split(',') for results in requests.get(url).text.splitlines()]

    points = {}

    for game in games:
        competitors = len(game)
        for placement, elf in enumerate(game, 1):
            if elf in points: points[elf] += competitors - placement
            else: points[elf] = competitors - placement

    winner = max(points, key=lambda key: points[key])
    print(winner + '-' + str(points[winner]))


main()
