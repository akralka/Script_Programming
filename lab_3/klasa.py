import sys


def methodBody(self, name):
    return "Wywołano metodę \033[{color}m{name:^17}\033[0m obiektu \033[{color}m{objectId}\033[0m".format(
            name     = name,
            color    = "38:5:{}".format(id(self) % 13 + 1),
            objectId = id(self)
        )


class Klasa(object):

    tab = [1,2,3]

    def __init__(self, tab, zmienna_1, zmienna_2):
        print(methodBody(self, sys._getframe().f_code.co_name))
        self.tab = tab
        self._zmienna_1 = zmienna_1
        self.__zmienna_2 = zmienna_2

    def __del__(self):
        print(methodBody(self, sys._getframe().f_code.co_name))

    def __str__(self):
        return methodBody(self, sys._getframe().f_code.co_name)

    def __repr__(self):
        return methodBody(self, sys._getframe().f_code.co_name)

    def metodaInstancyjna(self):
        print(methodBody(self, sys._getframe().f_code.co_name))
        print(self.tab)
        print(Klasa.tab)

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę \033[1m{name:^17}\033[0m klasy   \033[1m{cls}\033[0m".format(
            name = sys._getframe().f_code.co_name,
            cls  = cls.__name__)
        )

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę \033[1m{name:^17}\033[0m klasy   \033[1m{cls}\033[0m".format(
            name = sys._getframe().f_code.co_name,
            cls  = __class__.__name__)
        )


print("Załadowano zawartość pliku '{name}'".format(name=__file__))

# obiekt = Klasa([4,5,6], 10,20) 
# print(obiekt.tab)   #publiczne
# print(obiekt._zmienna1)     #chronione 
# print(obiekt._Klasa__zmienna_2)   #prywatne