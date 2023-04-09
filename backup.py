import os
import json

from data import data, abs_path


class Backup:
    listOfMembers = list()

    @staticmethod
    def writeJson(filePath, dataName, readmode = 'w'):
        with open(filePath, readmode) as json_file:
            json.dump(dataName, json_file, indent=4)

    @staticmethod
    def backupSystem():
        global data
        with open(abs_path + '/data/backup.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def loginMember(userInput, passInput, loginType, nameType = "Username", passwordType = "Password"):
        global data
        loggedIn = False
        with open(abs_path + f'/data/members.json') as f:
            data[loginType] = json.load(f)
            for i in data[loginType]:
                if userInput == i[nameType] and passInput == i[passwordType]:
                    loggedIn = True
                    return (loggedIn, loginType, i["Username"])
                else:
                    loggedIn = False
        return (loggedIn, loginType, "guest")
    
    @staticmethod
    def loginLibraryAdmin(userInput, passInput, loginType):
        global data
        loggedIn = False
        if userInput == "admin" and passInput == "admin123":
            loggedIn = True
            return (loggedIn, loginType, "libraryAdmin")
        else:
            loggedIn = False
        return (loggedIn, loginType, "guest")
    
    
        


    @staticmethod
    def loadSystemBackup():
        global data
        filename = input("Enter backup filename here: ")
        with open(abs_path + f'/data/{filename}.json') as f:
            data = json.load(f)
            Backup.writeJson(abs_path + '/data/members.json', data['members'])
            Backup.writeJson(abs_path + '/data/loanItems.json', data['loanItems'])
            Backup.writeJson(abs_path + '/data/catalog.json', data['books'])
        with open(abs_path + '/data/books.json') as f:
        	data['books'] = json.load(f)