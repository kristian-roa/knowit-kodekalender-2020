import requests


def main():
    url = 'https://julekalender-backend.knowit.no/challenges/11/attachments/hint.txt'
    passwords = requests.get(url).text.splitlines()
    pw = 'eamqia'

    for password in passwords:
        p_words = [list(password)]
        prev = password

        while len((shift := [shift_letter(l) for l in prev[1:]])) > 1:
            shift = [add_letters(prev[i], shift[i]) for i in range(len(shift))]
            p_words.append(shift)
            prev = shift
        else: p_words.append(shift)

        valid_passwords = ' '.join([''.join([p[i] for p in p_words if len(p) > i]) for i in range(len(p_words))])
        if pw in valid_passwords: print(password); break


def add_letters(a, b):
    o = ord(a) + ord(b) - 97
    if o > 122: o -= 26
    return chr(o)


def shift_letter(a): return chr(o) if (o := ord(a)+1) < 123 else chr(o-26)


main()
