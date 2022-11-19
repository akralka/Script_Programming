# python3 -c 'import sys,re,functools;from collections import Counter;print(re.sub(r":\s",":",str(dict(Counter((map(lambda i:len(i), (re.findall(r"\S+", sys.stdin.read())))))))))'


# from collections import Counter as ctr;data = ""; 
# while True: data += " " + input() if data[-4:] != "exit" else print(ctr(list(map(lambda el: len(el), data.split()[:-1]))).most_common())


from collections import Counter as ctr;data = ""; 
while True: 
    try:
        data += " " + input() 
    except(EOFError):
        print(ctr(list(map(lambda el: len(el), data.split()))).most_common());exit()



        