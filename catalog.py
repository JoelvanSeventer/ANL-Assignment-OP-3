import os
import json
from data import data, abs_path

class Catalog:

    bookList = []

    @staticmethod
    def GetInfo():
        bookIDCounter = 0
        for book in data['catalog']:
            bookIDCounter += 1
            print(f"Book ID: {bookIDCounter}")
            print('Title: ' + book['title'])
            print('Author: ' + book['author'])
            print('Language: ' + book['language'])
            print('')
        return bookIDCounter