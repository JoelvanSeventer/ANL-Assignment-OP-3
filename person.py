import os
import json
from data import data, abs_path
from backup import Backup

class Person:

    def __init__(self, name, username):
        self.Name = name
        self.userName = username

    
class LibraryAdmin(Person):
    global data

    def __init__(self, name, username, password):
        Person.__init__(self, name, username)
        self.password = password

    def __str__(self):
        return f" Name: {self.Name} \n Username: {self.userName} \n"
    
    def revealpassword(self):
        print(self.password)

    mayAddBooks = True
    @staticmethod
    def addMember(nameSet, customergender, customerfirstname, customerlastname, customerstreetaddress, customerzipcode, customercity, customeremailaddress, customertelephonenumber):
        
        customerNumber = str(len(data['customers'])+1)
        data['customers'].append({
            'Number' : customerNumber,
            'NameSet' : nameSet,
            'Gender' : customergender,
            'GivenName' : customerfirstname,
            'Surname' : customerlastname,
            'StreetAddress' : customerstreetaddress,
            'ZipCode' : customerzipcode,
            'City' : customercity,
            'EmailAddress' : customeremailaddress,
            'TelephoneNumber' : customertelephonenumber,
            'name': customerfirstname,
        })
        Backup.writeJson(abs_path + '/json/customers.json', data['customers'])

    @staticmethod
    def registerBook(author, country, imageLink, language, link, pages, title, year):
        data['books'].append({
            'title': title,
            'author': author,
            'pages': pages,
            'year': year,
            'country': country,
            'language': language,
            'imageLink': imageLink,
            'link': link
        })
        Backup.writeJson(abs_path + '/json/books.json', data['books'])


class Member(Person):

    def __init__(self, userNumber, gender, nameSet, givenName, surName, streetAdress, zipCode, city, emailAdress, telephoneNumber):
        self.userNumber = userNumber
        self.gender = gender
        self.nameSet = nameSet
        self.givenName = givenName
        self.surName = surName
        self.streetAdress = streetAdress
        self.zipCode = zipCode
        self.city = city
        self.emailAdress = emailAdress
        self.telephoneNumber = telephoneNumber
        self.name = givenName

    def __str__(self):
        return f"Usernumber: {self.userNumber}\nName: {self.givenName} {self.surName}\nUsername: {self.emailAdress} \n"

    @staticmethod
    def revealpassword(self):
        print(self.zipCode)