import csv
class Person():
    
    # Add new customer
    def NewCustomer(self):
        print("\nFill in your information below: ")
        givenname = input("Givenname: ")
        surname = input("Surname: ")
        streetaddress = input("Streetaddress: ")
        zipcode = input("Zipcode: ")
        city = input("City: ")
        emailaddress = input("Emailaddress: ")

        #Fill in Username and check if available 
        running = True
        while running:
            username = input("Username: ").lower()
            with open("data/customers.csv", "r") as f:
                csvdata = list(csv.reader(f))
            for user in csvdata:
                if username == user[9]:
                    print("This username is already in use.")
                    running = False
            if running == True:
                break
        password = input("Password: ").lower()
        telephonenumber = input("Telephonenumber: ")

        with open("data/customers.csv", "r") as f:
            csvdata = list(csv.reader(f))
            index = len(csvdata)
        data = f"\n{str(index)},{givenname},{surname},{streetaddress},{zipcode},{city},{emailaddress},{username}, {password}, {telephonenumber}"

        with open("data/customers.csv", "a") as f:
            f.write(data)

    #Search customer 
    def findCustomer(self):
        with open("data/customers.csv", "r") as f:
            csvdata = list(csv.reader(f))
        running = True
        while running:
            check = input("\nWith which term would you like to search?\n1.Givenname\n2. Surname\n3. Streetaddress\n4. Zipcode\n5. City\n6. Emailaddress\n7. Username\n8. Telephonenumber\n")
            if check == '1' or check == '2' or check == '3' or check == '4' or check == '5' or check == '6' or check == '7' or check == '8':
                running = False
                break
            else:
                print("Please choose one of the terms")
            
        terms = ['Givenname', 'Surname', 'Streetaddress', 'Zipcode', 'City', 'Emailaddress', 'Username', 'Telephonenumber']
        
        usercheck = input(f"\nFill in the {terms[check-1]}:\n").lower()
        for user in csvdata:
            if check == "1":
                if usercheck in user[1].lower():
                    print(user)

            if check == "2":
                if usercheck in user[2].lower():
                    print(user)

            if check == "3":
                if usercheck in user[3].lower():
                    print(user)

            if check == "4":
                if usercheck in user[4].lower():
                    print(user)

            if check == "5":
                if usercheck in user[5].lower():
                    print(user)

            if check == "6":
                if usercheck in user[6].lower():
                    print(user)

            if check == "7":
                if usercheck in user[7].lower():
                    print(user)
            
            if check == "8":
                if usercheck in user[9].lower():
                    print(user)
    
    #Delete customer
    def deleteCustomer(self):
        lines = list()
        members= input("Please enter a member's name to be deleted.")
        with open("data/customers.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                lines.append(row)
                for mem in row:
                    if mem == members:
                        lines.remove(row)

        with open('mycsv.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)