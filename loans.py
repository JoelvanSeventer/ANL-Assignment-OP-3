import json
from datetime import datetime as d
from datetime import date, timedelta
import csv

#loan administration class
class LoanAdministration():
    def __init__(self):
        #assign fields
        self.item = LoanItem()
        self.loan_path = 'data/loans.json'
        self.ownedbooks = []
        now = str(d.now())[:10]
        now = now.replace(":","_")
        self.datetime = now

    #view your loaned books
    def Loans(self, username):
        #open json file loans
        with open(self.loan_path, 'r') as f:
            #load loans
            data = json.load(f)
        #if the file is empty, there are no book being loaned
        if len(data) == 0:
            print("No books are being loaned out.")
        # Otherwise, show all books
        else:
            with open("data/loans.json", "r") as g:
                loans = json.load(g)
        
            loaned_books = []

            for book in loans:
                if book["username"].lower() == username.lower():
                    loaned_books.append(book)
            
            for book in loaned_books:
                split_book = list(book["loandate"].split('-'))
                start_date = date(int(split_book[0]), int(split_book[1]), int(split_book[2]))
                end_date = start_date + timedelta(days=60)
                total = str(end_date-start_date).removesuffix(', 0:00:00')
                print("Currently loaned book(s):")
                for book in data:
                    print("Title: " + book["booktitle"])
                    print("Days left: " + total)
    

    def loanStatus(self, username):
        
        with open("data/loans.json", "r") as f:
            loans = json.load(f)
        
        loaned_books = []

        for book in loans:
            if book["username"].lower() == username.lower():
                loaned_books.append(book)
        
        overdue_loan = []
        returning = False

        for book in loaned_books:
            split_book = list(book["loandate"].split('-'))
            start_date = date(int(split_book[0]), int(split_book[1]), int(split_book[2]))
            end_date = start_date + timedelta(days=60)
            
            if date.today() >= end_date:
                overdue_loan.append(book["title"])
                returning = True
        
        if returning:
            print("#####################################################")
            print("##                                                 ##")
            print("##         THESE BOOKS NEED TO BE RETURNED         ##")
            print("##                                                 ##")
            print("#####################################################")

            for book in overdue_loan:
                print("\n", book["booktitle"],", "  "\n")
                print("#####################################################")


    def checkUser(self, username):
        with open("data/members.csv", "r") as f:
            members = list(csv.reader(f))
        
        username_list = []

        for member in members:
            split_user = member[0].split(';')
            username_list.append(split_user[7].lower())

        return username.lower() in username_list

    #view the books loaned by a member
    def view_loaned_books(self):
        #ask for the member
        memName = input("Please enter the username of the member: ").lower()
        #open json file loans
        with open(self.loan_path, 'r') as f:
            #load loans
            data = json.load(f)
        #if the file is empty, there are no book being loaned
        if len(data) == 0:
            print("No books are being loaned out.")
        # Otherwise, show all books
        else:
            print("Currently loaned book(s):")
            for book in data:
                if book["username"] == memName:
                    print(book["title"])

    #loan a book
    def loanBook(self, username):

        #check if max loan amount
        with open("data/loans.json", "r") as f:
            loans = list(json.load(f))
        
        count = 0
        for book in loans:
            if book["username"] == username:
                count += 1
            
        if count >= 3:
            print("\nMax loan limit already reached\n")
            return

        #ask for title
        titleLoan = input("\nPlease enter the title of the book you want to loan: ").lower()

        with open("data/loans.json", "r") as f:
            loans = json.load(f)
        

        for book in loans:

            if book["booktitle"].lower() == titleLoan and book["username"] == username:
                print("\nYou already have this book.")
                return

        
        with open("data/bookcopies.json", "r") as f:
            bookcopies = json.load(f)
        
        bookcopy_titles = []

        for bookcopy in bookcopies:
            bookcopy_titles.append(bookcopy["title"].lower())
        
        if titleLoan not in bookcopy_titles:
            print("\nThis book doesn't exist\n")

        else:
            #loan the book
            book = self.item.loanbook(titleLoan)

            loan_info = {"username":username, "booktitle":book["title"], "loandate":self.datetime}

            #try in case its empty
            try:
                with open("data/loans.json", 'r') as f:
                    data = json.load(f)
            except:
                pass

            #add a book to the loans file
            with open("data/loans.json", "w+") as f:
                data.append(loan_info)
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)

    #return a book you loaned
    def return_this_book(self, username):
        #ask for the title
        titleReturn = input("\nPlease enter the title of the book you want to return: ").lower()
        #return the book
        self.item.returnthisbook(titleReturn, username)
        try:
            self.ownedbooks.remove(titleReturn)
        except:
            pass


#class to loan a book
class LoanItem():
    
    def returnthisbook(self, BookTitle_return, username):
        # load file and add the book back to the file
        item = False
        with open("data/loans.json", 'r') as f:
            data = json.load(f)
        
        for idx, book in enumerate(data):
            if book["booktitle"].lower() == BookTitle_return.lower() and username == book["username"]:
                data.pop(idx)
                item = book
                break


        if item:
            with open('data/loans.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            
            # add to copies json file
            with open("data/bookcopies.json", 'r') as f:
                data = json.load(f)
            
            for book in data:
                if book["title"].lower() == BookTitle_return.lower():
                    book["copies"] += 1

            with open('data/bookcopies.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            
            print(f"You've succesfully returned the book {item['booktitle']}!")
        else:
            print("That book hasn't been loaned out!")


    def loanbook(self, BookTitle_Loan):
        item = False
        #open bookcopies.json, load it and assign it to the variable data
        with open("data/bookcopies.json", 'r') as f:
            data = json.load(f)
        
        for book in data:
            #remove the book from the file if its the book that's going to be loaned
            if BookTitle_Loan == book['title'].lower() and book["copies"] > 0:
                book["copies"] -= 1
                item = book
                break
            elif BookTitle_Loan == book['title'].lower() and book["copies"] == 0:
                print(f"\nThere are no copies of {BookTitle_Loan} available")
                break

        if item:
            with open('data/bookcopies.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)

            print(f"\nYou've succesfully loaned a copy of the book: {item['title']}")
            return item