# python3 -c "from functools import reduce;import itertools,re,sys;res = reduce(lambda val, x: val+((x-1) % 2), iter(map(int, re.findall('\\d+', reduce(lambda val,e: val+e, itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2]))))))),0);print(res)", "plik1.txt" "plik2.txt"



# from functools import reduce;import itertools,re,sys;
# res = reduce(lambda val, x: val + ((x-1) % 2), iter(map(int, re.findall('\\d+', 
# reduce(lambda val,a: a+val, itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2]))))))),0);print(res)



# python3 -c "from functools import reduce;import itertools,re,sys;res = reduce(lambda val, x: val+((x-1) % 2), 
# iter(map(int, re.findall('\\d+', reduce(lambda val,e: val+e, itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2]))))))),0);
# print(list(itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2])))))", "plik1.txt" "plik2.txt"


# num = [1, 3, 5, 6, 2]
# from functools import reduce;import itertools,re,sys;res = reduce(lambda val, x: x+val, num); print(res)
# import functools
# lis = [1, 3, 5, 6, 2]
# print(functools.reduce(lambda a, b: a+b, lis)) >> sume z lis

import sys, functools
nums = sys.argv[1:]
tab = []
a=0
for i in nums:
    file = i
    with open(file, 'r') as File:
        for line in File:
            line = line.rstrip().split()
            for i in line:
                i = int(i)
                if i % 2 == 0:
                    tab.append(i)
res = functools.reduce(lambda x, val:val%2 ==0, tab)
print(res)
#         a+=len(tab)
#         tab = []
# print(a)
#  python3 zad3.py "plik1.txt" "plik2.txt"