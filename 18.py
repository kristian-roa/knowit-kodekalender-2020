import requests


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/18/attachments/wordlist.txt'
    words = requests.get(url).text.splitlines()

    counter = 0
    for word in words:
        if word == word[::-1]: continue
        if len(word) <= 2: continue
        if group_mid(word) or group_edges(word) or group_mid_edges(word): counter += 1
    print(counter)


def group_mid(word):
    half = len(word) // 2
    return word == word[half+1:][::-1] + word[half-1:half+1] + word[:half-1][::-1]


def group_edges(word):
    half = len(word) // 2

    for i in range(half - 1):
        if word == word[(end := -i if i != 0 else len(word)):][::-1] + word[-i-2:end] \
                + word[i+2:-i-2][::-1] + word[i:i+2] + word[:i][::-1]:
            return True
    return False


def group_mid_edges(word):
    if len(word) % 2 or len(word) < 6: return False
    half = len(word) // 2
    for i in range(half - 1):
        if word == word[(end := -i if i != 0 else len(word)):][::-1] + word[-i-2:end] \
                + word[half+1:-i-2][::-1] + word[half-1:half+1] + word[i+2:half-1][::-1] \
                + word[i:i+2] + word[:i][::-1]:
            return True
    return False


main()
