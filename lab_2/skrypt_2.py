

def digit(n):
        
        dig = []
        non_dig = []
        for i in n:
            if i.isdigit():
                i = int(i)
                dig.append(i)
            else:
                non_dig.append(i)

        if len(non_dig) != 0:
            print("    Wyraz:", end=' ')
            for element in non_dig:
                print(element, end='')
            print('\t')
            

        if len(dig) != 0:
            print("    Liczba:", end=' ')
            for element in dig:
                print(element, end='')
            print('\t')


if __name__=='__main__':
    for i in range(10):
        n = input()    
        digit(n)


