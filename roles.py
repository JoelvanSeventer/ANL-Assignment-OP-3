from person import Person
import json
from backup import Catalog
from book import Book
from loans import LoanAdministration
from book import BookItem
import csv 

class Librarian():
    def __init__(self):
        self.person = Person()
        self.book = Book()
        self.loan = LoanAdministration()
        self.catalog = Catalog()
        self.bookitem = BookItem()

    def books(self):
        action = input("\n[1] To add a book\n[2] To remove a book\n")
        if action == '1':
            self.book.addBook()
        elif action == '2':
            name = input("\nPlease enter the title of the book you would like to remove:\n")
            self.book.removeBook(name)

    def copies(self):
        action = input("\n[1] To add copies\n[2] To remove copies\n")
        if action == '1':
            self.bookitem.addCopies()
        elif action == '2':
            self.bookitem.removeCopies()

    def customer(self): 
        self.person.addCustomer()

    def searchCustomer(self):
        self.person.searchCustomer()

    def checkLoanStatus(self):
        self.loan.viewLoans()

    def makeBackup(self):
        self.catalog.makeBackup()

    def restoreDB(self):
        self.catalog.restoreDB()
    
    def viewbooks(self):
        self.book.viewBooks()

    def run(self):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n[1] To add or remove a book\n[2] To add or remove copies\n[3] To add customer\n[4] To view all books\n[5] To search a customer\n[6] To check loan status\n[7] To make backup\n[8] To restore database\n[9] Exit\n\nEnter a number: """)

            if action == '1':
                self.books()
            elif action == '2':
                self.copies()
            elif action == '3':
                self.customer()
            elif action == '4':
                self.viewbooks()
            elif action == '5':
                self.searchCustomer()
            elif action == '6':
                self.checkLoanStatus()
            elif action == '7':
                self.makeBackup()
            elif action == '8':
                self.restoreDB()
            elif action == '9':
                running = False
                break

            running = input("\nDo you want to continue y/n: ")
            if running.lower() == "n" or running.lower() == "no":
                running = False

class Subscriber(Person):
    def __init__(self):
        super().__init__()
        self.book = Book()
        self.loan = LoanAdministration()

    def searchBook(self):
        self.book.searchBook()

    def loanBook(self):
        action = input("\n[1] To loan a book\n[2] To return a book\n")
        if action == "1":
            self.loan.loanBook()
        if action == "2":
            self.loan.returnBook()
    
    def checkLoanStatus(self):
        self.loan.viewLoans()
    
    def viewbooks(self):
        self.book.viewBooks()

    def run(self):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n[1] To search a book\n[2] To loan or return a book\n[3] To check loan status\n[4] To view all books\n[5] Exit\n""")
            if action == '1':
                self.searchBook()
            if action == '2':
                self.loanBook()
            if action == '3':
                self.checkLoanStatus()
            if action == '4':
                self.viewbooks()
            if action == '5':
                running = False
                break

            running = input("\nDo you want to continue y/n: ")
            if running.lower() == "n" or running.lower() == "no":
                running = False
                

class Publisher():
    def __init__(self):
        self.book = Book()
        self.librarian = Librarian()
        self.bookitem = BookItem()

    def viewBooks(self):
        self.book.viewBooks()
    
    def books(self):
        self.librarian.books()
    
    def copies(self):
        action = input("\n[1] To add copies\n[2] To remove copies\n")
        if action == '1':
            self.bookitem.addCopies()
        elif action == '2':
            self.bookitem.removeCopies()

    def run(self):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n[1] To view books\n[2] To add or remove a books\n[3] Exit\n""")

            if action == '1':
                self.viewBooks()
            elif action == '2':
                self.books()
            if action == '3':
                running = False
                break

            running = input("\nDo you want to continue y/n: ")
            if running.lower() == "n" or running.lower() == "no":
                running = False