class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.year})"
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        for b in self.books:
            if b.title == book.title:
                print(f"book '{book.title}' this book is already added")
                return
        self.books.append(book)
        print(f"book '{book.title}' the book has been added succesfuly")
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"book '{title}' the book has been removed")
                return
        print(f"book '{title}' book was not found")
    def list_books(self):
        if not self.books:
            print("lybrary is empty")
            return
        print("books in lybrary:")
        for book in self.books:
            print(book)

library = Library()

book1 = Book("harry potter", "j.k rowling", 1990)
book2 = Book("Lord of the rings", "Tolken",1937)
book3 = Book("harry potter", "j.k rowling", 1990)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()

library.remove_book("Lord if the eings")
library.list_books()






class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(f"Current balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: {interest}. New balance: {self.balance}")


account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)
account.get_balance()