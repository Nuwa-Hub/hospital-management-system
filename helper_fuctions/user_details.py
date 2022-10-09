import csv

user_fields = ['username', 'password', 'type', 'user_ID', 'fullname', 'address', 'NIC']


def get_userID_by_username(username,file_path):
    with open(file_path, mode='r') as file:
        csvFile = csv.reader(file)

        for user in csvFile:

            if user == user_fields:
                pass

            if user[0] == username:
                return user[3]
        else:return False


# check duplicate usernames
def check_duplicate_usernames(username):
    with open('dataset/user.csv', mode='r') as file:
        csvFile = csv.reader(file)

        for user in csvFile:

            if user == user_fields:
                pass

            if user[0] == username:
                return False
        else:
            return True

# check duplicate usernames
def check_duplicate_NIC(nic):
    with open('dataset/user.csv', mode='r') as file:
        csvFile = csv.reader(file)

        for user in csvFile:

            if user == user_fields:
                pass

            if user[6] == nic:
                return False
        else:
            return True

def get_username_by_userID(userID,file_path):
    with open(file_path, mode='r') as file:
        csvFile = csv.reader(file)

        for user in csvFile:

            if user == user_fields:
                pass

            if user[3] == userID:
                return user[0]
        else:return False

def getall_patient_details(file_path):

    with open(file_path, mode='r') as file:
        csvFile = csv.reader(file)

        for user in csvFile:
            if user=="['username', 'password', 'type', 'user_ID']":
                pass
            if user[2]=='3':
               print(user[2:])
        else:
            print('successfully get users!!!!')
            return True
#print(get_userID_by_username("nuwan"))
