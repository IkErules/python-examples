class GeneratorObject:
    """
    Generator object to generate n fibonacci numbers.
    """

    def __init__(self, max):
        self._n = max

    def __iter__(self):
        self._current = 0
        self._next = 1
        self._counter = 0
        return self

    def __next__(self):
        if self._counter >= self._n:
            raise StopIteration

        self._current, self._next = self._next, self._current + self._next
        self._counter += 1
        return self._current


generator = GeneratorObject(5)
for i in generator:
    print(i)
