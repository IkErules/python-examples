"""
Übung Java 8, Teil 1+2
---- Nr. 4 ----
"""

from functools import reduce


def map_function_to_upper(x: str):
    return x.upper()


def filter_map_reduce(names):
    names = filter(lambda x: 3 <= len(x) <= 4, names)
    names = map(map_function_to_upper, names)
    return reduce(lambda x, y: x + " " + y, names)


def start():
    names = ["Susanna", "Joe", "Lu", "Timmy", "Rafael", "Lisa"]
    result = filter_map_reduce(names)
    result_chained = filter_map_reduce_chained(names)
    print(result)
    print(result_chained)


def filter_map_reduce_chained(names):
    return reduce(lambda x, y: x + " " + y,
                  map(lambda x: x.upper(),
                      filter(lambda x: 3 <= len(x) <= 4, names)))


start()
