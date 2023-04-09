import backend as BE
from data import data, abs_path
import json
import csv
import sys
import os


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
        print(f"{errorMessage}Hi, {currentUserName}.\n\nWhat would you like to do? (type the number)\n\n 1. Browse books\n 2. Loan/Return a book\n 9. Logout\n")
        answer = input(">> ")
        if answer == "1":
            searchBook()
        elif answer == "2":
            LoanMenu()
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
        print("\n 1. Functions related to members\n 2. Functions related to catalog\n 3. Loan books + loan administration \n 4. Load / make system backup. \n 9. Logout. \n")
        answer = input(">> ")

        if answer == "1":
            functionMember
        elif answer == "2":
            functionCatalog()
        elif answer == "3":
            print("You have selected: Loan books + loan administration")
            possibleanswers = ["1", "2", "3","9"]
            answer = ""

            while answer not in possibleanswers:
                print(f"\n 1. Loan a book to a customer \n 2. Return a loaned book \n 3. View loan administration \n 9. Return")
                answer = input()
                if answer == "1":

                    lendBookItem()
        
                elif answer == "2":
                    ReturnLoanItem()
                    
                elif answer == "3":
                    print("You have selected 3. View loan administration")
                    print("Viewing all loaned books. Press any key to continue... ")
                    a = input()
                    BE.LoanAdministration.GetInfo()
                elif answer == "9":
                    print("Returning to previous menu...")
                    RunProgram()
            RunProgram()
        elif answer == "5":
            print("You have selected: 6. Load / make system backup")
            possibleanswers = ["1", "2","9"]
            answer = ""

            while answer not in possibleanswers:
                print(f"\n 1. Load system backup \n 2. Make system backup \n 9. Return to the main menu.\n")
                answer = input()
                if answer == "1":
                    BE.Backup.loadSystemBackup()
                    print("Backup loaded. Press any key to continue... ")
                    a = input()
                    RunProgram()
                elif answer == "2":
                    try:
                        BE.Backup.backupSystem()
                        print("Backup succesful. \nFile created as: backup.json.  ")
                        a = input()
                        RunProgram()
                    except: 
                        print("Backup failed. Did you enter the filename correctly?")
                elif answer == "9":
                    print("Returning to previous menu...")
                    RunProgram()
        elif answer == "9":
            currentUser = "guest"
            RunProgram()
        else: 
            MenuLibraryAdmin("\nCommand not recognized, please try again.\n")

def functionMember():
    answer = ""
    possibleAnswers = ["1", "2", "3", "4"]

    while answer not in possibleAnswers:
        print("\n 1. To see a list of all members\n 2. Add a new member\n 3. Edit a member\n 4. Delete a member\n 5. Add a list of members using a CSV file\n 9. Return to previous menu\n")
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
        print("in try")
        BE.LibraryAdmin.addMember(firstName, lastName, address, zipCode, city, email, username, password, phoneNumber)
        print("\nMember added succesfully!")
    except:
        print("\nAdding member went wrong. Please try again.")
        addMember()
    addMember = ""
    possibleAnswers = ["1","2"]
    while addMember not in possibleAnswers:
        addMember = input("\nDo you want to add another member?\n 1. Yes\n 2. No\n")
        if addMember == "1":
            addMember()
        elif addMember == "2":
            print("\n")
            RunProgram()
        else:
            print("Command not recognized, please try again.")

def editMember():
    print("hoi")

def deleteMember():
    print("hoi")

def listMember():
    with open("data/members.json", "r") as f:
        data = json.load(f)

    for member in data:
        print(member["GivenName"] + " " + member["Surname"])

    x = input("\nPress any key to restart the program.")
    RunProgram()

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
    with open("data/books.json", "r") as f:
        data = json.load(f)

    for book in data:
        print(book["Title"] + " by " + book["Author"])

    x = input("\nPress any key to restart the program.")
    RunProgram()

def addBook():
    print("To add a new book we need some information.")
    title = input("Book title -> ")
    author = input("Book Author -> ")
    pages = input("Total pages -> ")
    year = input("Publishing year -> ")
    country = input("Country -> ")
    language = input("Book Language -> ")
    imageLink = input("Image link -> ")
    link = input("Website link -> ")
    try:
        BE.LibraryAdmin.registerBook(author, country, imageLink, language, link, pages, title, year)
        AddToLoanItemsNew(title, author)
        print("\nBook was succesfully added to the database.")
    except:
        print("\nSomething went wrong. Please try again.")
        addBook()

    addBook  = ""
    possibleAnswers = ["1","2"]
    while addBook not in possibleAnswers:
        addBook = input("\nDo you want to add another book?\n 1. Yes\n 2. No\n")
        if addBook == "1":
            addBook()
        elif addBook == "2":
            print("\n")
            functionCatalog()
        else:
            print("Command not recognized, please try again.")

