# PCP Python Bericht
#
# Eigener Typ definieren
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


r1 = Rechteck(12, 4)
