import sys

class Library:
    def __init__(self, file):
        self.books = self.parseFileLine(file)
        self.transactions = {} 

    def __str__(self):
        return f"{self.transactions}\n{self.books}"

    def parseFileLine(self, file):
        d = {} 
        with open(file, "r") as lines:
            for line in lines:
                if line:
                    key, value = map(str.strip, line.split(':'))
                    d[key] = int(value)

        self.books = d
        return self.books

    def parseInputLine(self):

        operation = input().split()

        if operation[0] == 'borrow':
            print(self.borrow(operation[1], int(operation[2]), operation[3]))

        if operation[0] == 'book_return':
            print(self.book_return(operation[1], int(operation[2]), operation[3]))

    
    def borrow(self, book, quantity, name):
        
        if book not in self.books.keys():
            return "Wrong book"

        if isinstance(quantity, str):
            if not quantity.isdigit():
                return 'Wrong quantity'
        
        if quantity > self.books[book]:
            return "Too much"

        for letter in name.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong name"

        if name == '':
            return 'No name'
        
        if quantity <= 0:
            return "Quantity equal or less than 0"
        
        self.books[book] -= quantity 
        
        if name in self.transactions.keys():
            if book in self.transactions[name]:
                self.transactions[name][book] += quantity
            else:
                self.transactions[name].update({book: quantity})
        else:
            self.transactions.update({name: {book: quantity}})

        return 'Borrowed'


    def book_return(self, book, quantity, name):

        if book not in self.books.keys():
            return "Wrong book"

        if isinstance(quantity, str):
            if not quantity.isdigit():
                return 'Wrong quantity'

        for letter in name.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong name"

        if name == '':
            return 'No name'
        
        if quantity <= 0:
            return "Quantity equal or less than 0"

        if name not in self.transactions.keys():
            return "You didn't borrow anything"     
        else:
            if book not in self.transactions[name]:
                return "You didn't borrow that book"
            else:
                if self.transactions[name][book] < quantity:
                    if self.transactions[name][book] ==0:
                        return "You've already return all of the copies"
                    return "You borrow less copies of that book"

        self.books[book] += quantity  
        
        if name in self.transactions.keys():
            if book in self.transactions[name]:
                self.transactions[name][book] -= quantity
            else:
                self.transactions[name].update({book: quantity})
        else:
            self.transactions.update({name: {book: quantity}})

        return 'Returned'



if __name__=='__main__':

    L = Library(sys.argv[1])

    try:
        while True:
            L.parseInputLine()
            
    except(EOFError):
        print(L)

# python ./biblioteka.py "book.txt"
# borrow Faust 2 Andy
# book_return Faust 1 Andy