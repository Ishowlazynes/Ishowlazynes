

def everything():  
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
                Sign_in()
                #If their problem with resgister or it will be success


    def Sign_in():
        DB = open('readme.txt', 'r')
        Username = input("Enter Username here: ")
        Password = input("Enter Password here: ")
        Attempts = 0
        if len(Username or Password)>1:
            d = []
            f = []
            for i in DB:
                a,b = i.split(", ")
                b = b.strip()
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))
            try:
                if data[Username]:
                    try:
                        if Password == data[Username]:
                            print("Confirmed")
                            print("HI", Username)
                        else:
                            print("Password or Username wrong")
                            Attempts+=1
                            Sign_in()
                    except:
                        print("Incorrect password or Username")
                else:
                    print("Username doesn't exist")
                    Attempts +=1
            except:
                print("Login error")
            if Attempts == 3:
                print("Try Again later.")
    g = int(input("Do want to resgister or login in? 1 for resgister or 0 for login in:  "))
    if g == 1:
        resgister()
    elif g == 0:
       Sign_in()
    else:
        print("Try again")
        everything()
                    
everything()

        


def access():
    pass
