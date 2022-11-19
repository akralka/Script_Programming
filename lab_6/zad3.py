# python3 -c "from functools import reduce;import itertools,re,sys;res = reduce(lambda val, x: val+((x-1) % 2), iter(map(int, re.findall('\\d+', reduce(lambda val,e: val+e, itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2]))))))),0);print(res)", "plik1.txt" "plik2.txt"


# import sys
# nums = sys.argv[1:]
# tab = []
# a=0
# for i in nums:
#     file = i
#     with open(file, 'r') as File:
#         for line in File:
#             line = line.rstrip().split()
#             for i in line:
#                 i = int(i)
#                 if i % 2 == 0:
#                     tab.append(i)
#         a+=len(tab)
#         tab = []
# print(a)
#  python3 zad3.py "plik1.txt" "plik2.txt"