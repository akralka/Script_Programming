
python3 -c "import itertools, sys; array = list(itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2]))));tab = [int(num) for line in array for num in line.rstrip().split()];print (len(list(itertools.filterfalse(lambda x : x % 2 != 0, tab ))))" "plik1.txt" "plik2.txt"




# import sys, functools
# files = sys.argv[1:]
# tab = [int(num) for file in files for line in open(file, 'r').readlines() for num in line.rstrip().split()]
# for file in files:
#     with open(file, 'r') as File:
#         for line in File:
#             line = line.rstrip().split()
#             for i in line:
#                 if int(i) % 2 == 0:
#                     tab.append(i)
# print(len(tab))

#  python3 zad3.py "plik1.txt" "plik2.txt"




# reduce()--------------------------------------------------------------
# import functools
# lis = [1, 3, 5, 6, 2]
# print(functools.reduce(lambda a, b: a+b, lis)) >> sume z lis