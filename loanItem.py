import os
import json
from data import data, abs_path

class LoanItem:

    def __init__(self, whichBook, dateOfLoan, dateOfReturn, username):

        self.bookItem = whichBook
        self.dateOfLoan = dateOfLoan
        self.dateOfReturn = dateOfReturn
        self.userOfItem = username
