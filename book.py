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
        pages = int(input("Pages: "))
        title = input("Title: ")
        isbn = input("ISBN: ")
        year = int(input("Year: "))

        #Add book to json file
        
        data = {"author":author, "country":country, "imagelink":imagelink, "language":language, "link":link, "pages":pages, "title":title, "ISBN":isbn, "year":year}
        with open("data/books.json", "r") as f:
            oldData = json.load(f)
        with open("data/books.json", "w+") as f:
            oldData.append(data)
            jsoned_data = json.dumps(oldData, indent=True)
            f.write(jsoned_data)

        #Add copies to json file
        
        self.addCopies(3, data)
            

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

        if item:
            with open("data/bookcopies.json", "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)


    def editBook(self):
        bookName = input("\nFill in the name of the book you want to edit: ").lower()
        with open("data/books.json", "r") as f:
            data = json.load(f)
        for book in data:
            if bookName == book["title"].lower():
                oldAuthor = book["author"]
                oldCountry = book["country"]
                oldImageLink = book["imageLink"]
                oldLanguage = book["language"]
                oldLink = book["link"]
                oldPages = book["pages"]
                oldTitle = book["title"]
                oldYear = book["year"]
                
                for index, book in enumerate(data):
                    if bookName == book["title"].lower():
                        break

                print("What do you want to edit?\n")
                inputEdit = input("\n1. author\n2. country\n3. imagelink\n4. language\n5. link\n6. pages\n7. title\n8. year\n")
                with open("data/books.json", "r") as f:
                    oldData = json.load(f)
                if inputEdit == "1":
                    newAuthor = input("\nNew author: ")
                    newData = {"author":newAuthor, "country":oldCountry, "imageLink":oldImageLink, "language":oldLanguage, "link":oldLink, "pages":oldPages, "title":oldTitle, "year":oldYear}
                    with open("data/books.json", "w+") as f:
                        oldData[index] = newData
                        jsoned_data = json.dumps(oldData, indent=True)
                        f.write(jsoned_data)
                        
                elif inputEdit == "2":
                    newCountry = input("\nNew country: ")
                    newData = {"author":oldAuthor, "country":newCountry, "imageLink":oldImageLink, "language":oldLanguage, "link":oldLink, "pages":oldPages, "title":oldTitle, "year":oldYear}
                    with open("data/books.json", "w+") as f:
                        oldData[index] = newData
                        jsoned_data = json.dumps(oldData, indent=True)
                        f.write(jsoned_data)

                elif inputEdit == "3":
                    newImageLink = input("\nNew imageLink: ")
                    newData = {"author":oldAuthor, "country":oldCountry, "imageLink":newImageLink, "language":oldLanguage, "link":oldLink, "pages":oldPages, "title":oldTitle, "year":oldYear}
                    with open("data/books.json", "w+") as f:
                        oldData[index] = newData
                        jsoned_data = json.dumps(oldData, indent=True)
                        f.write(jsoned_data)

                elif inputEdit == "4":
                    newLanguage = input("\nNew language: ")
                    newData = {"author":oldAuthor, "country":oldCountry, "imagelink":oldImageLink, "language":newLanguage, "link":oldLink, "pages":oldPages, "title":oldTitle, "year":oldYear}
                    with open("data/books.json", "w+") as f:
                        oldData[index] = newData
                        jsoned_data = json.dumps(oldData, indent=True)
                        f.write(jsoned_data)

                elif inputEdit == "5":
                    newLink = input("\nNew link: ")
                    newData = {"author":oldAuthor, "country":oldCountry, "imagelink":oldImageLink, "language":oldLanguage, "link":newLink, "pages":oldPages, "title":oldTitle, "year":oldYear}
                    with open("data/books.json", "w+") as f:
                        oldData[index] = newData
                        jsoned_data = json.dumps(oldData, indent=True)
                        f.write(jsoned_data)

                elif inputEdit == "6":
                    newPages = int(input("\nNew pages: "))
                    newData = {"author":oldAuthor, "country":oldCountry, "imagelink":oldImageLink, "language":oldLanguage, "link":oldLink, "pages":newPages, "title":oldTitle, "year":oldYear}
                    with open("data/books.json", "w+") as f:
                        oldData[index] = newData
                        jsoned_data = json.dumps(oldData, indent=True)
                        f.write(jsoned_data)

                elif inputEdit == "7":
                    newTitle = input("\nNew title: ")
                    newData = {"author":oldAuthor, "country":oldCountry, "imagelink":oldImageLink, "language":oldLanguage, "link":oldLink, "pages":oldPages, "title":newTitle, "year":oldYear}
                    with open("data/books.json", "w+") as f:
                        oldData[index] = newData
                        jsoned_data = json.dumps(oldData, indent=True)
                        f.write(jsoned_data)

                elif inputEdit == "8":
                    newYear = int(input("\nNew year: "))
                    newData = {"author":oldAuthor, "country":oldCountry, "imagelink":oldImageLink, "language":oldLanguage, "link":oldLink, "pages":oldPages, "title":oldTitle, "year":newYear}
                    with open("data/books.json", "w+") as f:
                        oldData[index] = newData
                        jsoned_data = json.dumps(oldData, indent=True)
                        f.write(jsoned_data)
                


    def addCopies(self, copies, data):
        
        for i in range(copies):
            with open("data/bookcopies.json", "r") as f:
                oldData = json.load(f)

            with open("data/bookcopies.json", "w+") as f:
                oldData.append(data)
                jsoned_data = json.dumps(oldData, indent=True)
                f.write(jsoned_data)

    def removeCopies(self, title, copies):
        item = False
        count = 0
        with open("data/bookcopies.json", 'r') as f:
            data = json.load(f)
        
        if copies == 1:
            for idx, book in enumerate(data):
                if title.lower() == book['title'].lower():
                    data.pop(idx)
                    item = book
                    break
                    
        if copies > 1:
            for i in range(copies):
                for idx, book in enumerate(data):
                    if title.lower() == book['title'].lower():
                        data.pop(idx)
                        item = book
                        break

        if item:
            print("\nRemoving copies...\n")

            with open('data/bookcopies.json', "w+") as f:
                jsoned_data = json.dumps(data, indent=True)
                f.write(jsoned_data)
            print(f"You've succesfully removed the copies of the book")
        else:
            print("This book does not have any copies")


    def viewBooktitles(self):
        #View all booktitles
        with open("data/books.json", "r") as f:
            data = json.load(f)

        for book in data:
            print(book["title"])
    
    def findBook(self):
        #Search for a book
        with open("data/books.json", "r") as f:
            data = json.load(f)
        subject = input("\nWith which term would you like to search? Author, Country, Imagelink, Language, Link, Pages, Title or Year:\n\nEnter term: ").lower()
        content = input(f"\nPlease enter the {subject}:\n").lower()
        found = False
        for book in data:
            if subject == "author" and content == book["author"].lower():
                    found = True
                    print(book)

            if subject == "country" and content == book["country"].lower():
                    found = True
                    print(book)

            if subject == "imagelink" and content == book["imageLink"].lower():
                    found = True
                    print(book)
            
            if subject == "language" and content == book["language"].lower():
                    found = True
                    print(book)

            if subject == "link" and content == book["link"].lower():
                    found = True
                    print(book)

            if subject == "pages" and int(content) == book["pages"]:
                    found = True
                    print(book)

            if subject == "title" and content == book["title"].lower():
                    found = True
                    print(book)

            if subject == "year" and int(content) == book["year"]:
                    found = True
                    print(book)

        if found == False:
            print("This book does not exist")

    #add list of books
    def addListOfBooks(self):
        filename = input("\nPlease enter the name of the file you want to add(for example: 'addbooks.json'):")
        filepath = self.findfile(filename, "/")
        with open(filepath, "r") as f:
            data = json.load(f)
        for book in data:
            data.append(book)
        with open("data/books.json", "w+") as f:
            for books in data:
                jsoned_data = json.dumps(books, indent=True)
                f.write(jsoned_data)
        print("\nThe books from the file have been added to the database.")
    
    def findfile(self, name, path):
        global filepath
        print("\nSearching for file...")
        for dirpath, dirnames, filename in os.walk(path):
            if name in filename:
                print("\nFile found!")
                filepath = os.path.join(dirpath, name)
                return filepath
        return "newbooks"

class BookItem():
    def __init__(self):
        self.book = Book()
    
    def addCopies(self):
        check = False
        title = input("\nPlease enter the title of the book you would like to make copies of:\n").lower()
        amount = int(input("\nPlease enter the amount of copies you would like to make:\n"))

        with open("data/books.json", "r") as f:
            alldata = json.load(f)

        for book in alldata:
            if title == book["title"].lower():
                data = book
                check = True
                self.book.addCopies(amount, data)
                print(f"Succesfully added the copies of the book")
                break

        if not check:
            print("That book does not exist")
        
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
                print("Please enter a number higher than 0.")


    def readAndWrite(self, index, newBook):
        with open("data/bookcopies.json", "r") as f:
            oldData = json.load(f)
        with open("data/bookcopies.json", "w+") as f:
            oldData[index] = newBook
            jsoned_data = json.dumps(oldData, indent=True)
            f.write(jsoned_data)

    def editCopies(self):
        bookName = input("\nFill in the name of the bookcopy you want to edit: ").lower()
        with open("data/bookcopies.json", "r") as f:
            data = json.load(f)
        for book in data:
            if bookName == book["title"].lower():
                newBook = book
                print("What do you want to edit?\n")
                inputEdit = input("\n1. Author\n2. Country\n3. Imagelink\n4. Language\n5. Link\n6. Pages\n7. Title\n8. ISBN9. Year\n10. Exit\n")

                if inputEdit == "1":
                    newAuthor = input("\nNew author: ")
                    newBook["author"] = newAuthor
                elif inputEdit == "2":
                    newCountry = input("\nNew country: ")
                    newBook["country"] = newCountry
                elif inputEdit == "3":
                    newImageLink = input("\nNew imagelink: ")
                    newBook["imageLink"] = newImageLink
                elif inputEdit == "4":
                    newLanguage = input("\nNew language: ")
                    newBook["language"] = newLanguage
                elif inputEdit == "5":
                    newLink = input("\nNew link: ")
                    newBook["link"] = newLink
                elif inputEdit == "6":
                    newPages = input("\nNew pages: ")
                    newBook["pages"] = newPages
                elif inputEdit == "7":
                    newTitle = input("\nNew title: ")
                    newBook["title"] = newTitle
                elif inputEdit == "8":
                    newISBN = input("\nNew ISBN: ")
                    newBook["ISBN"] = newISBN
                elif inputEdit == "9":
                    newYear = input("\nNew year: ")
                    newBook["year"] = newYear
                elif inputEdit == "10":
                    break
                else:
                    print("Please enter a number between 1 and 9")
            
                for index, book in enumerate(data):
                    if bookName == book["title"].lower():
                        self.readAndWrite(index, newBook)

                print("\n\nSuccesfully edited the copies of the book!\n\n")

    def searchBookItem(self):
        #search a book item and check its availibility
        with open("data/bookcopies.json", "r") as f:
            data = json.load(f)
        with open("data/books.json", "r") as f:
            books = json.load(f)
        found = False
        Enter = input("\nPlease enter the title of the book you would like to search for:\n").lower()
        for i in books:
            if Enter == i["title"].lower():
                found = True
        
        if found == False:
            print("This book does not exist")
        elif found == True:
            print("This book is available")
    
    #show all copies
    def showAllCopies(self):
        with open("data/bookcopies.json", "r") as f:
            data = json.load(f)
        for book in data:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Country: {book['country']}")
            print(f"Language: {book['language']}")
            print(f"Year: {book['year']}")
            print(f"Pages: {book['pages']}")
            print(f"Link: {book['link']}ISBN: {book['ISBN']}")
            print(f"ImageLink: {book['imageLink']}")
            print("\n")
                
