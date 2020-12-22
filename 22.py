import requests
import re


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/22/attachments/input.txt'
    words = [(list((w := re.match(r'(\w+) \[(.*)]', word)).group(1)), w.group(2).split(', '))
             for word in requests.get(url).text.splitlines()]

    counts = []
    for string, names in words:
        count = 0
        for name in names:
            idx = 0; l_idx = []
            for i, l in enumerate(string):
                if l == name[idx].lower():
                    idx += 1
                    l_idx.append(i)
                if idx == len(name):
                    for j in l_idx[::-1]: string.pop(j)
                    count += 1
                    break
        counts.append(count)

    print(max(enumerate(counts), key=lambda key: key[1])[0])


main()
