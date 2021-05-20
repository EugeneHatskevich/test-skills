import math


def func(phrase: str, word: str) -> str:

    n = int(math.sqrt(len(phrase)))
    result = []
    if n**2 < len(phrase):
        return "invalid length"
    for i in word:
        try:
            pos = list(phrase).index(i)
            pos1 = pos // n
            pos2 = pos % n
            result += [f'[{pos1}, {pos2}]']
        except ValueError:
            return "unknown character"
    return '->'.join(result)


try:
    search_phrase, key_word = input().split()
    print(func(search_phrase, key_word))
except ValueError:
    print("waiting 2 params")
