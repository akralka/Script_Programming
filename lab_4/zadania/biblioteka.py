import time

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


class Book():
    def __init__(self, book_id, author, title, reader_pesel = None):
            self.book_id = book_id
            self.author = author
            self.title = title
            self.borrow_date = None
            self.return_date = None
            self.reader_pesel = reader_pesel

    def __str__(self):
        return f"Book ID: {self.book_id:3d}, Author: {self.author:13}, Title: {self.title}"


class Reader():
    def __init__(self, name, surname, pesel):
        self.name = name
        self.surname = surname
        self.pesel = pesel

    def __str__(self):
        return f"Fullname: {self.name} {self.surname}"

    def __add__(self, book: Book):
        if not book.borrow_date:
            book.reader_pesel = self.pesel
            book.borrow_date = parse()
            book.return_date = None
            Library.transactions.append(f"{self.name:10} {self.surname:12} borrowed  {book.title:18} {book.author:10}  id number: {book.book_id:2}  at  {book.borrow_date}") 
            for reader in Library.readers_list:
                if reader.name == self.name and reader.surname == self.surname and reader.pesel == self.pesel:
                    return None
            Library.readers_list.append(self)   
        else:
            Library.transactions.append(f"{self.name} {self.surname} you can't borrow {book.title}!")

    def __sub__(self, book: Book):
        if  book.borrow_date is not None and book.reader_pesel == self.pesel:
            book.reader_pesel = None
            book.borrow_date = None
            book.return_date = parse()
            Library.transactions.append(f"{self.name:10} {self.surname:12} returned  {book.title:18} {book.author:10}  id number: {book.book_id:2}  at  {book.return_date}") 
        else:
            Library.transactions.append(f"{self.name} {self.surname} you can't return {book.title}!")


class Library:

    def __str__(self):
        for book in self.books:
            print(book)
        for reader in self.readers_list:
            print(reader)
        for transaction in self.transactions:
            print(transaction)
        return ''

    @staticmethod
    def parseLine():
        book_list = []
        with open("C:\\Users\\ASUS\\Desktop\\semestr3\\Programowanie_skryptowe\\Scrypts\\lab_4\\zadania\\book.txt", "r") as lines:
            id = 0
            for line in lines:
                book = line.strip('\n').split(':')
                quantity = int(book[-1])
                for _ in range(quantity):
                    book_list.append(Book(id, book[0], book[1], None))
                    id += 1       
        return book_list

    books = parseLine()
    readers_list = []
    transactions = []

    @classmethod
    def parseInput(cls):
        line = input().split()
        reader = Reader(line[0], line[1], line[2])
        operation = line[3]
        for book in cls.books:
            if line[4] == book.title and line[5] == book.author and not book.reader_pesel:
                if operation == '+':
                    reader + book
                    break
                elif operation == '-':
                    reader - book
                    break


if __name__=='__main__':

    try:
        while True:
            Library.parseInput()
            
    except(EOFError):
        print(Library())

# Adam Kasielski 123 + Harry_Potter Rowling