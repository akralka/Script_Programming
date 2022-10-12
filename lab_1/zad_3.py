def print_2(n):
    for i in range(n):
        print(arr[i])

def print_3(n):
    for i in range(n):
        print("Tab[" + str(i) + "] =" , arr[i])

def print_4(arr):
    hash = {f'Klucz{i}': j for i, j in zip(range(len(arr)), arr)} # zip ; zwieksza range.. i arr jednoczesnie 
    for i in range(len(hash)):
        print(f"Hash[Klucz{i}] = {hash[f'Klucz{i}']}")

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().rstrip().split()))
    print_2(N)
    print_3(N)
    print_4(arr)