def editBook():
    print("hoi")

def deleteBook():
    print("hoi")

def searchBook():
        print("\nList of books\n")

        def bookView():
            global bookIDCounter
            bookIDCounter = BE.Catalog.GetInfo()
            answer = ""
            possibleanswers = ["1", "2", "3", "4", "5", "9"]
            while answer not in possibleanswers:
                print("Would you like to:\n 1. Pick a book by Book ID.\n 2. Search book by Title.\n 3. Search by Author. \n 4. Search by publishing year.\n 5. Search by Language. \n 9. Return to main menu")
                answer = input("\n>> ")
                if answer == "1":
                    detailedBookView(bookIDCounter)
                    a = input("Press any key to continue...sup")
                elif answer == "2":
                    searchBookCatalog("title")
                elif answer == "3":
                    searchBookCatalog("author")
                elif answer == "4":
                    searchBookCatalog("year")
                elif answer == "5":
                    searchBookCatalog("language")
                elif answer == "9":
                    RunProgram()
                else:
                    print("\nInput not recognised. Please try again.")
                    answer = ""

        def searchBookCatalog(value):
            print(f"\nPlease enter the exact phrase for {value} search.")
            answer = input("\n>> ")
            for book in data['books']:
                if answer.lower() == book[value].lower():
                    print('Title: ' + book['title'])
                    print('Author: ' + book['author'])
                    print('Total pages: ' + str(book['pages']))
                    print('Published year: ' + str(book['year']))
                    print('Language: ' + book['language'])
                    print('Country: ' + book['country'])
                    print('Cover Image link: ' + book['imageLink'])
                    print('Website link: ' + book['link'])
            else:
                print(f"\nDisplaying all search results with parameter: {value} = {answer}")
                possibleAnswers = ["1", "2"]
                answer = ""
                while answer not in possibleAnswers:
                    print("\nWhat would you like to do.\n 1. Try another search.\n 2. View all books\n")
                    answer = input(">>")
                    if answer == "1":
                        bookView()
                    elif answer == "2":
                        bookView()
                    else:
                        print("Command not recognized, please try again.")
                        answer = ""

        def detailedBookView(bookIDCounter):
            global currentUser
            print("\nPlease pick a book by Book ID to see a more detailed view.")
            pickedBookID = input(">> ")
            try:
                pickedBookID = int(pickedBookID)
            except:
                print("\nThis Book ID does not exist. Please try again.")
                detailedBookView(bookIDCounter)
            if pickedBookID > bookIDCounter:
                print("\nThis Book ID does not exist. Please try again.")
                detailedBookView(bookIDCounter)
            print('Title: ' + data['books'][pickedBookID-1]['title'])
            print('Author: ' + data['books'][pickedBookID-1]['author'])
            print('Total pages: ' + str(data['books'][pickedBookID-1]['pages']))
            print('Published year: ' + str(data['books'][pickedBookID-1]['year']))
            print('Language: ' + data['books'][pickedBookID-1]['language'])
            print('Country: ' + data['books'][pickedBookID-1]['country'])
            print('Cover Image link: ' + data['books'][pickedBookID-1]['imageLink'])
            print('Website link: ' + data['books'][pickedBookID-1]['link'])

            if currentUser != "guest":
                possibleAnswers = ["1", "2", "9"]
                answer = ""
                while answer not in possibleAnswers:
                    print("\nWould you like to:\n 1. Loan a book\n 2. Browse books\n 9. Return to the main menu.\n")
                    answer = input(">> ")
                    if answer == "1":
                        LoanMenu()
                    elif answer == "2":
                        bookView()
                    elif answer == "9":
                        RunProgram()
                    else:
                        print("Input not recognised. Please try again. ")
                        answer = ""
            else:
                possibleAnswers = ["1", "2", "9"]
                answer = ""
                while answer not in possibleAnswers:
                    print("\nWould you like to:\n 1. Browse books\n 9. Return to the main menu.\n")
                    answer = input(">> ")
                    if answer == "1":
                        bookView()
                    elif answer == "9":
                        RunProgram()
                    else:
                        print("\nInput not recognised. Please try again.")
                        answer = ""

        bookView()

