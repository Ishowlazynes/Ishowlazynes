def Resgister():
    Info = open('readme.txt', 'r')
    username = input("Enter Username: ")
    Password = input("Enter Password: ")
    Password1 = input("Please Confirm Password: ")

    if Password != Password1:
        print("Passwords don't match. Please Try again.")
        Resgister()

Resgister()
