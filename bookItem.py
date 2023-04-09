import os
import json
from data import data, abs_path

class BookItem:

    def __init__(self, book, amount):
        self.book = book
        self.amount = amount