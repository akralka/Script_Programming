
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

# lista tylko z parzystymi liczbami w zakresie od 0 do 13
# lista kombinacji z powtórzeniami liczb z zakresu 3 : [(0, 0), (0, 1), ... (2, 1), (2, 2)]
# lista z liczbami z zakresu 5 w postaci: [(0, 0), (1, 1),...]
# lista z co drugim znakiem ze stringa 'Ada słodziak :3'
# 3 pierwsze nie wymagają żadnych bilbiotek

# Marcel 2
# from sys import argv; files = argv[1:]; result = len(list(filter(lambda x: x % 2 == 0, [int(number) for file in files for line in open(file, 'r').readlines() for number in line.rstrip().split()]))); print(result)

# Marcel 3
# from sys import argv
# numbers = [int(number) for file in files for line in open(file, 'r').readlines() for number in line.rstrip().split()]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(len(result))

# imperatywnie
# files = argv[1:]
# numbers = []
# for file in files:
#     with open(file, 'r') as file:
#         for line in file.readlines():
#             for number in line.rstrip().split():
#                 numbers.append(number)
# print(len(numbers))