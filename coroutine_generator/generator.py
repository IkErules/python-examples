"""
Mit dem yield Operator können Generatoren erstellt werden. Diese können in einer for-each Schleife
abgearbeitet werden.
"""

def fibonacci(n):
    """Ein Fibonacci-Zahlen-Generator"""
    a, b, counter = 0, 1, 0
    while True:
        if counter > n: return
        yield a
        a, b = b, a + b
        counter += 1

fibIterator = fibonacci(5)
for x in fibIterator:
    print(x)

"""Generatoren können nur einmal aufgerufen werden, folgender Code bleibt wirkungslos"""
for y in fibIterator:
    print(y)

"""Erst wenn der Generator neu erzeugt wird, werden die Zahlenfolgen erneut ausgegeben."""
fibIterator = fibonacci(5)
for y in fibIterator:
    print(y)