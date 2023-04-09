import os
import json
import csv
from datetime import datetime

abs_path = os.path.dirname(__file__)

data = {}
data['members'] = []
data['books'] = []
data['bookcopies'] = []
data['loans'] = []


try:
    
    with open(abs_path + '/data/books.json') as f:
        data['books'] = json.load(f) 

    with open(abs_path + '/data/members.json') as f:
        data['members'] = json.load(f)

    with open(abs_path + '/data/bookcopies.json') as f:
        data['bookcopies'] = json.load(f)

    with open(abs_path + '/data/loans.json') as f:
        data['loans'] = json.load(f)

except: 
    
    # check if path data/backup exists
    if not os.path.exists(abs_path + '/data/backup'):
        print("NO BACKUP")
        # create new directory named "data"
        os.mkdir(abs_path + '/data')
        
        #init json files of variable "data"
        with open(abs_path + '/data/books.json', 'w') as json_file:
            json.dump(data['books'], json_file, indent=4)
        
        with open(abs_path + '/data/members.json', 'w') as json_file:
            json.dump(data['members'], json_file, indent=4)
        
        with open(abs_path + '/data/bookcopies.json', 'w') as json_file:
            json.dump(data['bookcopies'], json_file, indent=4)

        with open(abs_path + '/data/loans.json', 'w') as json_file:
            json.dump(data['loans'], json_file, indent=4)
        

    else:
        print("RESTORING BACKUP")

       

        # get all files in data/backup
        files = os.listdir(abs_path + '/data/backup')

        filenames = ["books", "members", "bookcopies", "loans"]

        for name in filenames:
            version = 0
            date = None
            for filename in os.listdir("data/backup"):
                if name in str(filename):
                    #strip the filename and return the version number
                    # For example: 2020-12-12_1_backupbooks.json should give me 1

                    foundVersion = int(filename.split("_")[1])
                    foundDate = filename.split("_")[0]

                    #convert foundDate to DateTime
                    foundDate = datetime.strptime(foundDate, '%Y-%m-%d')
                    


                    #compare date and version, if more recent assign to version and date
                    if date == None:
                        version = foundVersion
                        date = foundDate
                    elif foundDate > date:
                        version = foundVersion
                        date = foundDate
                    elif foundDate == date:
                        if foundVersion > version:
                            version = foundVersion
                            date = foundDate
                            

            if version == 0 and date == None:
                data[name] = []
            
            else:

                #format date to uear-month-day
                date = date.strftime("%Y-%m-%d")
                

                #write the data from the backup file with the matching version to data
                with open(abs_path + f'/data/backup/{date}_{version}_backup{name}.json') as f:
                    data[name] = json.load(f)

            #write to file "books.json" in data
            with open(abs_path + f'/data/{name}.json', 'w') as json_file:
                json.dump(data[name], json_file, indent=4)
                


    