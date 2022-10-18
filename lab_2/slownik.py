import sys
import collections 

# print('Ładowanie modułu "{0}"'.format(__name__))

def wypisz(slownik):
    # print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    for key, value in slownik.items():
        print("{0}:{1}".format(key, value) +",", end="")

def zapisz(slownik, input):
    # print('Wywołano funkcję "zapisz()" modułu "{0}"'.format(__name__))
    for i in input:
        if i not in input:
            input[i] = 1
        else:
            input[i] += 1

    return input

if __name__=="__main__":
    # print('Załadowano moduł "{0}"'.format(__name__))
    slownik = {}
    slownik = zapisz(slownik, sys.argv[1:])  
    wypisz(slownik) 
    
