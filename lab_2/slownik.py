import sys


# print('Ładowanie modułu "{0}"'.format(__name__))

def wypisz(slownik):
    # print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    for key in slownik.keys():
        print("{0}:{1},".format(key, slownik[key]), end="")

def zapisz(slownik, input):
    # print('Wywołano funkcję "zapisz()" modułu "{0}"'.format(__name__))
    for i in input:
        if i in slownik:
            slownik[i] += 1
        else:
            slownik[i] = 1
    return slownik

if __name__=="__main__":
    # print('Załadowano moduł "{0}"'.format(__name__))
    slownik = {}
    slownik = zapisz(slownik, sys.argv[1:])  
    wypisz(slownik) 
    
