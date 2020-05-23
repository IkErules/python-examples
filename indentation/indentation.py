"""
Sprachen wie Java oder c# definieren auszuführende Blöcke, welche zusammen gehören, mit Klammern {}.

In python wird das mit Einrückung gemacht. Blöcke, welche gleich eingerückt sind, gehören zusammen.
Um wie viele Whitespaces der Code eingerückt wird, kommt nicht drauf an. Pro Block muss jedoch mit
derselben Anzahl eingerückt werden.
Normalerweise werden vier Whitespaces empfohlen, was einer Tabulator Einrückung entspricht.
"""


class Indentation:
    def __init__(self, name, should_hit_private_method):  # constructor
        self.__name = name                                          # private variable
        self.should_hit_private_method = should_hit_private_method  # public property

    def public_method(self):
        print("Indentation.public_method()")
        if True:
            print("Hello %r" % self.__name)
            if self.should_hit_private_method:
             self.__private_for_each_example()   # if block has only one whitespace, works fine like this

    def __private_for_each_example(self):
        print("Indentation.__private_for_each_example()")
        for i in range(1, 11):
            print(i)
            if i == 5:
                break


def public_function():
    print("public_function()")
    print("Indentation like following works perfectly fine")
    result = ""
    counter = 0
    while counter < 10:
        if counter % 2 == 0:
                                                result += "."
        else:
          result += "+"
        counter += 1
    print(result)


indentation = Indentation("Bob", True)
indentation.public_method()

public_function()

"""
Folgend ein paar Beispielen von falschen Einrückungen

 def perm(l):                       # Deklaration einer neuen Methode darf nicht bereits eingerückt sein
for i in range(len(l)):             # Einrückung erforderlich, da neuer Block erwartet 
    s = l[:i] + l[i+1:]
        p = perm(l[:i] + l[i+1:])   # Kein neuer Block erwartet, nicht erlaubte Einrückung 
        for x in p:
                r.append(l[i:i+1] + x)
            return r                # Falsche Einrückung, muss im selben Kontex vom restlichen foreach Kontex sein
"""
