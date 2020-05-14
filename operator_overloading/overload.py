# PCP Python Bericht
#
# Operator overloading
#

class Rechteck:

    # Konstruktor
    def __init__(self, breite, hoehe):
        if (breite <= 0):
            raise ValueError('Breite von einem Rechteck muss grösser 0 sein')
        self.__w = breite
        self.__h = hoehe

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    # Der Operator + wird hier überschrieben
    def __add__(self, other):
        sum_h = self.__h + other.h
        sum_w = self.__w + other.w
        return Rechteck(sum_w, sum_h)

    def __str__(self):
        return str(self.w) + " " + str(self.h)


r1 = Rechteck(12, 4)
r2 = Rechteck(2, 2)

# Zwei Rechtecke addieren
r3 = r1 + r2

print('Rechteck 1: ', r1)
print('Rechteck 2: ', r2)
print('Rechteck 3: ', r3)

