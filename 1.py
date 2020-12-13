import requests

def main():
    url = 'https://julekalender-backend.knowit.no/challenges/1/attachments/numbers.txt'
    all_nums = set(range(1, 100001))
    nums = set([int(i) for i in requests.get(url).text.split(',')])
    ans = (all_nums - nums).pop()
    print(ans)


main()
