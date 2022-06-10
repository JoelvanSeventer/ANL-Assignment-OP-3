import csv
class Person():
    
    # Add new member
    def newMember(self):
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
            exists = False
            username = input("Username: ").lower()
            with open("data/members.csv", "r") as f:
                csvdata = list(csv.reader(f))
            for user in csvdata:
                split_user = user[0].split(';') 
                if username == split_user[7].lower():
                    exists = True
                    print("This username is already in use.")
                    break
            if exists == False:
                running = False

        password = input("Password: ").lower()
        telephonenumber = input("Telephonenumber: ")

        with open("data/members.csv", "r") as f:
            csvdata = list(csv.reader(f))
            index = len(csvdata)
        data = f"\n{str(index)};{givenname};{surname};{streetaddress};{zipcode};{city};{emailaddress};{username};{password};{telephonenumber}"

        with open("data/members.csv", "a") as f:
            f.write(data)

    #Search member 
    def findmember(self):
        with open("data/members.csv", "r") as f:
            csvdata = list(csv.reader(f))
        running = True
        while running:
            check = input("\nWith which term would you like to search?\n1. Firstname\n2. Surname\n3. Streetaddress\n4. Zipcode\n5. City\n6. Emailaddress\n7. Username\n8. Telephonenumber\n")
            if check == '1' or check == '2' or check == '3' or check == '4' or check == '5' or check == '6' or check == '7' or check == '8':
                running = False
                break
            else:
                print("Please choose one of the terms")
            
        terms = ['Givenname', 'Surname', 'Streetaddress', 'Zipcode', 'City', 'Emailaddress', 'Username', 'Telephonenumber']
        
        usercheck = input(f"\nFill in the {terms[int(check) - 1]}:\n").lower()
        for user in csvdata:
            split_user = user[0].split(';') 
            if check == "1" and usercheck == split_user[1].lower():
                    print(split_user[0] + ". " + split_user[1] + " " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    
            if check == "2" and usercheck == split_user[2].lower():
                    print(split_user[0] + ". " + split_user[1] + " " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
            
            if check == "3" and usercheck == split_user[3].lower():
                    print(split_user[0] + ". " + split_user[1] + " " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])

            if check == "4" and usercheck == split_user[4].lower():
                    print(split_user[0] + ". " + split_user[1] + " " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
            
            if check == "5" and usercheck == split_user[5].lower():
                    print(split_user[0] + ". " + split_user[1] + " " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])

            if check == "6" and usercheck == split_user[6].lower():
                    print(split_user[0] + ". " + split_user[1] + " " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])

            if check == "7" and usercheck == split_user[7].lower():
                    print(split_user[0] + ". " + split_user[1] + " " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
            
            if check == "8"and usercheck == split_user[9].lower():
                    print(split_user[0] + ". " + split_user[1] + " " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
    
    #Delete member
    def deletemember(self):
        lines = list()
        members= input("Please enter a member's name to be deleted.")
        with open("data/members.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                lines.append(row)
                for mem in row:
                    if mem == members:
                        lines.remove(row)

        with open('mycsv.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    
    #Show all members
    def showAllmembers(self):
        with open("data/members.csv", "r") as f:
            csvdata = list(csv.reader(f))
        index = 0
        for user in csvdata:
            for i in user:
                if index > 0:
                    memlist = i.split(';')
                    print(memlist[0] + ". " + memlist[1] + " " + memlist[2])
                index += 1

    #Edit member
    def editmember(self):
        with open("data/members.csv", "r") as f:
            csvdata = list(csv.reader(f))

        check = ""
        running = True
        while running:
            check = input("\nWhich term would you like to edit?\n1.Givenname\n2. Surname\n3. Streetaddress\n4. Zipcode\n5. City\n6. Emailaddress\n7. Username\n8. Telephonenumber\n")
            if check == '1' or check == '2' or check == '3' or check == '4' or check == '5' or check == '6' or check == '7' or check == '8':
                running = False
                break
            else:
                print("Please choose one of the options.")

        active = True
        while active:
            exists = False	
            username = input("Please enter the username of the member you want to edit: ").lower()
            for user in csvdata:
                thisuser = user[0].split(';')
                if username == thisuser[7].lower():
                    print("User found!")
                    exists = True
                    new_value = input("What new value do you want to insert?")

                    with open ('data/members.csv', 'w') as f:
                        writer = csv.writer(f)
                        index = thisuser[0]
                        s = ""
                        for row in csvdata:
                            row_list = row[0].split(';')
                            print(index)
                            print(row_list[0])
                            if row_list[0] == index:
                                for i in range(len(thisuser)):
                                    if i == int(check) and i == len(thisuser) - 1:
                                        s += new_value
                                    elif i == int(check) and i != len(thisuser) - 1:
                                        s += new_value + ";"
                                    elif i == len(thisuser) - 1:
                                        s += thisuser[i]
                                    else: 
                                        s += thisuser[i] + ";"
                                print("s = ", s)
                                for line in csvdata:
                                    line_list = line[0].split(';')
                                    if line_list[0] == index:
                                        writer.writerow(s)
                                
            if exists:
                active = False

                
                    #     index = int(thisuser[0])
                    #     thisuser[int(check)] = new_value
                    #     s = ""
                    #     for i in range(len(thisuser)):
                    #         if i == len(thisuser) - 1:
                    #             s += thisuser[i]
                    #             break
                    #         s += thisuser[i] + ";"
                    #     f[index].write(s)
                    # active = False
                    
        
        # while running:
        #     exists = False
        #     username = input("Username: ").lower()
        #     with open("data/members.csv", "r") as f:
        #         csvdata = list(csv.reader(f))
        #     for user in csvdata:
        #         split_user = user[0].split(';') 
        #         if username == split_user[7].lower():
        #             exists = True
        #             print("This username is already in use.")
        #             break
        #     if exists == False:
        #         running = False
        
        
    def EditMember(self, check, username):
        csvdata = open('data/members.csv', 'r+')
        terms = ['Givenname', 'Surname', 'Streetaddress', 'Zipcode', 'City', 'Emailaddress', 'Username', 'Telephonenumber']
        for user in csvdata:
            thisuser = user.split(';')
            if username == thisuser[7]:

                if check == "1":
                    print("\nThe current Givenname is: " + thisuser[1])
                    thisuser[1] = input(f"\nFill in the new {terms[int(check)-1]}:\n").lower()
                    

                elif check == "2":
                    thisuser[2] = input(f"\nFill in the new {terms[int(check)-1]}:\n").lower()
                    break

                elif check == "3":
                    thisuser[3] = input(f"\nFill in the new {terms[int(check)-1]}:\n").lower()
                    break

                elif check == "4":
                    thisuser[4] = input(f"\nFill in the new {terms[int(check)-1]}:\n").lower()
                    break

                elif check == "5":
                    thisuser[5] = input(f"\nFill in the new {terms[int(check)-1]}:\n").lower()
                    break

                elif check == "6":
                    thisuser[6] = input(f"\nFill in the new {terms[int(check)-1]}:\n").lower()
                    break

                elif check == "7":
                    thisuser[7] = input(f"\nFill in the new {terms[int(check)-1]}:\n").lower()
                    break
                
                elif check == "8":
                    thisuser[8] = input(f"\nFill in the new {terms[int(check)-1]}:\n").lower()
                    break

                thisuser = ';'.join(thisuser)
                csvdata.write(thisuser)
                break
        csvdata.close()

    #add list of members
    def addListOfMembers(self):
        listofmembers = input(f"\nFill in the list of members you want to add:\n")
        print(listofmembers)
        with open("data/members.csv", "a") as f:
            writer = csv.writer(f)
            for i in range(len(listofmembers)):
                addmem = []
                for i in range(0, 10):
                    print(listofmembers[i])
                    addmem.append(listofmembers[i])
                writer.writerow(addmem)
                i+= 9
        print("\nList of members added.")
        return