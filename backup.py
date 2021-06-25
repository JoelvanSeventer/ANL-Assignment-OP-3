import shutil

class Catalog():
    def __init__(self):
        self.backup_path = 'database/backup/'

    def makeBackup(self):
        shutil.copy('database/books.json', self.backup_path + 'backupbooks.json')
        shutil.copy('database/customers.csv', self.backup_path + 'backupcustomers.csv')
        shutil.copy('database/loans.json', self.backup_path + 'backuploans.json')
        shutil.copy('database/bookcopies.json', self.backup_path + 'backupbookcopies.json')

    def restoreDB(self):
        shutil.copy(self.backup_path + 'backupbooks.json', 'database/books.json')
        shutil.copy(self.backup_path + 'backupcustomers.csv', 'database/customers.csv')
        shutil.copy(self.backup_path + "backuploans.json", 'database/loans.json')
        shutil.copy(self.backup_path + 'backupbookcopies.json', 'database/bookcopies.json')
