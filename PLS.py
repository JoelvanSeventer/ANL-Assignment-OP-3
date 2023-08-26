import backend as BE
from data import data, abs_path
import json
import csv
import sys
import os
from backup import Backup


currentUser = "guest"
currentUserName = ""

def Start():
    BE.clear()
    print(
        "Welcome to the Public Library System\n\n"
    )

def MenuNoLogin(errorMessage = ""): 
    global currentUser, currentUserName
    possibleanswers = ["1", "9"]
    answer = ""
    while answer not in possibleanswers:
        #Start()
        print(f"{errorMessage}Hi, What would you like to do? (type the number)\n1. Log in\n9. Exit Program\n")
        answer = input(">> ")
        if answer == "1" :
            loginMenu()
        elif answer == "9":
            CloseProgram()
        else:
            MenuNoLogin("Command not recognized, please try again.\n\n")

def loginMenu(errorMessage = ""):
    global currentUser, currentUserName
    answer = ""
    possibleAnswers = ["1", "2"]
    while answer not in possibleAnswers:
        Start()
        print(f"{errorMessage}\nLogin Menu\n\n 1. Log in as Member.\n 2. Log in as LibraryAdmin.\n 9. Return to the main menu.\n")
        answer = input(">> ")
        if answer == "1":
            Start()
            print("\nEnter login information for Member:\n")
            username = input("Enter username: ")
            password = input("Enter password: ")
            loggedIn, currentUser, currentUserName = BE.Backup.loginMember(username, password, "members", "Username", "Password")
            if loggedIn:
                RunProgram()
            else:
                loginMenu("\nLogin failed. Please try again\n")
        elif answer == "2":
            Start()
            print("\nEnter login information for LibraryAdmin:\n")
            username = input("Enter username: ")
            password = input("Enter password: ")
            loggedIn, currentUser, currentUserName = BE.Backup.loginLibraryAdmin(username, password, "libraryAdmin")
            if loggedIn:
                RunProgram()
            else:
                loginMenu("\nLogin failed. Please try again\n")
        elif answer == "9":
            RunProgram()
        else:
            loginMenu("\nCommand not recognized, please try again.\n")

def MenuMember(errorMessage = ""):
    global currentUser, currentUserName
    answer = ""
    possibleAnswers = ["1", "2", "9"]

    while answer not in possibleAnswers:
        Start()
        print(f"{errorMessage}Hi, {currentUserName}.\n\nWhat would you like to do? (type the number)\n\n 1. See list of all books in catalog\n 2. Search book in catalog\n 3. See list of book items\n 4. Search book item and it's availability\n 5. Loan a book item\n 6. Return a book item\n 9. Logout\n")
        answer = input(">> ")
        if answer == "1":
            listBook()
        elif answer == "2":
            searchBook()
        elif answer == "3":
            listBookItem()
        elif answer == "4":
            searchBookItem()
        elif answer == "5":
            lendBookItem()
        elif answer == "6":
            ReturnLoanItem()
        elif answer == "9":
            currentUser = "guest"
            RunProgram()
        else:
            MenuMember("\nCommand not recognized, please try again.\n\n")

def MenuLibraryAdmin(errorMessage = ""):
    global currentUser, currentUserName
    answer = ""
    possibleanswers = ["1", "2","3","4", "5", "6", "7","9"]

    while answer not in possibleanswers:
        Start()
        print(f"{errorMessage}\nWelcome, {currentUserName}. What would you like to do?")
        print("\n 1. Functions related to members\n 2. Functions related to catalog\n 3. Functions related to book item\n 4. Make backup\n 5. Load backup \n 9. Logout. \n")
        answer = input(">> ")

        if answer == "1":
            functionMember()
        elif answer == "2":
            functionCatalog()
        elif answer == "3":
            functionBookItem()
        elif answer == "4":
            try: 
                BE.Backup.backupSystem()
                print("Make backup succesful.\n")
                a = input()
                RunProgram()
            except:
                print("Make Backup failed. \nPress any key to continue... ")
                a = input()
                RunProgram()
                
        elif answer == "5":
            try: 
                BE.Backup.loadSystemBackup()
                print("Loaded backup succesful. Press any key to continue... ")
                a = input()
                RunProgram()
            except: 
                print("Load Backup failed. \nPress any key to continue... ")
                a = input()
                RunProgram()
        elif answer == "9":
            currentUser = "guest"
            RunProgram()
        else: 
            MenuLibraryAdmin("\nCommand not recognized, please try again.\n")

