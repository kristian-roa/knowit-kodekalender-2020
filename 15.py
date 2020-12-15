import requests


def main():
    url_dictionary = 'https://julekalender-backend.knowit.no/challenges/15/attachments/wordlist.txt'
    url_riddles = 'https://julekalender-backend.knowit.no/challenges/15/attachments/riddles.txt'

    dictionary = set(requests.get(url_dictionary).text.splitlines())
    riddles = [i.split(', ') for i in requests.get(url_riddles).text.splitlines()]

    limord = set()
    for r1, r2 in riddles:
        for word in dictionary:
            if word in limord: continue
            if r1 + word in dictionary and word + r2 in dictionary: limord.add(word)

    print(sum([len(word) for word in limord]))


main()
