from getpass import getpass

print("Hello, You are entering C4E Admin Console")

username = input("Username: ")

if username != "C4E":
    print("You are not authorized. This session will end.")

else:
    password = getpass("Password: ")
    if password != "codethechange":
        print("Incorrect Password")
    else:
        print("Welcome to C4E Admin Console")

print("Powered by Techkids")
