from person import Person
import json
from backup import Catalog
from book import Book
from loans import LoanAdministration
from book import BookItem
import csv 

class LibraryAdmin():
    def __init__(self):
        #assign fields
        self.person = Person()
        self.book = Book()
        self.loan = LoanAdministration()
        self.catalog = Catalog()
        self.bookitem = BookItem()

    #add or remove a book from the library(json file)
    def AddOrRemoveBook(self):
        action = input("\n1. Add a book\n2. Remove a book\n")
        if action == '1':
            self.book.addNewBook()
        elif action == '2':
            RemoveTitle = input("\nPlease enter the title of the book you would like to remove:\n")
            self.book.removeOldBook(RemoveTitle)
        # Edit Book
        #
        #
        #

    #Add or Remove copies
    def copies(self):
        action = input("\n1. Add copies\n2. Remove copies\n")
        if action == '1':
            self.bookitem.addCopies()
        elif action == '2':
            self.bookitem.removeCopies()
        # Edit Copies
        #
        #
        #

    #add new member
    def addMember(self): 
        self.person.addMember()

    #find a member
    def findmember(self):
        self.person.findmember()

    #delete a member
    def deleteMember(self):
        self.person.deletemember()

    #show all members
    def showAllMembers(self):
        self.person.showAllmembers()
    
    #edit a member
    def editMember(self):
        self.person.editmember()

    #check the loan status
    def checkLoanStatus(self):
        self.loan.Loans()

    #Load and Add list of members (all at once)
    
    #Load and Add list of books (all at once)

    #Load all bookItems

    #To search a bookItem and its availibility

    def lendBook(self):
        self.loan.loanBook()

    def searchBook(self):
        self.book.findBook()

    #make a backup
    def makeBackup(self):
        self.catalog.makeBackup()

    #restore the backup
    def RestoreBackup(self):
        self.catalog.RestoreBackup()
    
    #view all book titles 
    def viewBooktitles(self):
        self.book.viewBooktitles()

    #main method of library admin
    def run(self):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n1. Add or remove a book\n2. Add or remove copies\n3. Add member\n4. View all books\n5. Search a member\n6. Check loan status\n7. Make backup\n8. Restore data\n9. Delete a member\n10. Show all members\n11. Edit member\n12. Exit -->\n\nEnter a number: """)

            if action == '1':
                self.AddOrRemoveBook()
            elif action == '2':
                self.copies()
            elif action == '3':
                self.member()
            elif action == '4':
                self.viewBooktitles()
            elif action == '5':
                self.findmember()
            elif action == '6':
                self.checkLoanStatus()
            elif action == '7':
                self.makeBackup()
            elif action == '8':
                self.RestoreBackup()
            elif action == '9':
                self.deleteMember()
            elif action == '10':
                self.showAllMembers()
            elif action == '11':
                self.editMember()
            elif action == '12':
                print("Thanks for visiting! See you next time!")
                running = False
                break

            running = input("\nDo you want to continue y/n: ")
            if running.lower() == "n" or running.lower() == "no":
                running = False

class Member(Person):
    def __init__(self):
        #assign fields
        super().__init__()
        self.book = Book()
        self.loan = LoanAdministration()

    #view all booktitles
    def viewBooktitles(self):
        self.book.viewBooktitles()

    #find book
    def findBook(self):
        self.book.findBook()

    #Load all bookItems


    #To search a bookItem and its availibility
    

    #make a loan or return a book
    def loanBook(self):
        action = input("\n1. Loan a book\n2. Return a book\n")
        if action == "1":
            self.loan.loanBook()
        if action == "2":
            self.loan.return_this_book()
    
    #check loan status
    def checkLoanStatus(self):
        self.loan.Loans()
    

    #main function of member
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