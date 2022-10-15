<<<<<<< HEAD
import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#



def quartiles(arr):
    n = len(arr)
    arr.sort()
    tab = []
    q = []
    w = []
    print(arr)
    if n % 2 == 0:
        med2 = (arr[n//2 - 1] + arr[n//2]) / 2
        for i in range(len(arr)):
            if i < n//2:
                q.append(arr[i])
                if len(q) % 2 == 0:
                    med1 = (q[len(q)//2 - 1] + q[len(q)//2]) / 2
                else:
                    med1 = q[len(q)//2]

        for i in range(len(arr)):
            if i > n//2 - 1:
                w.append(arr[i])
                print(w)
                if len(w) % 2 == 0:
                    med3 = (w[len(w)//2 - 1] + w[len(w)//2]) / 2
                else:
                    med3 = w[len(w)//2]
        

    if n % 2 != 0:
        med2 = arr[n//2]
        for i in range(len(arr)):
            if i < n//2:
                q.append(arr[i])
                if len(q) % 2 == 0:
                    med1 = (q[len(q)//2 - 1] + q[len(q)//2]) / 2
                else:
                    med1 = q[len(q)//2]

        for i in range(len(arr)):
            if i > n//2:
                w.append(arr[i])
                # print(w)
                if len(w) % 2 == 0:
                    med3 = (w[len(w)//2 - 1] + w[len(w)//2]) / 2
                
                else:
                    med3 = w[len(w)//2]


    tab.append(int(med1))
    tab.append(int(med2))
    tab.append(int(med3))


    return tab



if __name__ == '__main__':
=======

>>>>>>> a27f0ea52263afa4b7985ad4cd2bd94e3e15ab6c
    

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    print(res)



# 12
# 4 17 7 14 18 12 3 16 10 4 4 12

# 9
# 3 7 8 5 12 14 21 13 18