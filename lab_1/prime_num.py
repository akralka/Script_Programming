import math

def prime(a):
    for i in range(a):
        if arr[i] == 0 or arr[i] == 1:
            print(arr[i])
            continue
        elif arr[i] == 2:
            continue
        for j in range(2, math.ceil(arr[i]/2)+1):
            if arr[i] % j == 0:
                break
            else:
                print(arr[i])
                break

if __name__ == '__main__':
    a = int(input())
    arr = list(map(int, input().rstrip().split()))
    prime(a)
