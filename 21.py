import requests


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/21/attachments/input.txt'
    order = [(int((i := elf.split(','))[1]), ts, i[0]) if elf != '---' else elf
             for ts, elf in enumerate(requests.get(url).text.splitlines())]

    queue = []
    counter = 0

    for elf in order:
        if elf == '---':
            queue.sort()
            queue.pop(0)
            counter += 1
        else: queue.append(elf)

    queue.sort()
    while queue.pop(0)[2] != 'Claus': counter += 1
    print(counter)


main()
