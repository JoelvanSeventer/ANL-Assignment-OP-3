import os
import json
from data import data, abs_path

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

from backup import Backup
from book import Book
from book import BookItem
from book import Book
from loans import LoanItem
from person import Person
from loans import LoanAdministration