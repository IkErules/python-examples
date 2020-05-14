"""
Übung Java 8, Teil 1+2
---- Nr. 4 ----
"""

from functools import reduce


def filter_map_reduce(names):
    names = filter(lambda x: 3 <= len(x) <= 4, names)
    names = map(lambda x: x.upper(), names)
    return reduce(lambda x, y: x + " " + y, names)


def start():
    names = ["Susanna", "Joe", "Lu", "Timmy", "Rafael", "Lisa"]
    result = filter_map_reduce(names)
    print(result)


start()
