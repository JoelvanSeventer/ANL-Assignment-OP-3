import shutil

class Catalog():
    def __init__(self):
        self.backup_path = 'data/backup/'

    def makeBackup(self):
        shutil.copy('data/books.json', self.backup_path + 'backupbooks.json')
        shutil.copy('data/customers.csv', self.backup_path + 'backupcustomers.csv')
        shutil.copy('data/loans.json', self.backup_path + 'backuploans.json')
        shutil.copy('data/bookcopies.json', self.backup_path + 'backupbookcopies.json')

    def restoreDB(self):
        shutil.copy(self.backup_path + 'backupbooks.json', 'data/books.json')
        shutil.copy(self.backup_path + 'backupcustomers.csv', 'data/customers.csv')
        shutil.copy(self.backup_path + "backuploans.json", 'data/loans.json')
        shutil.copy(self.backup_path + 'backupbookcopies.json', 'data/bookcopies.json')
