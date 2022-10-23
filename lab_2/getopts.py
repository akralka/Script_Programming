import slownik
import lista
import sys
import getopt

try:
    opts = getopt.getopt(sys.argv[1:], "m:")
    # opts = [('-m', 'slownik')] albo [('-m', 'lista')] >> opts[0][1]
    module = opts[0][1]
    print(opts)

    if module == "lista":  
        arr = lista.zapisz(sys.argv[3:])
        lista.wypisz(arr)

    if module == "slownik":
        arr = {}
        arr = slownik.zapisz(arr, sys.argv[3:])
        slownik.wypisz(arr)

except:
    print("Wrong input!")
        





