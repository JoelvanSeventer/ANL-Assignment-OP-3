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
        
    #add new member
    def addMember(self): 
        self.person.newMember()
    
    #Load all bookItems
    def viewBooktitles(self):
        self.book.viewBooktitles()

    #find a member
    def findmember(self):
        self.person.findmember()

    #add list of members
    def addListOfMembers(self):
        self.person.addListOfMembers()
    
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




    #To search a bookItem and its availibility
    def searchBookItem(self):
        self.bookitem.searchBookItem()

    def lendBook(self):
        username = input("Please enter the username of the member you would like to lend a book to: ")
        self.loan.loanBook(username)

    #search a book in the catalog
    def searchBook(self):
        self.book.findBook()

    #main method of library admin
    def memberMenu(self):
        print("\n1. Add member\n2. Delete member\n3. Edit member\n4. Show all members\n5. Search member\n6. Add list of members\n7.  Exit -->\n")
        action = input("Enter a number: ")
        if action == '1':
            self.addMember()
        elif action == '2':
            self.deleteMember()
        elif action == '3':
            self.editMember()
        elif action == '4':
            self.showAllMembers()
        elif action == '5':
            self.findmember()
        elif action == '6':
            self.person.addListOfMembers()
        elif action == '7':
            return
        else:
            print("\nInvalid input!\n")
            self.memberMenu()
    
    def catalogMenu(self):
        print("\n1. Add book\n2. Remove book\n3. Edit book\n4. Show all books\n5. Search book\n6. Add a list of books\n7. Exit -->\n")
        action = input("Enter a number: ")
        if action == '1':
            self.book.addNewBook()
        elif action == '2':
            RemoveTitle = input("\nPlease enter the title of the book you would like to remove:\n").lower()
            self.book.removeOldBook(RemoveTitle)
        # Edit Book
        elif action == '3':
            self.book.editBook()
        elif action == '4':
            self.book.viewBooktitles()
        elif action == '5':
            self.book.findBook()
        elif action == '6':
            self.book.addListOfBooks()
        elif action == '7':
            return
        else:
            print("\nInvalid input!\n")
            self.catalogMenu()

    def bookItemMenu(self):
        print("\n1. Add copies\n2. Remove copies\n3. Edit copies\n4. Search bookitem and its availability\n5. Show all copies\n6. Lend a book to a member\n7. Exit -->\n")
        action = input("Enter a number: ")
        if action == '1':
            self.bookitem.addCopies()
        elif action == '2':
            self.bookitem.removeCopies()
        # Edit Copies
        elif action == '3':
            self.bookitem.editCopies()
        elif action == '4':
            self.bookitem.searchBookItem()
        elif action == '5':
            self.bookitem.showAllCopies()
        elif action == '6':
            self.lendBook()
        elif action == '7':
            return
        else:
            print("\nInvalid input!\n")
            self.bookItemMenu()

    def systemAdministrationMenu(self):
        print("\n1. Make backup\n2. Restore backup\n3. Exit -->\n")
        action = input("Enter a number: ")
        if action == '1':
            self.makeBackup()
        elif action == '2':
            self.RestoreBackup()
        elif action == '3':
            return
        else:
            print("\nInvalid input!\n")
            self.systemAdministrationMenu()

    def run(self):
        running = True
        while running:
            print("\nWelcome to the library admin menu.\n")
            action = input("Fill in the menu number to select an option.\n1. Members\n2. Catalog\n3. Book Items\n4. System Administration\n5. Exit\n")
            if action == '1':
                self.memberMenu()
            elif action == '2':
                self.catalogMenu()
            elif action == '3':
                self.bookItemMenu()
            elif action == '4':
                self.systemAdministrationMenu()
            elif action == '5':
                print("\nThank you for using the library admin menu.\n")
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