import json
from datetime import datetime as d

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

    #view the loaned books
    def Loans(self):
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
                print(book["title"])
    
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
        #ask for title
        titleLoan = input("\nPlease enter the title of the book you want to loan: ").lower()

        with open("data/bookcopies.json", "r") as f:
            bookcopies = list(json.load(f))
        
        booktitles = []

        for book in bookcopies:
            booktitles.append(book["title"].lower())
        
        if titleLoan in self.ownedbooks and titleLoan in booktitles:
            print("\nYou already have this book.")
        
        elif titleLoan not in booktitles:
            print("\nThis book doesn't exist\n")

        else:
            self.ownedbooks.append(titleLoan)
            #loan the book
            book = self.item.loanbook(titleLoan)
            data = []

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