def digit(n): 

    dig = ''
    non_dig = ''

    for i in n:
        if i.isdigit():
            dig +=i
        else:
            non_dig += i

    return (dig, non_dig)


if __name__=='__main__':

    while True:
        dig, non_dig = digit(input())

        if len(non_dig) != 0:
            print("\tWyraz:", non_dig)
            
        if len(dig) != 0:
            print("\tLiczba:", dig)
