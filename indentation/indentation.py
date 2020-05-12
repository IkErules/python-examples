"""
Sprachen wie Java oder c# definieren auszuführende Blöcke, welche zusammen gehören, mit Klammern {}.

In python wird das mit Einrückung gemacht. Blöcke, welche gleich eingerückt sind, gehören zusammen.
Um wie viele Whitespaces der Code eingerückt wird, kommt nicht drauf an. Pro Block muss jedoch mit
derselben Anzahl eingerückt werden.
Normalerweise werden vier Whitespaces empfohlen, was einem Tabulator Einrückung entspricht.
"""

# if-statements
if True:
    name = "first indentation if"
    nextStep = True
    print("First if %r" % name)
    if nextStep:
     name = "second indentation if"
     print("Is only one space indentation valid? YES! Name is %r" % name)

# for each
for i in range(1, 11):
    print(i)
    if i == 5:
        break

# while
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
