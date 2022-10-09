import csv
import re
# working of MD5 (byte - byte)
import hashlib
import uuid

from helper_fuctions.user_details import check_duplicate_usernames, check_duplicate_NIC

fields = ['username', 'password', 'type']


def update_profile(user_id):
    # name of csv file
    filename = "dataset/user.csv"

    history = []

    with open(filename, mode='r') as file:
        csvFile = csv.reader(file)

        for user in csvFile:
            history.append(user)
    print(history)
    file.close()

    # data rows of csv file
    userData = []

    # writing to csv file
    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        user_id=input("Please Enter Your New Username : ")
        # get username
        valid_username = False
        while not valid_username:

            username = input("Please Enter Your New Username : ")

            if username == "e":
                return

                # pattern is a string containing the regex pattern
            usernamePat = r"[0-9a-z]{3,5}"

            # Checks whether the whole string matches the re.pattern or not
            if re.fullmatch(usernamePat, username) and check_duplicate_usernames(username):

                userData.append(username)
                valid_username = True
            else:
                print("Username should be 5 characters or shouldn't be reused!")

        # get password
        valid_password = False
        while not valid_password:

            password = input("Please Enter New Your Password : ")

            if password == "e":
                return

                # pattern is a string containing the regex pattern
            passwordPat = r"[0-9a-z]{3,5}"

            # Checks whether the whole string matches the re.pattern or not
            if re.fullmatch(passwordPat, password):
                # password hash
                hashedPassword = hashlib.md5(password.encode())
                userData.append(hashedPassword.hexdigest())

                valid_password = True
            else:
                print("Password should be 5 characters!")

        newdata=[]
        #modify data
        for user in history:
            if user[3]==user_id:
                newuser=userData+user[2:]
                newdata.append(newuser)
            else:newdata.append(user)
        # writing the data rows
        csvwriter.writerows(newdata)
        print("successfully updated!!!")
