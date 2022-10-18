import sys


print('Ładowanie modułu "{0}"'.format(__name__))


############################################


def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))

def zapisz():
    print('Wywołano funkcję "zapisz()" modułu "{0}"'.format(__name__))


############################################

if __name__=="__main__":
    print('Załadowano moduł "{0}"'.format(__name__))
    lista = []
    lista = sys.argv[1:]


