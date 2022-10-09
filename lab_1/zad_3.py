
def print_2(n):
    for i in range(n):
        print(arr[i])

def print_3(n):
    for i in range(n):
        print("Tab[" + str(i) + "] =" , arr[i])

def print_4(n):
    hash = {}
    for i in range(n):
        hash["KLucz"] = arr[i]
        for j in hash:
            print("Hash["+ str(j) + str(i) + "]= %d" % (hash[j]))

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().rstrip().split()))
    print_2(N)
    print_3(N)
    print_4(N)


