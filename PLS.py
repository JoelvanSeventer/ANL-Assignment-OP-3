from roles import Librarian, Subscriber, Publisher
class PublicLibrary():
    def __init__(self, role):
        self.role = role
        if role == "1":
            obj = Librarian()
            obj.run()
        elif role == "2":
            Subscriber().run()
        elif role == "3":
            Publisher().run()
        else:
            print("Please select an available role!")
            main()
    

def main():
    role = input("\nPlease select your role:\n1. Librarian\n2. Subscriber\n3. Publisher\n").lower()
    PublicLibrary(role)
main()