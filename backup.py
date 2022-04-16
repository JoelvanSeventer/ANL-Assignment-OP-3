import shutil
from datetime import datetime as d

class Catalog():
    def __init__(self):
        self.backup_path = 'data/backup/'
        now = str(d.now())[:10]
        now = now.replace(":","_")
        self.datetime = now

    def makeBackup(self):
        shutil.copy('data/books.json', self.backup_path + self.datetime + '_backup_books.json')
        shutil.copy('data/customers.csv', self.backup_path + self.datetime + '_backup_customers.csv')
        shutil.copy('data/loans.json', self.backup_path + self.datetime + '_backup_loans.json')
        shutil.copy('data/bookcopies.json', self.backup_path + self.datetime + '_backup_bookcopies.json')
        print("\nBackup complete!\n")

    def restoreDB(self):
        shutil.copy(self.backup_path + self.datetime + 'backupbooks.json', 'data/books.json')
        shutil.copy(self.backup_path + self.datetime + 'backupcustomers.csv', 'data/customers.csv')
        shutil.copy(self.backup_path + self.datetime + 'backuploans.json', 'data/loans.json')
        shutil.copy(self.backup_path + self.datetime + 'backupbookcopies.json', 'data/bookcopies.json')
        print("\nRestore complete!\n")
