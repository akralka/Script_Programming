import slownik
import lista
import sys


if __name__=="__main__":

    try:
        if sys.argv[1] == "--lista":  
            arr = lista.zapisz(sys.argv[2:])
            lista.wypisz(arr)

        if sys.argv[1] == "--slownik":
            arr = {}
            arr = slownik.zapisz(arr, sys.argv[2:])
            slownik.wypisz(arr)

    except TypeError:
        print("Wrong input!")
