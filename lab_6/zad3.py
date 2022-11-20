# python3 -c "import itertools, sys; array = list(itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2]))));tab = [int(num) for line in array for num in line.rstrip().split()];print (len(list(itertools.filterfalse(lambda x : x % 2 != 0, tab ))))" "plik1.txt" "plik2.txt"


# dla czytelnosci
import itertools, sys

array = list(itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2]))))
tab = [int(num) for line in array for num in line.rstrip().split()]
print (len(list(itertools.filterfalse(lambda x : x % 2 != 0, tab ))))


