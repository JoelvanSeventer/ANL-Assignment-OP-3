import csv
class Person():
    
    def addCustomer(self):
        print("\nFill in the following")
        gender = input("Gender: ")
        nameset = input("Nameset: ")
        givenname = input('Givenname: ')
        surname = input('Surname: ')
        streetaddress = input('Streetaddress: ')
        zipcode = input("Zipcode: ")
        city = input("City: ")
        emailaddress = input("Emailaddress: ")

        running = True
        while running:
            username = input('Username: ')
            count = 0
            with open('database/customers.csv', 'r') as f:
                csvdata = list(csv.reader(f))
            for user in csvdata:
                if username == user[9]:
                    print("This username is already in use.")
                    count = 1
                else: 
                    count = 0
            if count == 0:
                running = False
                break

        telephonenumber = input('Telephonenumber: ')

        with open('database/customers.csv', 'r') as f:
            csvdata = list(csv.reader(f))
            index = len(csvdata)
            
        data = f"\n{str(index)},{gender},{nameset},{givenname},{surname},{streetaddress},{zipcode},{city},{emailaddress},{username},{telephonenumber}"

        with open('database/customers.csv', 'a') as f:
            f.write(data)
      
    def searchCustomer(self):
        with open('database/customers.csv', 'r') as f:
            csvdata = list(csv.reader(f))
        running = True
        while running:
            check = input("\nVia what term would you like to search? Gender, Nameset, Givenname, Surname, Streetaddress, Zipcode, City, Emailaddress, Username, Telephonenumber:\n").lower()
            if check == 'gender' or check == 'nameset' or check == 'givenname' or check == 'surname' or check == 'streetaddress' or check == 'zipcode' or check == 'city' or check == 'emailaddress' or check == 'username' or check == 'telephonenumber':
                running = False
                break
            else:
                print("Please choose one of the given terms!")
        
        usercheck = input(f"\nFill in the {check}:\n").lower()
        for user in csvdata:
            if check == "gender":
                if usercheck in user[1].lower():
                    print(user)

            if check == "nameset":
                if usercheck in user[2].lower():
                    print(user)

            if check == "givenname":
                if usercheck in user[3].lower():
                    print(user)

            if check == "surname":
                if usercheck in user[4].lower():
                    print(user)

            if check == "streetaddress":
                if usercheck in user[5].lower():
                    print(user)

            if check == "zipcode":
                if usercheck in user[6].lower():
                    print(user)

            if check == "city":
                if usercheck in user[7].lower():
                    print(user)

            if check == "emailaddress":
                if usercheck in user[8].lower():
                    print(user)

            if check == "username":
                if usercheck in user[9].lower():
                    print(user)

            if check == "telephonenumber":
                if usercheck in user[10].lower():
                    print(user)
            