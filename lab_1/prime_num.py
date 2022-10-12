import math
import sys

def prime(arr):
    for i in range(len(arr)):
        if arr[i] == 0 or arr[i] == 1:
            continue
        elif arr[i] == 2:
            print(arr[i])
            continue
        for j in range(2, math.ceil(arr[i]/2)+1):
            if arr[i] % j == 0:
                break
            else:
                print(arr[i])
                break

if __name__ == '__main__': 
    a = sys.argv[1:] # string, 1: zeby nie brać nazwy pliku z konsoli [0]
    a = [int(i) for i in a if i.isdigit()] # digit 
    prime(a)
