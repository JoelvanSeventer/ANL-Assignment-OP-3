import json

class Book():
    def addBook(self):

        print("To add book fill in the following.")
        author = input("Author: ")
        country = input("Country: ")
        imagelink = input("ImageLink: ")
        language = input("Language: ")
        link = input("Link: ")
        pages = int(input("Pages: "))
        title = input("Title: ")
        year = int(input("Year: "))
        copies = int(input("Amount of copies: "))

        #add to books.json
        data = {"author":author, "country":country, "imagelink":imagelink, "language":language, "link":link, "pages":pages, "title":title, "year":year}
        with open("database/books.json", "r") as f:
            oldData = json.load(f)
        with open("database/books.json", "w+") as f:
            oldData.append(data)
            jsoned_data = json.dumps(oldData, indent=True)
            f.write(jsoned_data)

        #add to bookcopies.json
        self.addCopies(copies, data)

    def removeBook(self, name):
        #remove book
        item = False
        with open("database/books.json", 'r') as f:
            data = json.load(f)
        

        for idx, book in enumerate(data):
                if name == book['title'].lower():
                    data.pop(idx)
                    item = book
            
        if item:
            with open('database/books.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            print(f"\nYou've succesfully removed the book {item['title']}.")
        else:
            print("\nThis book doesn't exist!")

        #remove copies
        self.removeCopies(name, 2)
    
    def addCopies(self, copies, data):
        
        for i in range(copies):
            with open("database/bookcopies.json", "r") as f:
                oldData = json.load(f)

            with open("database/bookcopies.json", "w+") as f:
                oldData.append(data)
                jsoned_data = json.dumps(oldData, indent=True)
                f.write(jsoned_data)

    def removeCopies(self, title, copies):
        item = False
        count = 0
        with open("database/bookcopies.json", 'r') as f:
            data = json.load(f)
        
        if copies == 1:
            for idx, book in enumerate(data):
                if title == book['title'].lower():
                    data.pop(idx)
                    item = book
                    count+= 1
                    break
                    
        if copies > 1:
            for i in range(len(data)):
                for idx, book in enumerate(data):
                        if title == book['title'].lower():
                            data.pop(idx)
                            item = book
                            count+= 1
        if item:
            with open('database/bookcopies.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            print(f"You've succesfully removed {count} copies of the book {item['title']}.")
        else:
            print("This book doesn't exist!")

    def viewBooks(self):
        with open("database/books.json", 'r') as f:
            data = json.load(f)

        for book in data:
            print(book['title'])
    
    def searchBook(self):
        with open('database/books.json', 'r') as f:
            data = json.load(f)
        subject = input("\nVia what term would you like to search? Author, Country, Imagelink, Language, Link, Pages, Title or Year:\n\nEnter term: ").lower()
        content = input(f"\nPlease enter the {subject}:\n").lower()
        found = False
        for book in data:
            if subject == 'author':
                if content == book["author"].lower():
                    found = True
                    print(book)

            if subject == 'country':
                if content == book["country"].lower():
                    found = True
                    print(book)

            if subject == 'imagelink':
                if content == book["imageLink"].lower():
                    found = True
                    print(book)
            
            if subject == 'language':
                if content == book["language"].lower():
                    found = True
                    print(book)

            if subject == "link":
                if content == book["link"].lower():
                    found = True
                    print(book)

            if subject == "pages":
                if int(content) == book["pages"]:
                    found = True
                    print(book)

            if subject == "title":
                if content == book["title"].lower():
                    found = True
                    print(book)

            if subject == "year":
                if int(content) == book["year"]:
                    found = True
                    print(book)

        if found == False:
            print("This book doesn't exist!")

class BookItem():
    def __init__(self):
        self.book = Book()
    
    def addCopies(self):
        check = False
        title = input("\nPlease enter the title of the book you would like to make copies of:\n").lower()
        amount = int(input("\nPlease enter the amount of copies you would like to make:\n"))

        with open("database/books.json", 'r') as f:
            alldata = json.load(f)

        for book in alldata:
            if title == book['title'].lower():
                data = book
                check = True
                self.book.addCopies(amount, data)
                print(f"Succesfully added {amount} copies of the book {book['title']}")
                break

        if not check:
            print("That book doesn't exist!")
        
    def removeCopies(self):
        title = input("\nPlease enter the title of the book:\n").lower()
        running = True
        while running:
            amount = int(input("\nPlease enter the amount of copies you would like to remove:\n"))
            if amount > 0:
                self.book.removeCopies(title, amount)
                running = False
                break
            else:
                print("Please a number higher than 0.")