import requests
from collections import Counter


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/13/attachments/text.txt'
    text = requests.get(url).text.strip()
    counts = Counter()

    def inc_char(char):
        counts[char] += 1
        return char if counts[char] == ord(char) - 96 else ''

    print(''.join([inc_char(char) for char in text]))


main()
