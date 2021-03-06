import csv
import re


adminPassword = "admin786"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def readAllUsers():
    with open("users.csv", mode="r", newline="") as f:
     reader = csv.reader(f,delimiter=",")
     print("Current Users ")
     for row in reader:
         print(row[0])

def changePassword():
    userToChangePassowrd = input("Enter email of user to change password ")
    alluserEmails = getallEmails()

    if userToChangePassowrd not in alluserEmails:
        print("This User not exist")
    else:

        newPassword = getPassword()
        if newPassword == "Invalid Password":
            while newPassword == "Invalid Password":
                print("Invalid Password")
                newPassword = getPassword()

        allUsersList = []
        with open("users.csv", mode="r", newline="") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                allUsersList.append(row)

        for user in allUsersList:
            if userToChangePassowrd == user[0]:
                user[1] = newPassword
                print("Password changed successfully ")

        with open("users.csv", mode="w", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            for user in allUsersList:
                writer.writerow([user[0], user[1]])


def getallEmails():
    userEmails = []
    with open("users.csv", mode="r", newline="") as f:
     reader = csv.reader(f,delimiter=",")
     for row in reader:
         userEmails.append(row[0])
    return userEmails

def removeUsers():
    userAdminPassword = input("Please give admin password to remove a user ")
    if userAdminPassword != adminPassword:
        print("Wrong Password")
    else:
        print("Access Granted")
        userToRemove = input("Enter email of user to remove ")
        alluserEmails = getallEmails()

        if userToRemove not in alluserEmails:
            print("User Not exist")
        else:
            allUsersList =[]
            with open("users.csv", mode="r", newline="") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    allUsersList.append(row)

            for user in allUsersList:
              if userToRemove == user[0]:
                  allUsersList.remove(user)
                  print("User Removed Successfully")

            with open("users.csv", mode="w", newline="") as f:
              writer = csv.writer(f, delimiter=",")
              for user in allUsersList:
                  writer.writerow([user[0],user[1]])


def getEmail(email):
    if  (re.fullmatch(regex, email)):
        return email
    else:
       return "Invalid Email"

def getPassword(password):
    if len(password) > 7:
        return password
    else:
       return "Invalid Password"

def addnewUser():
    print("Enter Your email")
    email = input()
    email = getEmail(email)
    if email in getallEmails():
        print("User with same email already exists")

    else:
        if email == "Invalid Email":
            while email == "Invalid Email":
                print("Invalid Email")
                print("Enter Your email")
                email = input()
                email = getEmail(email)

        print("Enter password(password must be greater than 7 characters)")
        password = input()
        password = getPassword(password)
        if password == "Invalid Password":
            while password == "Invalid Password":
                print("Invalid Password")
                print("Enter password(password must be greater than 7 characters)")
                password = input()
                password = getPassword(password)

        with open ("users.csv", mode="a", newline="") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([email,password])

        print("User Added Successfully")

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
    elif userSelectedNumber == 2:
        readAllUsers()
    elif userSelectedNumber == 3:
        removeUsers()
    elif userSelectedNumber == 4:
        changePassword()

def main():
    userInput()

if __name__ == "__main__":
        main()