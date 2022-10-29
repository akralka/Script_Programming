
class Library:
    def __init__(self):
        self.books= {"brysiu": 5, "Random kic": 7, "still_stresujacy_marcel:(((": 0.75}
        self.transactions = {} 

    def __str__(self):
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

        if isinstance(quantity, int):
            if not quantity.isdigit():
                return 'Wrong quantity'

        for letter in name.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong name"

        if name == '':
            return 'No name'
        
        if quantity <= 0:
            return "Quantity equal or less than 0"

        self.books[book] += quantity  
        
    




# if __name__ == '__main__':
#     while True:
#         pass




# s ł o d z i a k :((