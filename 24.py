import requests


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/24/attachments/rute.txt'
    route = requests.get(url).text

    energy = 10
    for count, house in enumerate(route, 1):
        energy += 1 if house == '1' else -1
        if energy == 0: break

    print(count)


main()
