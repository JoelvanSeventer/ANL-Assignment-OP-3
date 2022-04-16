import json

#loan administration class
class LoanAdministration():
    def __init__(self):
        #assign fields
        self.item = LoanItem()
        self.loan_path = 'data/loans.json'
        self.ownedbooks = []

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
            for book in data:
                print(book)
    
    #loan a book
    def loanBook(self):
        #ask for title
        titleLoan = input("\nPlease enter the title of the book you want to loan: ").lower()
        if titleLoan in self.ownedbooks:
            print("\nYou already have this book.")
        else:
            self.ownedbooks.append(titleLoan)
            #loan the book
            book = self.item.loanbook(titleLoan)
            data = []

            #try in case its empty
            try:
                with open(self.loan_path, 'r') as f:
                    data = json.load(f)
            except:
                pass

            #add a book to the loans file
            with open(self.loan_path, "w+") as f:
                data.append(book)
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)

    #return a book you loaned
    def return_this_book(self):
        #ask for the title
        titleReturn = input("\nPlease enter the title of the book you want to return: ").lower()
        self.ownedbooks.remove(titleReturn)
        #return the book
        self.item.returnthisbook(titleReturn)


#class to loan a book
class LoanItem():
    
    def returnthisbook(self, BookTitle_return):
        # load file and add the book back to the file
        item = False
        with open("data/loans.json", 'r') as f:
            data = json.load(f)
        
        for idx, book in enumerate(data):
            if BookTitle_return == book['title'].lower():
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

            with open('data/bookcopies.json', "w+") as f:
                data.append(item)
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            
            print(f"You've succesfully returned the book {item['title']}!")
        else:
            print("That book hasn't been loaned out!")


    def loanbook(self, BookTitle_Loan):
        item = False
        #open bookcopies.json, load it and assign it to the variable data
        with open("data/bookcopies.json", 'r') as f:
            data = json.load(f)
        
        for idx, book in enumerate(data):
            #remove the book from the file if its the book that's going to be loaned
            if BookTitle_Loan == book['title'].lower():
                data.pop(idx)
                item = book
                break
        #if there's a book left
        if item:
            with open('data/bookcopies.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            print(f"\nYou've succesfully loaned the book {item['title']}")
            return item
        #when there are no copies to loan
        print(f"\nThere are no copies of {BookTitle_Loan} available")