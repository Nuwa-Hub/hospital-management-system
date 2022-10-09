import csv
import re
# working of MD5 (byte - byte)
import hashlib
import uuid

from helper_fuctions.user_details import check_duplicate_usernames, check_duplicate_NIC

fields = ['username', 'password', 'type']


def register():
    # data rows of csv file
    userData = [[]]

    # name of csv file
    filename = "dataset/user.csv"

    # writing to csv file
    with open(filename, 'a', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # get username
        valid_username = False
        while not valid_username:

            username = input("Please Enter Your Username : ")

            if username == "e":
                return

                # pattern is a string containing the regex pattern
            usernamePat = r"[0-9a-z]{3,15}"

            # Checks whether the whole string matches the re.pattern or not
            if re.fullmatch(usernamePat, username) and check_duplicate_usernames(username):

                userData[0].append(username)
                valid_username = True
            else:
                print("Username should be 5 characters or shouldn't be reused!")

        # get password
        valid_password = False
        while not valid_password:

            password = input("Please Enter Your Password : ")

            if password == "e":
                return

                # pattern is a string containing the regex pattern
            passwordPat = r"[0-9a-z]{10,15}"

            # Checks whether the whole string matches the re.pattern or not
            if re.fullmatch(passwordPat, password):
                # password hash
                hashedPassword = hashlib.md5(password.encode())
                userData[0].append(hashedPassword.hexdigest())

                valid_password = True
            else:
                print("Password should be at least 10 characters!")

        # get username
        valid_type = False
        while not valid_type:

            type = input("Please Enter Your Type : ")

            if type == "e":
                exit()

            # pattern is a string containing the regex pattern
            types = ["1", "2", "3","4","5"]

            # Checks whether the whole string matches the re.pattern or not
            if type in types:
                userData[0].append(type)
                valid_type = True
            else:
                print("Type should be valid!")
        # print(userData)

        # writing the fields
        # csvwriter.writerows(fields)

        # create id
        userData[0].append(uuid.uuid4())

        # get fullname
        fullName = input("Enter your Full Name : ")
        userData[0].append(fullName)

        # get address
        address = input("Enter your address : ")
        userData[0].append(address)

        # get NIC
        valid_NIC = False
        while not valid_NIC:

            nic = input("Please Enter Your NIC : ")

            if type == "e":
                return

                # Checks whether the whole string matches the re.pattern or not
            if check_duplicate_NIC(nic):
                userData[0].append(nic)
                valid_NIC = True
            else:
                print("NIC can't be reused!!!")

        # writing the data rows
        csvwriter.writerows(userData)
        print("successfully registered!!!")


def login():
    with open('dataset/user.csv', mode='r') as file:
        csvFile = csv.reader(file)

        # get username and password
        username = input("Please Enter your Username : ")
        password = input("Please Enter your Password : ")
        # password hash
        hashedPassword = hashlib.md5(password.encode())

        for user in csvFile:

            if user == fields:
                pass

            if user[0] == username and user[1] == hashedPassword.hexdigest():
                print("login success!!!")
                return [user[2], user[3]]
        else:
            print("login failed")
            return False

# register()
# login()
