""""""
from random import choice

ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def get_random_word(min_len: int = None, max_len: int = None) -> str:
    """"""
    with open('resources/words.txt', 'rt', encoding='utf8') as words_file:
        words = words_file.read().split('\n')
        words = [wd for wd in words if (min_len or 0) <= len(wd) <= (max_len or 1000)]
        return choice(words)


with open('resources/words.txt', 'rt', encoding='utf8') as words_file:
    words = words_file.read().split('\n')

counter = [0] * 25
for wd in words:
    counter[len(wd)] += 1

for i, cnt in enumerate(counter):
    print("{:>2}: {}" .format(i, cnt))
