# python3 -c 'from collections import Counter;import sys,re;res = dict(Counter((map(lambda i:len(i), (re.findall(f"\\w+", sys.stdin.read()))))));print(res)'

# dla czytelnosci
from collections import Counter
import sys
import re
res = dict(Counter((map(lambda i:len(i), (re.findall(f"\\w+", sys.stdin.read()))))))
print(res)

# \\w 0-9 a-Z