############################################################################

def functionMember():
    answer = ""
    possibleAnswers = ["1", "2", "3", "4"]

    while answer not in possibleAnswers:
        print("\n 1. To see a list of all members\n 2. Add a new member\n 3. Edit a member\n 4. Delete a member\n 5. Add a list of members using a CSV file\n 6. Check status of book items currently loaned by a member\n 9. Return to previous menu\n")
        answer = input(" >> ")
        if answer == "1":
            listMember()
        elif answer == "2":
            addMember()
        elif answer == "3":
            editMember()
        elif answer == "4":
            deleteMember()
        elif answer == "5":
            ImportCSV()
        elif answer == "6":
            checkStatus()
        elif answer == "9":
            RunProgram()

def addMember():
    print("Fill in the information of the member you want to add.")
    firstName = input("First name -> ")
    lastName = input("Last name -> ")
    address = input("Adress -> ")
    zipCode = input("ZipCode -> ")
    city = input("City -> ")
    email = input("Email -> ")
    username = input("Username -> ")
    password = input("Password -> ")
    phoneNumber = input("Phone number -> ")
    try:
        BE.LibraryAdmin.addMember(firstName, lastName, address, zipCode, city, email, username, password, phoneNumber)
        print("\nMember added succesfully!")
    except:
        print("\nAdding member went wrong. Please try again.")
        addMember()
    menu = ""
    possibleAnswers = ["1","2"]
    while menu not in possibleAnswers:
        menu = input("\nDo you want to add another member?\n 1. Yes\n 2. No\n")
        if menu == "1":
            addMember()
        elif menu == "2":
            print("\n")
            RunProgram()
        else:
            print("Command not recognized, please try again.")

def editMember():
    while True:
        inputName = input("Enter the first and lastname of the member you want to edit: ")
        if findMember(inputName):
            print("Member found!")
            break
        else:
            print("Member not found. Press 1 to try again or press 2 to return to the main menu.")
            inp = input(">> ")
            if inp == "1":
                continue
            elif inp == "2":
                RunProgram()
            else:
                print("Command not recognized, please try again.")
                editMember()    

    print("Choose the information you want to edit of the member.\n")
    print("1. First name\n2. Last name\n3. Address\n4. ZipCode\n5. City\n6. Email\n7. Username\n8. Password\n9. Phone number\n")
    inp = input(">> ")
    edit = ""
    if inp == "1":
        edit = "GivenName"
    elif inp == "2":
        edit = "Surname"
    elif inp == "3":
        edit = "StreetAddress"
    elif inp == "4":
        edit = "ZipCode"
    elif inp == "5":
        edit = "City"
    elif inp == "6":
        edit = "EmailAddress"
    elif inp == "7":
        edit = "Username"
    elif inp == "8":
        edit = "Password"
    elif inp == "9":
        edit = "TelephoneNumber"
    try: 
        BE.LibraryAdmin.editMember(inputName, edit)
        print("Member edited succesfully!")
    except:
        print("Something went wrong. Please try again.")
        editMember()

    menu = ""
    possibleAnswers = ["1","2"]
    while menu not in possibleAnswers:
        menu = input("\nDo you want to edit another member?\n 1. Yes\n 2. No\n")
        if menu == "1":
            editMember()
        elif menu == "2":
            print("\n")
            RunProgram()
        else:
            print("Command not recognized, please try again.")
        

def deleteMember():
    while True:
        inputName = input("Enter the first and lastname of the member you want to delete: ")
        if findMember(inputName):
            print("Member found!")
            break
        else:
            print("Member not found. Press 1 to try again or press 2 to return to the main menu.")
            inp = input(">> ")
            if inp == "1":
                continue
            elif inp == "2":
                RunProgram()
            else:
                print("Command not recognized, please try again.")
                deleteMember()  

    try:
        BE.LibraryAdmin.deleteMember(inputName)
        print("Member deleted succesfully!")
    except:
        print("Something went wrong. Please try again.")
        deleteMember()

    menu = ""
    possibleAnswers = ["1","2"]
    while menu not in possibleAnswers:
        menu = input("\nDo you want to delete another member?\n 1. Yes\n 2. No\n")
        if menu == "1":
            deleteMember()
        elif menu == "2":
            print("\n")
            RunProgram()
        else:
            print("Command not recognized, please try again.")

