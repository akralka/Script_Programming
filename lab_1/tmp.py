def avg(n):
    avg = 0
    for i in range(0,n):
        avg += arr[i]
    return avg
def med(n):
    if n % 2 == 0:
        print((q[n // 2 - 1] + q[n //2]) / 2)
    if n % 2 != 0:
        print(q[n // 2])
def mode(n):
    a = 0
    tmp = []
    for i in range(0,n):
        for j in range(0,n):
            if i != j:
                if arr[i] == arr[j]:
                    a += 1
                    tmp.append(arr[i])
    print(tmp)


if __name__ == '__main__':
    n =int(input())
    arr = list(map(int, input().rstrip().split())) 
    q = sorted(set(arr))
    print(float(avg(n)/10))
    med(n)
    mode(n)
    
