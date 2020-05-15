from functools import reduce

"""
Übung Java 8, Teil 1+2
---- Nr. 4 ----
"""


def filter_map_reduce(names):
    names = filter(lambda x: 3 <= len(x) <= 4, names)
    names = map(map_function_to_upper, names)
    return reduce(lambda x, y: x + " " + y, names)


def map_function_to_upper(x: str):
    return x.upper()


"""
Sehr unschön und nicht zu gebrauchen! Um eine chained-Version zu verwenden, wird filter-map-reduce
zu reduce-map-filter.
"""
def filter_map_reduce_chained(names):
    return reduce(lambda x, y: x + " " + y,
                  map(lambda x: x.upper(),
                      filter(lambda x: 3 <= len(x) <= 4, names)))


def start():
    names = ["Susanna", "Joe", "Lu", "Timmy", "Rafael", "Lisa"]
    result = filter_map_reduce(names)
    result_chained = filter_map_reduce_chained(names)
    print(f"result: {result}")
    print(f"result chained: {result_chained}")


start()
