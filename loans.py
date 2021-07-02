import json

#loan administration class
class LoanAdministration():
    def __init__(self):
        #assign fields
        self.item = LoanItem()
        self.loan_path = 'database/loans.json'

    #view the loaned books
    def viewLoans(self):
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
    def returnBook(self):
        #ask for the title
        titleReturn = input("\nPlease enter the title of the book you want to return: ").lower()

        #return the book
        self.item.returnthisbook(titleReturn)


#class to loan a book
class LoanItem():
    
    def returnthisbook(self, BookTitle_return):
        # load and remove from
        item = False
        with open("database/loans.json", 'r') as f:
            data = json.load(f)
        
        for idx, book in enumerate(data):
            
            if BookTitle_return == book['title'].lower():
                data.pop(idx)
                item = book
                break

        if item:
            with open('database/loans.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            
            # add to books json
            with open("database/bookcopies.json", 'r') as f:
                data = json.load(f)

            with open('database/bookcopies.json', "w+") as f:
                data.append(item)
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            
            print(f"You've succesfully returned the book {item['title']}!")
        else:
            print("That book hasn't been loaned out!")


    def loanbook(self, BookTitle_Loan):
        item = False
        #open bookcopies.json, load it and assign it to the variable data
        with open("database/bookcopies.json", 'r') as f:
            data = json.load(f)
        
        for idx, book in enumerate(data):

            if BookTitle_Loan == book['title'].lower():
                data.pop(idx)
                item = book
                break
        if item:
            with open('database/bookcopies.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            print(f"\nYou've succesfully loaned the book {item['title']}")
            return item
        print(f"\nThere are no copies of {BookTitle_Loan} available")