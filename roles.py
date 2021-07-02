from person import Person
import json
from backup import Catalog
from book import Book
from loans import LoanAdministration
from book import BookItem
import csv 

class Librarian():
    def __init__(self):
        #assign fields
        self.person = Person()
        self.book = Book()
        self.loan = LoanAdministration()
        self.catalog = Catalog()
        self.bookitem = BookItem()

    def books(self):
        action = input("\n1. Add a book\n2. Remove a book\n")
        if action == '1':
            self.book.addNewBook()
        elif action == '2':
            name = input("\nPlease enter the title of the book you would like to remove:\n")
            self.book.removeOldBook(name)

    def copies(self):
        action = input("\n1. Add copies\n2. Remove copies\n")
        if action == '1':
            self.bookitem.addCopies()
        elif action == '2':
            self.bookitem.removeCopies()

    def customer(self): 
        self.person.NewCustomer()

    def findCustomer(self):
        self.person.findCustomer()

    def checkLoanStatus(self):
        self.loan.Loans()

    def makeBackup(self):
        self.catalog.makeBackup()

    def restoreDB(self):
        self.catalog.restoreDB()
    
    def viewBooktitles(self):
        self.book.viewBooktitles()

    def run(self):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n2. Add or remove a book\n2. Add or remove copies\n3. Add customer\n4. View all books\n5. Search a customer\n6. Check loan status\n7. Make backup\n8. Restore data\n9. Exit -->\n\nEnter a number: """)

            if action == '1':
                self.books()
            elif action == '2':
                self.copies()
            elif action == '3':
                self.customer()
            elif action == '4':
                self.viewBooktitles()
            elif action == '5':
                self.findCustomer()
            elif action == '6':
                self.checkLoanStatus()
            elif action == '7':
                self.makeBackup()
            elif action == '8':
                self.restoreDB()
            elif action == '9':
                print("Thanks for visiting! See you next time!")
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

    def findBook(self):
        self.book.findBook()

    def loanBook(self):
        action = input("\n1. Loan a book\n2. Return a book\n")
        if action == "1":
            self.loan.loanBook()
        if action == "2":
            self.loan.return_this_book()
    
    def checkLoanStatus(self):
        self.loan.Loans()
    
    def viewBooktitles(self):
        self.book.viewBooktitles()

    def run(self):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n1. Search a book\n2. Loan or return a book\n3. Check loan status\n4. View all books\n5. Exit -->\n""")
            if action == '1':
                self.findBook()
            if action == '2':
                self.loanBook()
            if action == '3':
                self.checkLoanStatus()
            if action == '4':
                self.viewBooktitles()
            if action == '5':
                print("Thanks for visiting! See you next time!")
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

    def viewBooktitles(self):
        self.book.viewBooktitles()
    
    def books(self):
        self.librarian.books()
    
    def copies(self):
        action = input("\n1. Add copies\n2. Remove copies\n")
        if action == '1':
            self.bookitem.addCopies()
        elif action == '2':
            self.bookitem.removeCopies()

    def run(self):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n1. View books\n2. Add or remove a books\n3. Exit -->\n""")

            if action == '1':
                self.viewBooktitles()
            elif action == '2':
                self.books()
            if action == '3':
                print("Thanks for visiting! See you next time!")
                running = False
                break

            running = input("\nDo you want to continue y/n: ")
            if running.lower() == "n" or running.lower() == "no":
                running = False