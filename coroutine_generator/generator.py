"""
Mit dem yield Operator können Generatoren erstellt werden. Diese können in einer for-each Schleife
abgearbeitet werden.
"""


def fibonacci(n):
    """Ein Fibonacci-Zahlen-Generator"""
    a, b, counter = 0, 1, 0  # Wird nur beim ersten Aufruf des Generators aufgerufen
    while True:
        if counter >= n: return
        yield a
        a, b = b, a + b
        counter += 1


"""Generatoren werden lazy instanziert. Sie werden somit erst ausgeführt, wenn ein Resultat benötigt wird."""

fibIterator = fibonacci(5)

print("Erster Aufruf des Iterators")
print(fibIterator.__next__())  # 0
print(fibIterator.__next__())  # 1
print(fibIterator.__next__())  # 1
print(fibIterator.__next__())  # 2
print(fibIterator.__next__())  # 3


"""Generatoren können nur einmal aufgerufen werden, folgender Code bleibt wirkungslos"""
print("Zweiter Aufruf nicht möglich...")
for y in fibIterator:
    print(y)


"""Erst wenn der Generator neu erzeugt wird, werden die Zahlenfolgen erneut ausgegeben."""
fibIterator = fibonacci(5)
print("Erst bei einer erneuten Instanzierung kann der Generator erneut ausgeführt werden...")
for y in fibIterator:
    print(y)