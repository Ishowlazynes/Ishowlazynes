

def Resgister():
    Info = open('readme.txt', 'r')
    username = input("Enter Username: ")
    Password = input("Enter Password: ")
    Password1 = input("Please Confirm Password: ")

    if Password != Password1:
        print("Passwords don't match. Please Try again.")
        Resgister()
    else:
        if len(Password) <= 6:
            print("Password is too short")
            Resgister()
        elif username in Info:
            print("Username exist")
            Resgister()
        else:
            Info = open('readme.txt', 'a')
            Info.writelines(username + ", " + Password + "\n")
            print("Success")



Resgister()

def login():
    Login_Info = open('readme.txt', 'r')
    username = input("Enter your Username: ")
    password = input("Enter your password: ")
    Login_Info.readline()
def access():
    pass
