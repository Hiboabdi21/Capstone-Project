import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def getEmail():
    print("Enter You email")
    email = input()
    if  (re.fullmatch(regex, email)):
        return email
    else:
       return "Invalid Email"

def getPassword():
    print("Enter password(password must be greater than 7 characters)")
    password = input()
    if len(password) > 7:
        return password
    else:
       return "Invalid Password"

def addnewUser():
    email = getEmail()
    if email == "Invalid Email":
        while email == "Invalid Email":
              email = getEmail()

    password = getPassword()
    if password == "Invalid Password":
        while password == "Invalid Password":
            password = getPassword()

    print(email)
    print(password)

def userInput():
    print("1. Add new user")
    print("2. See all current users")
    print("3. Remove existing user")
    print("4. Change password for a particular user")
    print("Choose between 1-4")
    userSelectedNumber = int(input())
    if userSelectedNumber not in [1,2,3,4]:
        print("Please select only from 1-4")
        userInput()
    elif userSelectedNumber == 1:
        addnewUser()

if __name__ == "__main__":
       userInput()