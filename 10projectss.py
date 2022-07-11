

def resgister():
    db = open("readme.txt", "r")
    username = input("Enter Username: ")
    Password = input("Enter Password: ")
    Password1 = input("Please Confirm Password: ")
    d = []
    f = []
    #To see the username and passwords
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a) # seperates the usernames and passwords
        f.append(b)
    data = dict(zip(d, f))
    print(data)
    # Checks prints the login info
    if Password != Password1:
        print("Passwords don't match. Please Try again.")
        resgister()
    else:
        if len(Password) <= 6:
           print("Password is too short")
           resgister()
        elif username in d:
            print("Username exist")
            resgister()
        else:
            db = open('readme.txt', 'a')
            db.write(username + ", " + Password + "\n")
            print("Success")
            #If their problem with resgister or it will be success
#resgister()

def Sign_in():
    DB = open('readme.txt', 'r')
    Username = input("Enter Username here: ")
    Password = input("Enter Password here: ")
    d = []
    f = []

    for i in DB:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    print(data)


Sign_in()
def access():
    pass
