import sys
import collections 

print('Ładowanie modułu "{0}"'.format(__name__))

############################################

def wypisz(lista):
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    for i in lista:
           print("{0}:{1}".format(i[0], i[1]) +",", end="")     


def zapisz(lista):
    print('Wywołano funkcję "zapisz()" modułu "{0}"'.format(__name__))
    return collections.Counter("".join(lista)).most_common()
    # most_common - obsługuje liste krotek
     
############################################

if __name__=="__main__":
    print('Załadowano moduł "{0}"'.format(__name__))
    lista = []
    lista = zapisz(sys.argv[1:])
    wypisz(lista)


