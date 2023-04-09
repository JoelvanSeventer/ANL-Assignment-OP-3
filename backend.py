import os
import json
from data import data, abs_path

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

from backup import Backup
from book import Book
from bookItem import BookItem
from catalog import Catalog
from loanItem import LoanItem
from person import Person, LibraryAdmin, Member
from loanAdministration import LoanAdministration