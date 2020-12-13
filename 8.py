import requests
import re


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/8/attachments/input.txt'
    inp = requests.get(url).text

    global cities, times
    cities = re.findall(r'(.+): (.+)$', inp, re.M)
    cities = dict([(c[0], [int(i) for i in re.findall(r'\d+', c[1])]) for c in cities])
    path = re.findall(r'^(?!.*:).+$', inp, re.M)
    times = dict([(city, 0) for city in cities])

    pos = [0, 0]
    for city in path: move(pos, cities[city])
    print('Greatest time difference:', max(times.values()) - min(times.values()))


def distance(coord_1, coord_2):
    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])


def inc_times(pos):
    for city, coord in cities.items():
        dist = distance(pos, coord)
        times[city] += 0 if dist == 0 else 0.25 if dist < 5 else 0.5 if dist < 20 else 0.75 if dist < 50 else 1


def move(pos, city):
    x, y = [city[i] - pos[i] for i in (0, 1)]

    move = 1 if x > 0 else -1
    for _ in range(abs(x)):
        pos[0] += move
        inc_times(pos)

    move = 1 if y > 0 else -1
    for _ in range(abs(y)):
        pos[1] += move
        inc_times(pos)


main()
