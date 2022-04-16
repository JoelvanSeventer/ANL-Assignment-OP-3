from roles import Librarian, Subscriber, Publisher

# main asks for the role
def main():
    un = input("\nPlease enter your username: ")
    pw = input("\nPlease enter your password: ")
    csvdata = open('data/customers.csv', 'r')
    for user in csvdata:
        thisuser = user.split(';')
        if(un == "admin" and pw == "admin123"):
            welcome()
            print("\nWelcome admin!\n")
            Librarian().run()
            break
        elif un == thisuser[7] and pw == thisuser[8]:
            welcome()
            print("\nWelcome " + un + "!\n")
            Subscriber().run()
            break
        
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