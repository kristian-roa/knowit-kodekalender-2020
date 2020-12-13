import requests
import re
import numpy as np


def main():
    ingredients = ['sukker', 'mel', 'melk', 'egg']
    cake = [2, 3, 3, 1]

    deliveries = requests.get('https://julekalender-backend.knowit.no/challenges/4/attachments/leveringsliste.txt').text
    amount = [sum([int(i) for i in re.findall(rf'{ing}: (\d+)', deliveries)]) for ing in ingredients]

    print(min(np.array(amount) // np.array(cake)))


main()
