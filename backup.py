import os
import json
import shutil
from datetime import datetime as d
from data import data, abs_path


class Backup:
    listOfMembers = list()

    @staticmethod
    def writeJson(filePath, dataName, readmode = 'w'):
        with open(filePath, readmode) as json_file:
            json.dump(dataName, json_file, indent=4)

    @staticmethod
    def backupSystem():
        now = str(d.now())[:10]
        now = now.replace(":","_")
        file = 'data/backup/'
        count = 0
        running = True

        while running:

            print(os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backupcatalog.json'}"))
            print(f"{file} + {now + '_' + str(count) + '_' + 'backupcatalog.json'}")

            if not os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backupcatalog.json'}") == False:
                shutil.copy('data/catalog.json', file + now + '_' + str(count) + '_' + 'backupcatalog.json')
                running = False
            elif os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backupcatalog.json'}"):
                count += 1
        
        count = 0
        running = True
        while running:
            if not os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backupmembers.json'}"):
                shutil.copy('data/members.json', file + now + '_' + str(count) + '_' + 'backupmembers.json')
                running = False
            elif os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backupmembers.json'}"):
                count += 1

        count = 0
        running = True
        while running:
            if not os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backuploanItems.json'}"):
                shutil.copy('data/loanItems.json', file + now + '_' + str(count) + '_' + 'backuploanItems.json')
                running = False
            elif os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backuploanItems.json'}"):
                count += 1
        
        count = 0
        running = True
        while running:
            if not os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backupbookItems.json'}"):
                shutil.copy('data/bookItems.json', file + now + '_' + str(count) + '_' + 'backupbookItems.json')
                running = False
            elif os.path.exists(f"{file + now + '_' + str(count) + '_' + 'backupbookItems.json'}"):
                count += 1

    @staticmethod
    def loginMember(userInput, passInput, loginType, nameType = "Username", passwordType = "Password"):
        global data
        loggedIn = False
        with open(abs_path + f'/data/members.json') as f:
            data[loginType] = json.load(f)
            for i in data[loginType]:
                if userInput == i[nameType] and passInput == i[passwordType]:
                    loggedIn = True
                    return (loggedIn, loginType, i["Username"])
                else:
                    loggedIn = False
        return (loggedIn, loginType, "guest")
    
    @staticmethod
    def loginLibraryAdmin(userInput, passInput, loginType):
        global data
        loggedIn = False
        if userInput == "admin" and passInput == "admin123":
            loggedIn = True
            return (loggedIn, loginType, "libraryAdmin")
        else:
            loggedIn = False
        return (loggedIn, loginType, "guest")
    
    # @staticmethod
    # def loadSystemBackup():
    #     global data
    #     filename = input("Enter backup filename here: ")
    #     with open(abs_path + f'/data/{filename}.json') as f:
    #         data = json.load(f)
    #         Backup.writeJson(abs_path + '/data/members.json', data['members'])
    #         Backup.writeJson(abs_path + '/data/loanItems.json', data['loanItems'])
    #         Backup.writeJson(abs_path + '/data/catalog.json', data['books'])
    #     with open(abs_path + '/data/books.json') as f:
    #     	data['books'] = json.load(f)

    def RestoreBackup():
        now = str(d.now())[:10]
        now = now.replace(":","_")
        file = 'data/backup/'
        condition = True

        while condition:
            choice = input("\n1. Restore books\n2. Restore members\n3. Restore loans\n4. Restore bookcopies\n")
            if choice == '1':

                dir_path = "data/backup"

                files = []

                for filename in os.listdir(dir_path):
                    if "backupcatalog.json" in str(filename):
                        files.append(str(filename))
                
                print("\nWhich version would you like to restore?\n")
                count = 0
                for i in range(len(files)):
                    print(f"{count + 1}. {files[count]}")
                    count += 1

                running = True
                while running:
                    invalidInput = False
                    copy_version = input("")

                    if not copy_version.isnumeric():
                        print("\nInvalid input")
                        print("Please enter an integer\n")
                    
                    if invalidInput == False:
                        copy_version = int(copy_version)
                        running = False
                

                shutil.copy(file + now + '_' + str(copy_version - 1) + '_' + "backupbooks.json", 'data/books.json')

                print("\nRestore complete!\n")

                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    print("\nThanks for visiting! See you next time!")
                    break

            elif choice == '2':

                dir_path = "data/backup"

                files = []

                for filename in os.listdir(dir_path):
                    if "backupmembers.json" in str(filename):
                        files.append(str(filename))
                
                print("\nWhich version would you like to restore?\n")
                count = 0
                for i in range(len(files)):
                    print(f"{count + 1}. {files[count]}")
                    count += 1

                running = True
                while running:
                    invalidInput = False
                    copy_version = input("")

                    if not copy_version.isnumeric():
                        print("\nInvalid input")
                        print("Please enter an integer\n")
                    
                    if invalidInput == False:
                        copy_version = int(copy_version)
                        running = False
                

                shutil.copy(file + now + '_' + str(copy_version - 1) + '_' + 'backupmembers.json', 'data/members.json')

                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    break

            elif choice == '3':

                dir_path = "data/backup"

                files = []

                for filename in os.listdir(dir_path):
                    if "backuploans.json" in str(filename):
                        files.append(str(filename))
                
                print("\nWhich version would you like to restore?\n")
                count = 0
                for i in range(len(files)):
                    print(f"{count + 1}. {files[count]}")
                    count += 1

                running = True
                while running:
                    invalidInput = False
                    copy_version = input("")

                    if not copy_version.isnumeric():
                        print("\nInvalid input")
                        print("Please enter an integer\n")
                    
                    if invalidInput == False:
                        copy_version = int(copy_version)
                        running = False
                

                shutil.copy(file + now + '_' + str(copy_version - 1) + '_' + 'backuploanItems.json', 'data/loanItems.json')

                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    break

            elif choice == '4':


                dir_path = "data/backup"

                files = []

                for filename in os.listdir(dir_path):
                    if "backupbookItems.json" in str(filename):
                        files.append(str(filename))
                
                print("\nWhich version would you like to restore?\n")
                count = 0
                for i in range(len(files)):
                    print(f"{count + 1}. {files[count]}")
                    count += 1

                running = True
                while running:
                    invalidInput = False
                    copy_version = input("")

                    if not copy_version.isnumeric():
                        print("\nInvalid input")
                        print("Please enter an integer\n")
                    
                    if invalidInput == False:
                        copy_version = int(copy_version)
                        running = False
                

                shutil.copy(file + now + '_' + str(copy_version - 1) + '_' + 'backupbookItems.json', 'data/bookItems.json')

                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    break

                
    