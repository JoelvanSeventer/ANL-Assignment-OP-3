import shutil
from datetime import datetime as d

class Backup():
    def __init__(self):
        self.backup_path = 'data/backup/'
        now = str(d.now())[:10]
        now = now.replace(":","_")
        self.datetime = now

    def makeBackup(self):
        shutil.copy('data/books.json', self.backup_path + self.datetime + 'backupbooks.json')
        shutil.copy('data/members.csv', self.backup_path + self.datetime + 'backupmembers.csv')
        shutil.copy('data/loans.json', self.backup_path + self.datetime + 'backuploans.json')
        shutil.copy('data/bookcopies.json', self.backup_path + self.datetime + 'backupbookcopies.json')
        print("\nBackup complete!\n")

    def RestoreBackup(self):
        condition = True
        while condition:
            choice = input("\n1. Restore books\n2. Restore members\n3. Restore loans\n4. Restore bookcopies\n")
            if choice == '1':
                shutil.copy(self.backup_path + self.datetime + 'backupbooks.json', 'data/books.json')
                
                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    print("\nThanks for visiting! See you next time!")
                    break

            elif choice == '2':
                shutil.copy(self.backup_path + self.datetime + 'backupmembers.csv', 'data/members.csv')

                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    break

            elif choice == '3':
                shutil.copy(self.backup_path + self.datetime + 'backuploans.json', 'data/loans.json')

                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    break

            elif choice == '4':
                shutil.copy(self.backup_path + self.datetime + 'backupbookcopies.json', 'data/bookcopies.json')

                print("\nRestore complete!\n")
                proceed = input("\nDo you want to continue y/n: ")

                if proceed.lower() == "n" or proceed.lower() == "no":
                    condition = False
                    break