def listMember():
    with open("data/members.json", "r") as f:
        data = json.load(f)

    for member in data:
        print(member["GivenName"] + " " + member["Surname"])

    x = input("\nPress any key to restart the program.")
    RunProgram()

def findMember(member):
    with open("data/members.json", "r") as f:
        data = json.load(f)

    for item in data:
        if member.lower() == item["GivenName"].lower() + " " + item["Surname"].lower():
            return True
    return False

def checkStatus():
    print("hoi")

############################################################################

def functionCatalog():
    answer = ""
    possibleAnswers = ["1", "2", "3", "4"]

    while answer not in possibleAnswers:
        print("\n 1. See catalog (list of books)\n 2. Add a book\n 3. Edit a book\n 4. Delete a book\n 5. Search a book\n 6. Add a list of books using a JSON file\n 9. Return to previous menu\n")
        answer = input(" >> ")
        if answer == "1":
            listBook()
        elif answer == "2":
            addBook()
        elif answer == "3":
            editBook()
        elif answer == "4":
            deleteBook()
        elif answer == "5":
            searchBook()
        elif answer == "6":
            importJSON()
        elif answer == "9":
            RunProgram()

def listBook():
    with open("data/catalog.json", "r") as f:
        data = json.load(f)

    for book in data:
        print(book["title"] + " by " + book["author"])

    x = input("\nPress any key to restart the program.")
    RunProgram()

def addBook():
    print("To add a new book we need some information.")
    author = input("Book author -> ")
    country = input("Country -> ")
    imageLink = input("Image link -> ")
    language = input("Book Language -> ")
    link = input("Website link -> ")
    pages = int(input("Total pages -> "))
    title = input("Book title -> ")
    ISBN = input("ISBN -> ")
    year = int(input("Publishing year -> "))
    
    try:
        BE.LibraryAdmin.registerBook(author, country, imageLink, language, link, pages, title, ISBN, year)
        AddToLoanItemsNew(title, author)
        print("\nBook was succesfully added to the database.")
    except:
        print("\nSomething went wrong. Please try again.")
        addBook()

    addbook = ""
    possibleAnswers = ["1","2"]
    while addbook not in possibleAnswers:
        addbook = input("\nDo you want to edit another book?\n 1. Yes\n 2. No\n")
        if addbook == "1":
            addBook()
        elif addbook == "2":
            print("\n")
            functionCatalog()
        else:
            print("Command not recognized, please try again.")

