import csv

import os


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

        with open("data/members.csv", "a", newline='') as f:
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
        
        isfound = False
        while isfound == False:
            usercheck = input(f"\nFill in the {terms[int(check) - 1]}:\n").lower()
            
            
            for user in csvdata:
                split_user = user[0].split(';') 
                if check == "1" and usercheck == split_user[1].lower():
                    isfound = True
                    print("\nFirstname: " + split_user[1] + "\nSurname: " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    break

                if check == "2" and usercheck == split_user[2].lower():
                    isfound = True
                    print("\nFirstname: " + split_user[1] + "\nSurname: " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    break

                if check == "3" and usercheck == split_user[3].lower():
                    isfound = True
                    print("\nFirstname: " + split_user[1] + "\nSurname: " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    break

                if check == "4" and usercheck == split_user[4].lower():
                    isfound = True
                    print("\nFirstname: " + split_user[1] + "\nSurname: " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    break

                if check == "5" and usercheck == split_user[5].lower():
                    isfound = True
                    print("\nFirstname: " + split_user[1] + "\nSurname: " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    break

                if check == "6" and usercheck == split_user[6].lower():
                    isfound = True
                    print("\nFirstname: " + split_user[1] + "\nSurname: " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    break

                if check == "7" and usercheck == split_user[7].lower():
                    isfound = True
                    print("\nFirstname: " + split_user[1] + "\nSurname: " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    break

                if check == "8"and usercheck == split_user[9].lower():
                    isfound = True
                    print("\nFirstname: " + split_user[1] + "\nSurname: " + split_user[2] + "\nStreetaddress: " + split_user[3] + "\nZipcode: " + split_user[4] + "\nCity: " + split_user[5] + "\nEmailaddress: " + split_user[6] + "\nUsername: " + split_user[7] + "\nTelephonenumber: " + split_user[9])
                    break

            if not isfound:
                print("\nNo member found")    

    #Delete member
    def deletemember(self):
        with open("data/members.csv", "r") as f:
            csvdata = list(csv.reader(f))

        running = True
        while running:
            user_found = False
            username = input("Please enter the username of the member you want to delete: ").lower()
            
            with open("data/members.csv", "w", newline='') as f:
                writer = csv.writer(f)
                index = 0
                for user in csvdata:
                    thisuser = user[0].split(';')
                    if username == thisuser[7].lower():
                        print("\nUser found! Deleting...\n")
                        user_found = True
                    elif username != thisuser[7].lower():
                        if index == 0:
                            writer.writerow(user)
                            index += 1
                        else:
                            new_index = thisuser
                            new_index[0] = str(index)
                            joined_new_index = ';'.join(new_index)
                            final_new_index = [joined_new_index]
                            writer.writerow(final_new_index)
                            index += 1

            if user_found == True:
                running = False
    
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
            
            with open("data/members.csv", "w", newline='') as f:
                writer = csv.writer(f)
                for user in csvdata:
                    thisuser = user[0].split(';')
                    if username != thisuser[7].lower():
                        writer.writerow(user)
                    if username == thisuser[7].lower():
                        print("User found!")
                        new_value = input("What new value do you want to insert?")

                        found_user = thisuser
                        found_user[int(check)] = new_value
                        joined_user = ";".join(found_user)
                        final_user = [joined_user]
                        writer.writerow(final_user)
                        exists = True
            if exists:
                print("\nSuccefully updated member ", username, "!\n")
                active = False
            else:
                print("\nMember not found\n")
                print("\nPlease enter an existing member\n")

    #add list of members
    def addListOfMembers(self):
        filename = input("\nPlease enter the name of the file you want to add(for example: 'addmembers.csv'):")
        filepath = self.findfile(filename, "/")
        with open(filepath, "r") as f:
            csvdata = list(csv.reader(f))
        with open("data/members.csv", "r") as f:
            csvdata2 = list(csv.reader(f))
            index = len(csvdata2)
        with open("data/members.csv", "a", newline='') as f:
            writer = csv.writer(f)
            for idx, user in enumerate(csvdata):
                if idx != 0:
                    splituser = user[0].split(';')
                    splituser[0] = str(index)
                    joineduser = ";".join(splituser)
                    finaluser = [joineduser]
                    writer.writerow(finaluser)
                    index += 1
                
                
        print("\nThe file has been added to the database.")
    
    def findfile(self, name, path):
        global filepath
        print("\nSearching for file...")
        for dirpath, dirnames, filename in os.walk(path):
            if name in filename:
                print("\nFile found!")
                filepath = os.path.join(dirpath, name)
                return filepath
        return "newmembers"

        # listofmembers = list(input(f"\nFill in the list of members you want to add:\n"))
        # print(len(listofmembers))
        # with open("data/members.csv", "a") as f:
        #     writer = csv.writer(f)
        #     for i in range(len(listofmembers)):
        #         addmem = []
        #         j = 0
        #         for j in range(0, 10):
        #             #print(i + j)
        #             addmem.append(listofmembers[i+j])
        #         writer.writerow(addmem)
        #         i+= 9
        # print("\nList of members added.")
        # return