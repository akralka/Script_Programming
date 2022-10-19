import slownik
import lista
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "m:", ["moduł="])
    # opts = [('-m', 'slownik')] albo [('-m', 'lista')] >> opts[0][1]
    modul = opts[0][1]

except:
    print("Wrong input!")

if modul == "lista":  
    arr = lista.zapisz(sys.argv[3:])
    lista.wypisz(arr)

if modul == "slownik":
    arr = {}
    arr = slownik.zapisz(arr, sys.argv[3:])
    slownik.wypisz(arr)