def editBook():
    answer = ""
    possibleanswers = ["1", "2", "9"]
    while answer not in possibleanswers:
        print("Would you like to edit book by:\n 1. Title\n 2. Author\n 9. Return to main menu")
        answer = input("\n>> ")
        if answer == "1":
            title = input("\nPlease enter the title of the book you want to edit:\n")
            try: 
                for book in data['catalog']:
                    if title.lower() in book["title"].lower():
                        print('\nTitle: ' + book['title'])
                        print('Author: ' + book['author'])
                        print("\nWhat would you like to edit?\n1. Author\n2. Country\n3. Imagelink\n4. Language\n5. Link\n6. Pages\n7. Title\n8. ISBN\n9. Year\n10. Exit\n")
                        inputEdit = input(">> ")
                        if inputEdit == "1":
                            newValue = input("Enter the new value: ")
                            book["author"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "2":
                            newValue = input("Enter the new value: ")
                            book["country"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "3":
                            newValue = input("Enter the new value: ")
                            book["imageLink"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "4":
                            newValue = input("Enter the new value: ")
                            book["language"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "5":
                            newValue = input("Enter the new value: ")
                            book["link"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "6":
                            newValue = input("Enter the new value: ")
                            book["pages"] = int(newValue)
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "7":
                            newValue = input("Enter the new value: ")
                            book["title"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "8":
                            newValue = input("Enter the new value: ")
                            book["ISBN"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "9":
                            newValue = input("Enter the new value: ")
                            book["year"] = int(newValue)
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "10":
                            editBook()
                                         
                print("\n\nSuccesfully edited the book!\n\n")
                editbook = ""
                possibleAnswers = ["1","2"]
                while editbook not in possibleAnswers:
                    editbook = input("\nDo you want to edit another book?\n 1. Yes\n 2. No\n")
                    if editbook == "1":
                        editBook()
                    elif editbook == "2":
                        print("\n")
                        functionCatalog()
                    else:
                        print("Command not recognized, please try again.")
            except:
                print('Something went wrong. Please try again.')
                RunProgram()

        elif answer == "2":
            author = input("\nPlease enter the author of the book you want to edit:\n")
            try: 
                for book in data['catalog']:
                    if author.lower() in book["author"].lower():
                        print('\nTitle: ' + book['title'])
                        print('Author: ' + book['author'])
                        print("\nWhat would you like to edit? 1. Author\n2. Country\n3. Imagelink\n4. Language\n5. Link\n6. Pages\n7. Title\n8. ISBN\n9. Year\n10. Exit\n")
                        inputEdit = input(">> ")
                        if inputEdit == "1":
                            newValue = input("Enter the new value: ")
                            book["author"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "2":
                            newValue = input("Enter the new value: ")
                            book["country"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "3":
                            newValue = input("Enter the new value: ")
                            book["imageLink"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "4":
                            newValue = input("Enter the new value: ")
                            book["language"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "5":
                            newValue = input("Enter the new value: ")
                            book["link"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "6":
                            newValue = input("Enter the new value: ")
                            book["pages"] = int(newValue)
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "7":
                            newValue = input("Enter the new value: ")
                            book["title"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "8":
                            newValue = input("Enter the new value: ")
                            book["ISBN"] = newValue
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "9":
                            newValue = input("Enter the new value: ")
                            book["year"] = int(newValue)
                            Backup.writeJson(abs_path + '/data/catalog.json', data['catalog'])
                            break
                        elif inputEdit == "10":
                            editBook()

                print("\n\nSuccesfully edited the book!\n\n")
                editbook = ""
                possibleAnswers = ["1","2"]
                while editbook not in possibleAnswers:
                    editbook = input("\nDo you want to edit another book?\n 1. Yes\n 2. No\n")
                    if editbook == "1":
                        editBook()
                    elif editbook == "2":
                        print("\n")
                        functionCatalog()
                    else:
                        print("Command not recognized, please try again.")
            except:
                print('Something went wrong. Please try again.')
                RunProgram()

        elif answer == "9":
            RunProgram()
        else:
            print("\nInput not recognised. Please try again.")
            answer = ""

def deleteBook():
    try: 
        answer = ""
        possibleanswers = ["1", "2", "9"]
        while answer not in possibleanswers:
            print("Delete book by:\n 1. Title\n 2. Author\n 9. Return to main menu")
            answer = input("\n>> ")
            if answer == "1":
                title = input("\nPlease enter the title of the book you want to delete:\n")
                BE.LibraryAdmin.delBook("title", title)
                break
            elif answer == "2":
                author = input("\nPlease enter the author of the book you want to delete:\n")
                BE.LibraryAdmin.delBook("author", author)
                break
            elif answer == "9":
                RunProgram()
            else:
                print("\nInput not recognised. Please try again.")
                answer = ""

        editbook = ""
        possibleAnswers = ["1","2"]
        while editbook not in possibleAnswers:
            editbook = input("\nDo you want to delete another book?\n 1. Yes\n 2. No\n")
            if editbook == "1":
                deleteBook()
            elif editbook == "2":
                print("\n")
                functionCatalog()
            else:
                print("Command not recognized, please try again.")
    except:
        print('Something went wrong. Please try again.')
        RunProgram()

def searchBookCatalog(value):
    print(f"\nPlease enter a phrase for {value} search.")
    answer = input("\n>> ")
    try: 
        for book in data['catalog']:
            if answer.lower() in book[value].lower():
                print('Title: ' + book['title'])
                print('Author: ' + book['author'])
                print('Total pages: ' + str(book['pages']))
                print('Published year: ' + str(book['year']))
                print('Language: ' + book['language'])
                print('Country: ' + book['country'])
                print('Cover Image link: ' + book['imageLink'])
                print('Website link: ' + book['link'])
        
        x = input("\nPress any key to restart the program.")
        RunProgram()
    except: 
        print('Something went wrong. Please try again.')
        RunProgram()

def searchBook():
    answer = ""
    possibleanswers = ["1", "2", "9"]
    while answer not in possibleanswers:
        print("Would you like to:\n 1. Search book by Title\n 2. Search by Author\n 9. Return to main menu")
        answer = input("\n>> ")
        if answer == "1":
            searchBookCatalog("title")
        elif answer == "2":
            searchBookCatalog("author")
        elif answer == "9":
            RunProgram()
        else:
            print("\nInput not recognised. Please try again.")
            answer = ""

def importJSON():
    jsonbookfile = input("Type the name of the file here to load the books from JSON : ")
        
    try:
        with open(abs_path + f'//{jsonbookfile}.json') as f:
            jsonbookfile2 = json.load(f)

        with open(abs_path + '/data/catalog.json', 'w') as json_file:
            json.dump(jsonbookfile2, json_file, indent = 4)

        with open(abs_path + '/data/catalog.json') as f:
            data['catalog'] = json.load(f)

        with open(abs_path + '/data/members.json') as f:
            data['members'] = json.load(f)

        with open(abs_path + '/data/loanItems.json') as f:
            data['loanItems'] = json.load(f)

                
        for item in data['catalog']:
            AddToLoanItemsNew(item['title'], item['author'])
        print("Load succesfull. Press any key to continue...")
        a = input()
        RunProgram()

    except: 
        print("Load failed! Did you enter the correct filename?")
        a = input("Press any key to continue ...")
        RunProgram()

############################################################################

def functionBookItem():
    answer = ""
    possibleAnswers = ["1", "2", "3", "4"]

    while answer not in possibleAnswers:
        print("\n 1. To see a list of all book items\n 2. Add a book item\n 3. Edit a book item\n 4. Delete a book item\n 5. Search book item and its availabilty\n 6. lend a book item to member\n 9. Return to previous menu\n")
        answer = input(" >> ")
        if answer == "1":
            listBookItem()
        elif answer == "2":
            addBookItem()
        elif answer == "3":
            editBookItem()
        elif answer == "4":
            deleteBookItem()
        elif answer == "5":
            searchBookItem()
        elif answer == "6":
            lendBookItem()
        elif answer == "9":
            RunProgram()

def listBookItem():
    print("\nBook Items\n")
    for item in data['bookItems']:
        print(f"Book ID: {item['ISBN']}, Title: {item['title']}, Author: {item['author']}, Available: {item['copies']} copies")
    x = input("\nPress any key to restart the program.")
    RunProgram()

def addBookItem():
    check = False
    running = True

    title = input("\nPlease enter the title of the book you would like to make copies of:\n").lower()

    with open("data/bookItems.json", "r") as f:
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

    with open("data/bookItems.json", "w+") as f:
        jsoned_data = json.dumps(alldata, indent=True)
        f.write(jsoned_data)
        print(f"\nSuccesfully added {amount} copies\n")

    if check == False:
        print("That book does not exist")
    RunProgram()

def editBookItem():
        with open("data/bookItems.json", "r") as f:
                data = json.load(f)

        running = True
        while running:
            exists = False
            title = input("\nPlease enter the title of the book item you would like to edit:\n").lower()

            for book in data:
                if book["title"].lower() == title:
                    exists = True
                    break
            
            if exists:
                running = False
            else:
                print("\nThat book doesn't exist.")
                print("Please enter a existing book:\n")

        inputEdit = input("\n1. Author\n2. Country\n3. Imagelink\n4. Language\n5. Link\n6. Pages\n7. Title\n8. Year\n9. Exit\n") 
        newValue = input("Enter the new value: ")

        with open("data/bookItems.json", "r") as f:
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

            
        with open("data/bookItems.json", "w+") as f:
            jsoned_data = json.dumps(data, indent=True)
            f.write(jsoned_data)

        print("\n\nSuccesfully edited the copies of the book!\n\n")
        RunProgram()

def availableBookItem():
    try: 
        answer = ""
        possibleanswers = ["1", "2", "9"]
        while answer not in possibleanswers:
            print("Search availability book  by:\n 1. Title\n 2. Author\n 9. Return to main menu")
            found = False
            answer = input("\n>> ")
            if answer == "1":
                title = input("\nPlease enter the title of the book you want to delete:\n")
                for book in data['bookItems']:
                    if title.lower() in book["title"].lower():
                        found = True
                if found and book["copies"] > 0:
                    print("Book is available")
                    break
                elif found and book["copies"] == 0:
                    print("Book is not available")
                    break
                else:
                    print("Book not found")
                    break
            elif answer == "2":
                author = input("\nPlease enter the author of the book you want to delete:\n")
                for book in data['bookItems']:
                    if author.lower() in book["author"].lower():
                        found = True
                if found and book["copies"] > 0:
                    print("Book is available")
                    break
                elif found and book["copies"] == 0:
                    print("Book is not available")
                    break
                else:
                    print("Book not found")
                    break
            elif answer == "9":
                RunProgram()
            else:
                print("\nInput not recognised. Please try again.")
                answer = ""

        with open("data/bookItems.json", "r") as f:
            data = json.load(f)

        for book in data:
            if book["copies"] > 0:
                print(f"Title: {book['title']}, Author: {book['author']}, Available: {book['copies']} copies")
    
    except:
        print('Something went wrong. Please try again.')
        RunProgram()


def deleteBookItem():
    title = input("\nPlease enter the title of the book you want to remove copies from:\n")
    copies = int(input("\nEnter the amount of copies you want to remove:\n"))
    bookitemFound = False
    count = 0
    with open("data/bookItems.json", 'r') as f:
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

        with open('data/bookItems.json', "w+") as f:
            jsoned_data = json.dumps(data, indent=True)
            f.write(jsoned_data)
        print(f"You've succesfully removed the copies of the book")
    else:
        print("This book does not have any copies")
    RunProgram()

def searchBookItem():
    BE.LoanAdministration.GetInfo()
    RunProgram()

def lendBookItem():
    global currentUser, currentUserName
    Start()
    if len(data['loanItems']) == 0:
        print("There are no books in the entire library. Add books first.")
        a = input("\nPress any key to return to the main menu.")
        RunProgram()
    BE.Catalog.GetInfo()
    print("Loan a Book Menu\n\nType the title of the book you would like to loan. (Use the book browser to see available books)\n")
    booktitle = input(">> ")
    decidedonbook = False
    foundbook = 0
    
    for item in data['loanItems']:
        if booktitle.lower() == item['bookItem'].lower():
            foundbook += 1
            targetbook = item['bookItem'] 
            targetauthor = item['author']
    if foundbook == 1:
        print("\nYou have selected " + targetbook + " by " + targetauthor)
        decidedonbook = True
    elif foundbook > 1: 
        print(f"\nThere are multiple books by the name {targetbook}")
        for item in data['loanItems']:
            if targetbook == item['bookItem']:
                print(f"{item['bookItem']} by {item['author']}")
        targetauthor = input("Which author? ")     
        authorcheck = False   
        for item in data['loanItems']: 
            if targetbook == item['bookItem'] and targetauthor.lower() == item['author'].lower():
                print(f"{item['bookItem']} by {item['author']} it is. ")
                authorcheck = True
                decidedonbook = True
        if authorcheck == False:
            print("\nCould not find the author. Please try again.\n")

    else: 
        print("\nCould not find book. Please try again\n")
        a = input(">> ")
        RunProgram()


    for item in data['loanItems']:
        
        checkvar = json.loads(json.dumps(item))
        if checkvar['bookItem'] == targetbook and checkvar['author'] == targetauthor and checkvar['isAvailable'] == False:
            print("\nThis book is not available! Please return this book before trying to loan it.")
            decidedonbook = False
            a = input("\nPress any key to return to the menu")
            RunProgram()
    if decidedonbook:
        dateLoan = input("From when will the book be loaned? (DD-MM-YYYY): ")
        datereturn = input("When does the book have to be returned? (DD-MM-YYYY): ")
        if currentUser == "members":
            loanerusername = currentUserName
        else:
            loanerusername = input("What is the username of the person who will loan this book?: ")

        jsontopy = data['loanItems']

        for item in jsontopy: 
            if item['bookItem'] == targetbook and item['author'] == targetauthor:
                item['dateOfLoan'] = dateLoan
                item['dateOfReturn'] = datereturn
                item['userOfItem'] = loanerusername
                item['isAvailable'] = False


        with open(abs_path + '/data/loanItems.json', 'w') as outfile:
            json.dump(jsontopy, outfile, indent = 4)
        print(f"This book has now been loaned to {loanerusername} from {dateLoan} untill {datereturn}")
        a = input("\nPress any key to return to the main menu.")
        RunProgram()

############################################################################

def AddToLoanItemsNew(title, author):
    newloanitemdict = {"bookItem": title, "author": author, "dateOfLoan" : "none", "dateOfReturn" : "none", "userOfItem" : "none", "isAvailable" : True}
    for item in data['loanItems']:
        if (item['bookItem'] == title) and (item['author'] == author) :
            print(f"{item['bookItem']} already exists")
            return

    data['loanItems'].append(newloanitemdict)
    BE.Backup.writeJson(abs_path + '/data/loanItems.json', data['loanItems'])

def ReturnLoanItem():
    global currentUser, currentUserName
    print("\nWhich item would you like to return? ")
    targetbook = input("\nTitle of the book: ")
    
    if currentUser == "members":
        targetusername = currentUserName
    else:
        targetusername = input("Username: ")
    foundbook = False
    for item in data['loanItems']:
        if item['bookItem'].lower() == targetbook.lower():
            foundbook = True
            break
    
    if foundbook:
        print(f"\nThis book is due on {item['dateOfReturn']}")

        availableanswers = ["1", "2"]
        answer = "" 
        while answer not in availableanswers:
            print("Are you sure you want to return the book now? \n 1. Yes\n 2. No")
            answer = input()
            if answer == "1":
                print("\nOK, returning book.")
                try: 
                    jsontopy = data['loanItems']
                    for item in jsontopy: 
                        if item['bookItem'].lower() == targetbook.lower() and item['userOfItem'] == targetusername:
                            item['dateOfLoan'] = "none"
                            item['dateOfReturn'] = "none"
                            item['userOfItem'] = "none"
                            item['isAvailable'] = True

                            with open(abs_path + '/json/loanItems.json', 'w') as outfile:
                                json.dump(jsontopy, outfile, indent = 4)
                except: 
                    print("Something went wrong. Try again.")
                    a = input("Press any key to continue ...")
            elif answer == "2":
                print("OK, not returning book. Heading back to main menu")
                a = input("Press any key to continue ...")
    else:
        print("Could not find the specified title / username combination. Did you enter the credentials correctly?")
        a = input("Press any key to continue to return to the Menu.")
            
def ImportCSV():
    filename = input("What is the name of the file you are trying to import?: ") + ".csv"

    try:
        with open(abs_path + f"//{filename}") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for item in csv_reader:
                if item[0] != "Number" and item[1] != "GivenName":
                    data['members'].append({
                        "Number": item[0],
                        "GivenName": item[1],
                        "Surname": item[2],
                        "StreetAddress": item[3],
                        "ZipCode": item[4],
                        "City": item[5],
                        "EmailAddress": item[6],
                        "Username": item[7],
                        "Password": item[8],
                        "TelephoneNumber": item[9],
                        })
            BE.Backup.writeJson(abs_path + '/data/members.json', data['members'])
            print("\nMembers have been imported successfully.")
            a = input("Press any key to continue ...")
            # RunProgram()

    except: 
        print("Something went wrong. Please try again and check for spelling.")
        a = input("Press any key to continue ...")
        # RunProgram()

def RunProgram():

    global currentUser
    if currentUser == "guest":
        MenuNoLogin()
    elif currentUser == "members":
        MenuMember()
    elif currentUser == "libraryAdmin":
        MenuLibraryAdmin()
    else:
        BE.clear()
        print(f"ERROR: CURRENTUSER({currentUser}) -> RUNPROGRAM METHOD")
        currentUser = "guest"
        print("\nSomething went wrong.\n")
        x = input("\nPress any key to restart the program.")
        RunProgram()

def CloseProgram():
    print('Have a nice day!')
    sys.exit(1)

RunProgram()