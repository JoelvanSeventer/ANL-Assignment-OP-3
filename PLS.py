from roles import Librarian, Subscriber, Publisher
class PublicLibrary():
    def __init__(self, role):
        self.role = role
        if role == "librarian":
            obj = Librarian()
            obj.run()
        elif role == "subscriber":
            Subscriber().run()
        elif role == "publisher":
            Publisher().run()
        else:
            print("Please select an available role!")
            main()
    

def main():
    role = input("\nAre you a Librarian, Subscriber or Publisher?\n\nEnter a role: ").lower()
    PublicLibrary(role)
main()