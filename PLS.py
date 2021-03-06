from roles import LibraryAdmin, Member

# main asks for the role
def main():
    loggedin = False
    un = input("\nPlease enter your username: ")
    pw = input("\nPlease enter your password: ")
    

    if(un == "admin" and pw == "admin123"):
        loggedin = True
        welcome()
        print("\nWelcome admin!\n")
        LibraryAdmin().run()

    csvdata = open('data/members.csv', 'r')

    for user in csvdata:
        thisuser = user.split(';')
        if un == thisuser[7] and pw == thisuser[8]:
            loggedin = True
            welcome()
            print("\nWelcome " + un + "!\n")
            Member().run(un)
            break
    if loggedin == False:
        print("\nWrong username or password!\n")
        main()

def welcome():
    print("-----------------------------")
    print("------ Welcome to our -------")
    print("------ Public Library -------")
    print("-----------------------------\n")
    print("Welcome to our public library!\nHopefully you can find everything you're looking for!\n")

# call main
main()