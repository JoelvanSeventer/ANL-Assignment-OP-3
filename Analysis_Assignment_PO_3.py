class Book:
    def __init__(self, Title, Author, ISBN):
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN
        print("Title: ", self.Title, self.Author, self.ISBN)

while True:
    print("Welcome, choose one of the following options:\n\n\
1. Search for a book\n\
2. Make a book loan\n\
3. Add new customer\n\
4. Add new book\n\
5. Make a back-up\n\
6. Restore library from a back-up")
    UserInput = input()

    if UserInput == "1":
        print("Title:")
        Title = input()
        print("Author:")
        Author = input()
        print("ISBN:")
        ISBN = input()

        with open ("database/books.json", 'r') as f:
            data = json.load(f)
        for book in data:
            print(book['title'])

        print(books)
        for book in books:
            if Title == book['title'] or Author == book.Author or ISBN == book.ISBN:
                print("Title:", book.Title)
                print("Author: ", book.Author)
                print("ISBN:", book.ISBN)





    elif UserInput == "2":
        pass

    elif UserInput == "3":
        pass

    elif UserInput == "4":
        print("Title:")
        Title = input()
        print("Author:")
        Author = input()
        print("ISBN:")
        ISBN = input()
        book = Book(Title, Author, ISBN)
        books.append(book)


    elif UserInput == "5":
        pass


    elif UserInput == "6":
        pass

