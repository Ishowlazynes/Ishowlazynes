import random
import string # will get all the string stuff

characters = list(string.ascii_letters + string.digits + "`~!@#$%^&*()_")
# will make list of the letters, digits, and symbols

def passwordGenerator():
    length = int(input("How long do you want your password: "))
    #length of the password

    random.shuffle(characters)# shuffle

    password = []
    #the password

    for i in range(length):
        #it add the characters that are in length
        password.append(random.choice(characters))
    #then it shuffle again
    random.shuffle(password)
    #print the password
    print("".join(password))
passwordGenerator()