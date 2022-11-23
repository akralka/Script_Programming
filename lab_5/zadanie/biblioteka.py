import time
from abc import ABC

class Book(ABC):
    def __init__(self, book_id, author, title):
        self.book_id = book_id
        self.author = author
        self.title = title

class Date:
    def __init__(self, day, month, year, hour, minute, second):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second} {self.day}.{self.month}.{self.year}"

def parse():
    list = time.ctime().split()
    lista = list[3].split(':')
    date = Date(list[2], list[1], list[4], lista[0], lista[1], lista[2])
    return date


class BorrowedBook(Book):
    def __init__(self, book_id, author, title, reader_pesel = None):
            super().__init__(book_id, author, title)
            self.borrow_date = None
            self.return_date = None
            self.reader_pesel = reader_pesel

    def __str__(self):
        return f"Book ID: {self.book_id:3d}, Author: {self.author:13}, Title: {self.title}"

class BoughtBook(Book):
    def __init__(self, book_id, author, title, price, sold_quantity = 0):
            super().__init__(book_id, author, title)
            self.sell_date = None
            self.sold_quantity = sold_quantity
            self.price = price

    def __str__(self):
        return f"Book ID: {self.book_id:3d}, Author: {self.author:13}, Title: {self.title}"


class Reader():
    price_total_from_sell = 0

    def __init__(self, name, surname, pesel):
        self.name = name
        self.surname = surname
        self.pesel = pesel

    def __str__(self):
        return f"Fullname: {self.name} {self.surname}"

    def __add__(self, book: BorrowedBook):
        for letter in self.name.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong name"
        for letter in self.surname.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong surname"
        empty = True
        for i in Library.books_borrow:
            if book.title == i.title and book.author == i.author:
                empty = False
        if empty:
            return "can't borrow :there is no a book of that title or author"   
        if not book.borrow_date:
            book.reader_pesel = self.pesel
            book.borrow_date = parse()
            book.return_date = None
            Library.transactions_borrow.append(f"{self.name:10} {self.surname:12} borrowed  {book.title:8} {book.author:10}  id number: {book.book_id:2}  at  {book.borrow_date}") 
            for reader in Library.readers_list:
                if reader.name == self.name and reader.surname == self.surname and reader.pesel == self.pesel:
                    return None
            Library.readers_list.append(self)   
        else:
            Library.transactions_borrow.append(f"{self.name} {self.surname} you can't borrow {book.title}!")

    def __sub__(self, book: BorrowedBook):
        for letter in self.name.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong name"
        for letter in self.surname.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong surname"
        empty = True
        for i in Library.books_borrow:
            if book.title == i.title and book.author == i.author:
                empty = False
        if empty:
            return "can't return :there is no a book of that title or author"   
        if  book.borrow_date and book.reader_pesel == self.pesel:
            book.reader_pesel = None
            book.borrow_date = None
            book.return_date = parse()
            Library.transactions_borrow.append(f"{self.name:10} {self.surname:12} returned  {book.title:8} {book.author:10}  id number: {book.book_id:2}  at  {book.return_date}") 
        else:
            Library.transactions_borrow.append(f"{self.name} {self.surname} you can't return {book.title}!")

    def __eq__(self, book: BoughtBook): #==
        for letter in self.name.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong name"
        for letter in self.surname.lower():
            if letter not in 'aąbcćdeęfghijklłmnńoóprsśtuvwxyzźżq':
                return "Wrong surname"  
        empty = True
        for i in Library.books_buy:
            if book.title == i.title and book.author == i.author:
                empty = False
        if empty:
            return "can't buy: there is no a book of that title or author for sell"   
        Reader.price_total_from_sell += int(book.price)
        if not book.sell_date or i.book_id != book.book_id:
            book.sell_date = parse()
            book.sold_quantity +=1
            # Library.transactions_bought.append(f"{book.title} {book.author} {book.sold_quantity}")

            # Library.transactions_bought[self.name][book] += book.sold_quantity 
            
            if self.name in Library.transactions_bought.keys():
                if book in Library.transactions_bought[self.name]:
                    Library.transactions_bought[self.name][book] = book.sold_quantity
                else:
                    Library.transactions_bought[self.name].update({book: book.sold_quantity})
            else:
                Library.transactions_bought.update({self.name: {book: book.sold_quantity}})

class Library:

    def __str__(self):
        print('\nTransactions_borrowed:')
        for transaction in self.transactions_borrow:
            print(transaction)
        print('\nTransactions_bought:')
        print(Library.transactions_bought)
        print("\nIncome from sold books: ", Reader.price_total_from_sell)
        return ''

    @staticmethod
    def parseLine():
        book_borrow_list = []
        book_bought_book = []
        with open("C:\\Users\\ASUS\\Desktop\\semestr3\\Programowanie_skryptowe\\Scrypts\\lab_5\\zadanie\\book.txt", "r") as lines:
            id = 1
            for line in lines:
                book = line.rstrip().split(':')
                quantity = int(book[2])
                for _ in range(quantity):
                    if not book[3]:
                        book_borrow_list.append(BorrowedBook(id, book[0], book[1]))
                    else:
                        book_bought_book.append(BoughtBook(id, book[0], book[1], book[3]))
                    id += 1       
        return book_borrow_list, book_bought_book

    books_borrow, books_buy = parseLine()
    readers_list = []
    transactions_borrow = []
    transactions_bought = {}

    @classmethod
    def parseInput(cls):
        line = input().split()
        reader = Reader(line[0], line[1], line[2])
        operation = line[3]
        if operation == '+':
            for book in cls.books_borrow:
                if line[4] == book.title and line[5] == book.author and not book.reader_pesel:
                    reader + book
                    break
        elif operation == '==':
            for book in cls.books_buy:
                if line[4] == book.title and line[5] == book.author:
                    reader == book
                    break
        elif operation == '-':
            for book in cls.books_borrow:
                if line[4] == book.title and line[5] == book.author:
                    reader - book
                    break


if __name__=='__main__':

    try:
        while True:
            Library.parseInput()
            
    except(EOFError):
        print(Library())

# Adam Kasielski 123 == Harry_Potter Rowling
# Adam Kasielski 123 == Ludzie_bezdomni Zeromski
# Bartuś Fober 223 + Iliada Homer