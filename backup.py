import shutil
from datetime import datetime as d
import os.path
import os

class Catalog():
    def __init__(self):
        self.backup_path = 'data/backup/'
        now = str(d.now())[:10]
        now = now.replace(":","_")
        self.datetime = now

    def makeBackup(self):

        count = 0
        running = True
        while running:

            print(os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupbooks.json'}"))
            print(f"{self.backup_path} + {self.datetime + '_' + str(count) + '_' + 'backupbooks.json'}")

            if os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupbooks.json'}") == False:
                shutil.copy('data/books.json', self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupbooks.json')
                running = False
            elif os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupbooks.json'}"):
                count += 1
        
        count = 0
        running = True
        while running:
            if not os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupmembers.csv'}"):
                shutil.copy('data/members.csv', self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupmembers.csv')
                running = False
            elif os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupmembers.csv'}"):
                count += 1

        count = 0
        running = True
        while running:
            if not os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backuploans.json'}"):
                shutil.copy('data/loans.json', self.backup_path + self.datetime + '_' + str(count) + '_' + 'backuploans.json')
                running = False
            elif os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backuploans.json'}"):
                count += 1
        
        count = 0
        running = True
        while running:
            if not os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupbookcopies.json'}"):
                shutil.copy('data/bookcopies.json', self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupbookcopies.json')
                running = False
            elif os.path.exists(f"{self.backup_path + self.datetime + '_' + str(count) + '_' + 'backupbookcopies.json'}"):
                count += 1
        
        # shutil.copy('data/members.csv', self.backup_path + self.datetime + 'backupmembers.csv')
        # shutil.copy('data/loans.json', self.backup_path + self.datetime + 'backuploans.json')
        # shutil.copy('data/bookcopies.json', self.backup_path + self.datetime + 'backupbookcopies.json')
        print("\nBackup complete!\n")

    def RestoreBackup(self):
        condition = True
        while condition:
            choice = input("\n1. Restore books\n2. Restore members\n3. Restore loans\n4. Restore bookcopies\n")
            if choice == '1':

                dir_path = "data/backup"

                files = []

                for filename in os.listdir(dir_path):
                    if "backupbooks.json" in str(filename):
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
                

                shutil.copy(self.backup_path + self.datetime + '_' + str(copy_version - 1) + '_' + "backupbooks.json", 'data/books.json')

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
                    if "backupmembers.csv" in str(filename):
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
                

                shutil.copy(self.backup_path + self.datetime + '_' + str(copy_version - 1) + '_' + 'backupmembers.csv', 'data/members.csv')

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
                

                shutil.copy(self.backup_path + self.datetime + '_' + str(copy_version - 1) + '_' + 'backuploans.json', 'data/loans.json')

                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    break

            elif choice == '4':


                dir_path = "data/backup"

                files = []

                for filename in os.listdir(dir_path):
                    if "backupbookcopies.json" in str(filename):
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
                

                shutil.copy(self.backup_path + self.datetime + '_' + str(copy_version - 1) + '_' + 'backupbookcopies.json', 'data/bookcopies.json')

                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    break
