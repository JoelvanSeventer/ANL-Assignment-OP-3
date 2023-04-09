import json
import os

class Book():
    def addNewBook(self):
        
        print("To add a book fill in the following.")
        author = input("Author: ")
        country = input("Country: ")
        imagelink = input("ImageLink: ")
        language = input("Language: ")
        link = input("Link: ")
        
        running = True
        while running:
            invalidInput = False
            pages = input("Pages: ")

            if not pages.isnumeric():
                invalidInput = True
                print("\nInvalid input")
                print("Please enter an integer\n")
            
            if invalidInput == False:
                pages = int(pages)
                running = False

        running = True
        while running:
            isUnique = True
            title = input("Title: ")

            with open("data/books.json", "r") as f:
                oldData = json.load(f)

            for book in oldData:
                if title.lower() == book["title"].lower():
                    isUnique = False
                    print("\nA book with this title already exists!")
                    print("Please enter a unique book title:\n")
                    break

            if isUnique:
                break

            
        isbn = input("ISBN: ")

        running = True
        while running:
            invalidInput = False
            year = input("Year: ")

            if not year.isnumeric():
                invalidInput = True
                print("\nInvalid input")
                print("Please enter an integer\n")
            
            if invalidInput == False:
                year = int(year)
                running = False

        #Add book to json file
        
        data = {"author":author, "country":country, "imageLink":imagelink, "language":language, "link":link, "pages":pages, "title":title, "ISBN":isbn, "year":year}
        with open("data/books.json", "r") as f:
            oldData = json.load(f)
        with open("data/books.json", "w+") as f:
            oldData.append(data)
            jsoned_data = json.dumps(oldData, indent=True)
            f.write(jsoned_data)

        #Add copies to json file
        print("Succesfully added the book!")
        self.addCopies(5, data)
    
    def addCopies(self, amount, data):

        data["copies"] = amount

        
        with open("data/bookcopies.json", "r") as f:
            book_copies = json.load(f)


        with open("data/bookcopies.json", "w+") as f:
            book_copies.append(data)
            jsoned_data = json.dumps(book_copies, indent=True)
            f.write(jsoned_data)
            print(f"\nSuccesfully added {amount} copies\n")
        
        

    def removeOldBook(self, name):

        item = False
        with open("data/books.json", 'r') as f:
            data = json.load(f)
            
        for idx, book in enumerate(data):
            if name.lower() == book["title"].lower():
                data.pop(idx)
                item = book
            
        if item:
            print("\nRemoving book...\n")

            with open("data/books.json", "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
                #Remove the copies
                print("\nRemoving copies...\n")
                self.removeAllCopies(name)
            print(f"\nYou've succesfully removed the book {item['title']} and all of its copies.")

        else:
            print("\nThis book does not exist!")

    def removeAllCopies(self, title):

        item = False

        with open("data/bookcopies.json", 'r') as f:
            data = json.load(f)
        
        for idx, book in enumerate(data):
            if title.lower() == book["title"].lower():
                data.pop(idx)
                item = book
                break

        if item:
            with open("data/bookcopies.json", "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)


    def editBook(self, inputEdit, title, newValue):
        with open("data/books.json", "r") as f:
                    data = json.load(f)     
        for book in data:
            if title == book["title"].lower():            

                if inputEdit == "1":
                    book["author"] = newValue
                    print("\nBook edited\n")
                    BookItem.editCopies(self, inputEdit, title, newValue)
                    break

                elif inputEdit == "2":
                    book["country"] = newValue
                    print("\nBook edited\n")
                    BookItem.editCopies(self, inputEdit, title, newValue)
                    break

                elif inputEdit == "3":
                    book["imageLink"] = newValue
                    print("\nBook edited\n")
                    BookItem.editCopies(self, inputEdit, title, newValue)
                    break

                elif inputEdit == "4":
                    book["language"] = newValue
                    print("\nBook edited\n")
                    BookItem.editCopies(self, inputEdit, title, newValue)
                    break

                elif inputEdit == "5":
                    book["link"] = newValue
                    print("\nBook edited\n")
                    BookItem.editCopies(self, inputEdit, title, newValue)
                    break

                elif inputEdit == "6":
                    book["pages"] = int(newValue)
                    print("\nBook edited\n")
                    BookItem.editCopies(self, inputEdit, title, newValue)
                    break

                elif inputEdit == "7":
                    book["title"] = newValue
                    print("\nBook edited\n")
                    BookItem.editCopies(self, inputEdit, title, newValue)
                    break

                elif inputEdit == "8":
                    book["year"] = int(newValue)
                    print("\nBook edited\n")
                    BookItem.editCopies(self, inputEdit, title, newValue)
                    break

                elif inputEdit == "9":
                    break

            
        with open("data/books.json", "w+") as f:
            jsoned_data = json.dumps(data, indent=True)
            f.write(jsoned_data)

        print("\n\nSuccesfully edited the copies of the book!\n\n")

    def viewBooktitles(self):
        #View all booktitles
        with open("data/books.json", "r") as f:
            data = json.load(f)

        for book in data:
            print(book["title"])
    
    def findBook(self):
        #Search for a book
        with open("data/bookcopies.json", "r") as g:
            datacopies = json.load(g)
        print("\nWith which term would you like to search?\n")
        running = True
        while running:
            wrongInput = False
            searchterm = input("1. Author\n2. Title\n").lower()

            if searchterm != "1" and searchterm != "2":
                wrongInput = True
                print("\nInvalid input\n")
                print("Please enter a valid input:\n")

            if wrongInput == False:
                running = False
        
        if searchterm == "1":
            searchvalue = input("\nPlease enter an author: \n")
        else:
            searchvalue = input("\nPlease enter a title: \n")
            
        found = False
        for book in datacopies: # book in data and 
            if searchterm == "1" and (searchvalue.lower() == book["author"].lower() or searchvalue.lower() in book["author"].lower()):
                    found = True
                    print(f"\nAuthor: {book['author']}\nCountry: {book['country']}\nImageLink: {book['imageLink']}\nLanguage: {book['language']}\nLink: {book['link']}Pages: {book['pages']}\nTitle: {book['title']}\nISBN: {book['ISBN']}\nYear: {book['year']}\n")
                    
                    print(f"Available copies: {book['copies']}")
            elif searchterm == "2" and (searchvalue.lower() == book["title"].lower() or searchvalue.lower() in book["title"].lower()):
                    found = True
                    print(f"\nAuthor: {book['author']}\nCountry: {book['country']}\nImageLink: {book['imageLink']}\nLanguage: {book['language']}\nLink: {book['link']}Pages: {book['pages']}\nTitle: {book['title']}\nISBN: {book['ISBN']}\nYear: {book['year']}\n")


        if found == False:
            print("This book or author does not exist")

    #add list of books
    def addListOfBooks(self):
        filename = input("\nPlease enter the name of the file you want to add(for example: 'addbooks.json'): ")
        filepath = self.findfile(filename, "/")
        
        if filepath != "Not found":
            with open(filepath, "r") as f:
                data = json.load(f)

            with open("data/books.json", "r") as f:
                oldData = json.load(f)

            count = 0
            found = False
            for book in data:
                for oldBook in oldData:
                    if book == oldBook:
                        found = True
                if found == False:
                    oldData.append(book)
                    self.addCopies(5, book)
                    count += 1
                    print(f"{book['title']} has been added to the database.\n")
                else:
                    print(f"The title {book['title']} already exists in the database.\n")


            if count == 0:
                print("There are no new books in the file!!")
                print("\nAll the books from the file already exit in the database.")
            else:      
                with open("data/books.json", "w+") as f:
                    jsoned_data = json.dumps(oldData, indent=True)
                    f.write(jsoned_data)
                print(f"\n{count} books have been added to the database.")


    
    def findfile(self, name, path):
        global filepath
        print("\nSearching for file...")
        for dirpath, dirnames, filename in os.walk(path):
            if name in filename:
                print("\nFile found!")
                filepath = os.path.join(dirpath, name)
                return filepath
        print("\nNo file found with that name.")
        return "Not found"

class BookItem():
    def __init__(self):
        self.book = Book()
    
    def addCopies(self):
        check = False
        running = True

        title = input("\nPlease enter the title of the book you would like to make copies of:\n").lower()

        with open("data/bookcopies.json", "r") as f:
            alldata = json.load(f)

        while running:
            exists = False

            for book in alldata:
                if book["title"].lower() == title:
                    exists = True
                    break
            
            if exists:
                running = False
            else:
                print("\nThat book doesn't exist.")
                print("Please enter a existing book:\n")

        running = True
        while running:
            invalidInput = False
            amount = input("\nPlease enter the amount of copies you would like to make:\n")

            if not amount.isnumeric():
                invalidInput = True
                print("\nInvalid input")
                print("Please enter an integer\n")
            
            if invalidInput == False:
                amount = int(amount)
                running = False


        for book in alldata:
            if title == book["title"].lower():
                book["copies"] += amount
                check = True
                break

        with open("data/bookcopies.json", "w+") as f:
            jsoned_data = json.dumps(alldata, indent=True)
            f.write(jsoned_data)
            print(f"\nSuccesfully added {amount} copies\n")

        if check == False:
            print("That book does not exist")

    
        
    def removeCopies(self):
        title = input("\nPlease enter the title of the book you want to remove copies from:\n")
        copies = int(input("\nEnter the amount of copies you want to remove:\n"))
        bookitemFound = False
        count = 0
        with open("data/bookcopies.json", 'r') as f:
            data = json.load(f)
        
        for bookitem in data:
            if bookitem["title"].lower() == title.lower():
                bookitemFound = True
                if copies > bookitem["copies"]:
                    bookitem["copies"] = 0
                    break
                else:
                    bookitem["copies"] -= copies
                    break
               
        if bookitemFound:
            print("\nRemoving copies...\n")

            with open('data/bookcopies.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            print(f"You've succesfully removed the copies of the book")
        else:
            print("This book does not have any copies")


    def editCopies(self, inputEdit, title, newValue):   
        with open("data/bookcopies.json", "r") as f:
                    data = json.load(f)     
        for book in data:
            if title == book["title"].lower():            

                if inputEdit == "1":
                    book["author"] = newValue
                    break

                elif inputEdit == "2":
                    book["country"] = newValue
                    break

                elif inputEdit == "3":
                    book["imageLink"] = newValue
                    break

                elif inputEdit == "4":
                    book["language"] = newValue
                    break

                elif inputEdit == "5":
                    book["link"] = newValue
                    break

                elif inputEdit == "6":
                    book["pages"] = int(newValue)
                    break

                elif inputEdit == "7":
                    book["title"] = newValue
                    break

                elif inputEdit == "8":
                    book["year"] = int(newValue)
                    break

                elif inputEdit == "9":
                    break

            
        with open("data/bookcopies.json", "w+") as f:
            jsoned_data = json.dumps(data, indent=True)
            f.write(jsoned_data)

        print("\n\nSuccesfully edited the copies of the book!\n\n")


    def searchBookItem(self):
        #search a book item and check its availibility
        with open("data/bookcopies.json", "r") as f:
            books = json.load(f)

        found = False
        Enter = input("\nPlease enter the title of the book you would like to search for:\n").lower()

        for book in books:

            if book["copies"] > 0 and (Enter == book["title"].lower() or Enter in book["title"].lower()):
                amount_of_copies = book["copies"]
                found = True

        if found == False:
            print("This bookcopy is not available")

        elif found == True:
            print(f"There are {amount_of_copies} copies of this book available.")
    
    #show all copies
    def showAllCopies(self):
        with open("data/bookcopies.json", "r") as f:
            data = json.load(f)
        for book in data:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Copies: {book['copies']}\n")
                
