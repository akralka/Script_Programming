
def parseFileLine(file):
    d = {} 

    with open(file, "r") as zawartosc:
        for line in zawartosc:
            if line:
                key, value = map(str.strip, line.split(':'))
                d[key] = value

    return d

if __name__ == "__main__":


    print(parseFileLine("book.txt"))
