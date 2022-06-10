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

    #add, remove or edit a book from the library(json file)
    def AddRemoveOrEditBook(self):
        action = input("\n1. Add a book\n2. Remove a book\n3. Edit a book\n")
        if action == '1':
            self.book.addNewBook()
        elif action == '2':
            RemoveTitle = input("\nPlease enter the title of the book you would like to remove:\n")
            self.book.removeOldBook(RemoveTitle)
        # Edit Book
        elif action == '3':
            self.book.editBook()

    #Add, Remove or edit copies
    def copies(self):
        action = input("\n1. Add copies\n2. Remove copies\n3. Edit copies\n")
        if action == '1':
            self.bookitem.addCopies()
        elif action == '2':
            self.bookitem.removeCopies()
        # Edit Copies
        elif action == '3':
            self.bookitem.editCopies()

    #add new member
    def addMember(self): 
        self.person.newMember()
    
    #Load all bookItems
    def viewBooktitles(self):
        self.book.viewBooktitles()

    #find a member
    def findmember(self):
        self.person.findmember()
    
    #check the loan status
    def checkLoanStatus(self):
        self.loan.view_loaned_books()

    #make a backup
    def makeBackup(self):
        self.catalog.makeBackup()

    #restore the backup
    def RestoreBackup(self):
        self.catalog.RestoreBackup()

    #delete a member
    def deleteMember(self):
        self.person.deletemember()

    #show all members
    def showAllMembers(self):
        self.person.showAllmembers()
    
    #edit a member
    def editMember(self):
        self.person.editmember()


    #Load and Add list of members (all at once)
    
    #Load and Add list of books (all at once)

    #To search a bookItem and its availibility
    def searchBookItem(self):
        self.bookitem.searchBookItem()

    def lendBook(self):
        username = input("Please enter the username of the member you would like to lend a book to: ")
        self.loan.loanBook(username)

    def searchBook(self):
        self.book.findBook()

    #main method of library admin
    def run(self):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n1. Add, remove or edit a book\n2. Add, remove or edit copies\n3. Add member\n4. View all books\n5. Search a member\n6. Check loan status\n7. Make backup\n8. Restore data\n9. Delete a member\n10. Show all members\n11. Edit member\n12. Search a book item and its availibility\n13. Lend a book to a member\n14. Exit -->\n\nEnter a number: """)

            if action == '1':
                self.AddRemoveOrEditBook()
            elif action == '2':
                self.copies()
            elif action == '3':
                self.addMember()
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
                self.searchBookItem()
            elif action == '13':
                self.lendBook()
            elif action == '14':
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
    def loanBook(self, username):
        action = input("\n1. Loan a book\n2. Return a book\n")
        if action == "1":
            self.loan.loanBook(username)
        if action == "2":
            self.loan.return_this_book()
    
    #check loan status
    def checkLoanStatus(self):
        self.loan.Loans()
    

    #main function of member
    def run(self, username):
        running = True
        while running:
            action = input("""\nFill in the action you want to execute:\n1. Search a book\n2. Loan or return a book\n3. Check loan status\n4. View all books\n5. Exit -->\n""")
            if action == '1':
                self.findBook()
            if action == '2':
                self.loanBook(username)
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