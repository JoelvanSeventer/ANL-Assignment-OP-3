import csv
class Person():
    
    # Add new customer
    def NewCustomer(self):
        print("\nFill in your information below: ")
        gender = input("Gender: ")
        nameset = input("Nameset: ")
        givenname = input("Givenname: ")
        surname = input("Surname: ")
        streetaddress = input("Streetaddress: ")
        zipcode = input("Zipcode: ")
        city = input("City: ")
        emailaddress = input("Emailaddress: ")

        #Fill in Username and check if available 
        running = True
        while running:
            username = input("Username: ")
            with open("data/customers.csv", "r") as f:
                csvdata = list(csv.reader(f))
            for user in csvdata:
                if username == user[9]:
                    print("This username is already in use.")
                    running = False
            if running == True:
                break

        telephonenumber = input("Telephonenumber: ")

        with open("data/customers.csv", "r") as f:
            csvdata = list(csv.reader(f))
            index = len(csvdata)
            
        data = f"\n{str(index)},{gender},{nameset},{givenname},{surname},{streetaddress},{zipcode},{city},{emailaddress},{username},{telephonenumber}"

        with open("data/customers.csv", "a") as f:
            f.write(data)

    #Search customer 
    def findCustomer(self):
        with open("data/customers.csv", "r") as f:
            csvdata = list(csv.reader(f))
        running = True
        while running:
            check = input("\nWith which term would you like to search? Gender, Nameset, Givenname, Surname, Streetaddress, Zipcode, City, Emailaddress, Username, Telephonenumber:\n").lower()
            if check == 'gender' or check == 'nameset' or check == 'givenname' or check == 'surname' or check == 'streetaddress' or check == 'zipcode' or check == 'city' or check == 'emailaddress' or check == 'username' or check == 'telephonenumber':
                running = False
                break
            else:
                print("Please choose one of the terms")
        
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
            