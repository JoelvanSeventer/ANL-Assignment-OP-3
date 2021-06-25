import json

class LoanItem():
    def loanbook(self, word):
        item = False
        with open("database/bookcopies.json", 'r') as f:
            data = json.load(f)
        
        for idx, book in enumerate(data):

            if word == book['title'].lower():
                data.pop(idx)
                item = book
                break
        if item:
            with open('database/bookcopies.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            print(f"\nYou've succesfully loaned the book {item['title']}")
            return item
        print(f"\nThere are no copies of {word} available")

    def returnbook(self, word):
        # load and remove from
        item = False
        with open("database/loans.json", 'r') as f:
            data = json.load(f)
        
        for idx, book in enumerate(data):
            
            if word == book['title'].lower():
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

class LoanAdministration():
    def __init__(self):
        self.item = LoanItem()
        self.loan_path = 'database/loans.json'

    def loanBook(self):
        word = input("\nPlease enter the title of the book you want to loan: ").lower()
        book = self.item.loanbook(word)
        data = []
        try:
            with open(self.loan_path, 'r') as f:
                data = json.load(f)
        except:
            pass

        with open(self.loan_path, "w+") as f:
            data.append(book)
            jsoned_data = json.dumps(data, indent=True)
            f.write(jsoned_data)
        
    def returnBook(self):
        word = input("\nPlease enter the title of the book you want to return: ").lower()

        self.item.returnbook(word)

    def viewLoans(self):
        with open(self.loan_path, 'r') as f:
            data = json.load(f)
        if len(data) == 0:
            print("No books are being loaned out.")
        else:
            for book in data:
                print(book)