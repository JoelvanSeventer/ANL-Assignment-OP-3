import os
import json
from data import data, abs_path

class LoanAdministration: 

    loanItems = []

    @staticmethod
    def GetInfo():
        checkvar = json.loads(json.dumps(data['loanItems']))
        if len(checkvar) != 0:
            for item in checkvar: 
                if item['isAvailable'] == False:
                    print(f"{item['bookItem']} is loaned to {item['userOfItem']} from {item['dateOfLoan']} until {item['dateOfReturn']}")
            a = input("Press any key to continue")
        else:
            print("There are no books loaned out right now.\n")
            a = input("Press any key to continue")