def importJSON():
    jsonbookfile = input("Type the name of the file here to load the books from JSON : ")
        
    try:
        with open(abs_path + f'//{jsonbookfile}.json') as f:
            jsonbookfile2 = json.load(f)

        with open(abs_path + '/data/books.json', 'w') as json_file:
            json.dump(jsonbookfile2, json_file, indent = 4)

        with open(abs_path + '/data/books.json') as f:
            data['books'] = json.load(f)

        with open(abs_path + '/data/members.json') as f:
            data['members'] = json.load(f)

        with open(abs_path + '/data/loanItems.json') as f:
            data['loanItems'] = json.load(f)

                
        for item in data['books']:
            AddToLoanItemsNew(item['title'], item['author'])
        print("Load succesfull. Press any key to continue...")
        a = input()
        RunProgram()

    except: 
        print("Load failed! Did you enter the correct filename?")
        a = input("Press any key to continue ...")
        RunProgram()

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
        print(f"Book ID: {item['bookID']}, Title: {item['title']}, Author: {item['author']}, Available: {item['isAvailable']}")

def addBookItem():
    print("hoi")

def editBookItem():
    print("hoi")

def deleteBookItem():
    print("hoi")

def searchBookItem():
    print("hoi")

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
        LoanMenu()


    for item in data['loanItems']:
        
        checkvar = json.loads(json.dumps(item))
        if checkvar['bookItem'] == targetbook and checkvar['author'] == targetauthor and checkvar['isAvailable'] == False:
            print("\nThis book is not available! Please return this book before trying to loan it.")
            decidedonbook = False
            a = input("\nPress any key to return to the loan menu.")
            LoanMenu()
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

def AddToLoanItemsNew(title, author):
    newloanitemdict = {"bookItem": title, "author": author, "dateOfLoan" : "none", "dateOfReturn" : "none", "userOfItem" : "none", "isAvailable" : True}
    for item in data['loanItems']:
        if (item['bookItem'] == title) and (item['author'] == author) :
            print(f"{item['bookItem']} already exists")
            return 

    data['loanItems'].append(newloanitemdict)
    BE.Backup.writeJson(abs_path + '/json/loanItems.json', data['loanItems'])

def LoanMenu():
    answer = ""
    if currentUser == "librarians":
        possibleanswers = ["1", "2", "3","9"]
        while answer not in possibleanswers:
            Start()
            print(f"\nLoan Menu\n\n 1. Loan a book to a customer \n 2. Return a loaned book \n 3. View loan administration \n 9. Return to main menu. \n")
            answer = input()
            if answer == "1":
                lendBookItem()
            elif answer == "2":
                ReturnLoanItem()
            elif answer == "3":
                print("You have selected 3. View loan administration")
                print("Viewing all loaned books. Press any key to continue... ")
                a = input()
                BE.LoanAdministration.GetInfo()
            elif answer == "9":
                RunProgram()
        RunProgram()
    elif currentUser == "members":
        possibleanswers = ["1", "9"]
        while answer not in possibleanswers:
            Start()
            print(f"\nLoan Menu\n\n 1. Loan a book\n 2. Return a loaned book\n 9. Return to main menu.\n")
            answer = input(">> ")
            if answer == "1":
                lendBookItem()
            elif answer == "2":
                ReturnLoanItem()
            elif answer == "9":
                RunProgram()
    elif currentUser == "guest":
        possibleanswers = ["1", "9"]
        while answer not in possibleanswers:
            Start()
            print("\nLoan Menu\n\nYou can only loan a book while logged in.\n")
            print(f"\n 1. Log in\n 9. Return to main menu.\n")
            if answer == "1":
                loginMenu()
            elif answer == "9":
                RunProgram()
            else:
                x = input("\nCommand not recognized. Enter any key and try again.\n")

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

        if currentUserName == item['userOfItem'] or currentUser == "libraryAdmin":

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
                        print("Something went horribly wrong. Please contact the servicedesk.")

                    a = input("Press any key to continue ...")
                elif answer == "2":
                    print("OK, not returning book. Heading back to main menu")
                    a = input("Press any key to continue ...")
        else:
            print("\nSorry you are not a librarian nor the user who has loaned this book. Therefor you can not return this book.")
            x = input("\nPress any key to return to the loan menu.")
            LoanMenu()
    else:
        print("Could not find the specified title / username combination. Did you enter the credentials correctly?")
        a = input("Press any key to continue to return to the Loan Menu.")
            
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