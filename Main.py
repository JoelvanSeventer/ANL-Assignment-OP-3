from roles import Librarian, Subscriber, Publisher

#met input van main naar de ingevulde role
class PublicLibrary():

    def __init__(self, role):
        #set field
        self.role = role

        #check input
        if role == "1":
            Librarian().run()

        elif role == "2":
            Subscriber().run()

        elif role == "3":
            Publisher().run()

        else: #bij verkeerde input
            print("Please enter a valid number!\n\n")
            main()
    
# main vraagt om de role
def main():
    print("-----------------------------")
    print("------ Welcome to our -------")
    print("------ Public Library -------")
    print("-----------------------------\n")
    print("Welcome to our public library!\nHopefully you can find everything you're looking for!\n")
    role = input("Please select your role by typing one of the following numbers:\n1. Librarian\n2. Subscriber\n3. Publisher\n").lower()
    
    PublicLibrary(role)

# call main
main()