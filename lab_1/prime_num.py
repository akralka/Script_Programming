import math
import sys

def prime(num): 

    if num == 0 or num == 1:
        return False

    for j in range(2, math.ceil(num/2)+1):
        if num % j == 0:
            return False
    
    return True


if __name__ == '__main__': 
    nums = sys.argv[1:] # string, 1: zeby nie brać nazwy pliku z konsoli [0]
    nums = [int(i) for i in nums if i.isdigit()] # digit    

    for num in nums:
        if prime(num) == True:
            print(num)
