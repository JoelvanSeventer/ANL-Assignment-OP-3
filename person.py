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

    mayAddBooks = True
    @staticmethod
    def addMember(firstname, surname, streetaddress, zipcode, city, emailaddress, username, password, telephonenumber):
        
        Number = str(len(data['members'])+1)
        data['members'].append({
            'Number' : Number,
            'GivenName' : firstname,
            'Surname' : surname,
            'StreetAddress' : streetaddress,
            'ZipCode' : zipcode,
            'City' : city,
            'EmailAddress' : emailaddress,
            'Username' : username,
            'Password' : password,
            'TelephoneNumber' : telephonenumber,
        })
        Backup.writeJson(abs_path + '/data/members.json', data['members'])

    @staticmethod
    def editMember(inputName, edit):
        for member in data['members']:
            if inputName == member["GivenName"].lower() + " " + member["Surname"].lower():
                member[edit] = input("Enter new " + edit + ": ")
                Backup.writeJson(abs_path + '/data/members.json', data['members'])
                return True
        return False

    @staticmethod
    def registerBook(author, country, imageLink, language, link, pages, title, year):
        data['catalog'].append({
            'title': title,
            'author': author,
            'pages': pages,
            'year': year,
            'country': country,
            'language': language,
            'imageLink': imageLink,
            'link': link
        })
        Backup.writeJson(abs_path + '/data/catalog.json', data['books'])


class Member(Person):

    def __init__(self, Number, GivenName, SurName, StreetAdress, ZipCode, City, EmailAdress, Username, Password, TelephoneNumber):
        self.Number = Number
        self.GivenName = GivenName
        self.SurName = SurName
        self.StreetAdress = StreetAdress
        self.ZipCode = ZipCode
        self.City = City
        self.EmailAdress = EmailAdress
        self.Username = Username
        self.Password = Password
        self.TelephoneNumber = TelephoneNumber

    def __str__(self):
        return f"Usernumber: {self.Number}\nName: {self.GivenName} {self.SurName}\nUsername: {self.Username} \n"
