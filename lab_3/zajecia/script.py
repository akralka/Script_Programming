# import argparse

class Library:
    def __init__(self):
        self.books= {}
        self.transactions = {} 

    # def __str__(self):
    #     return self.transactions

    def parseFileLine(self, file):
        d = {} 
        with open(file, "r") as zawartosc:
            for line in zawartosc:
                if line:
                    key, value = map(str.strip, line.split(':'))
                    d[key] = int(value)

        self.books = d
        return self.books

    def parseInputLine():
        pass
    
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


# if __name__ == '__main__':
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-f", "--file", help="Give input!", required=True, nargs="+")

    # try:
    #     args = parser.parse_args()
        
    # except:
    #     print("Specify file names")      
    #     exit()

    # for file in args.file:
    #     conversion(file, args.c[0])
    

    # L = Library()

    # while True:
    #     try:
    #         operation = input().split()
    #         # transaction[0] to ma byc nazwa pliku
    #         if operation[0] == 'borrow':
    #             L.borrow(operation[1], operation[2], operation[3])

    #         if operation[0] == 'book_return':
    #             L.book_return(operation[1], operation[2], operation[3])

    #     except(EOFError):
    #         pass

