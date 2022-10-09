import csv
import uuid
from helper_fuctions.user_details import get_userID_by_username, get_username_by_userID
# Import date class from datetime module
from datetime import date


def save_sickness_detail():
    sickness_data = [[]]

    # name of csv file
    filename = "dataset/sickness_details.csv"

    # writing to csv file
    with open(filename, 'a', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        sickness_data[0].append(uuid.uuid4())

        valid_doctor_name = False
        while not valid_doctor_name:

            doctor_name = input("Enter the doctor's Name : ")

            if doctor_name == "e":
                return

            doctor_ID = get_userID_by_username(doctor_name, 'dataset/user.csv')
            if doctor_ID:
                valid_doctor_name = True
                sickness_data[0].append(doctor_ID)
            else:
                print('not valid name')

        valid_patient_name = False
        while not valid_patient_name:

            patient_name = input("Enter the patient's Name : ")

            if patient_name == "e":
                return

            patient_ID = get_userID_by_username(patient_name, 'dataset/user.csv')
            if patient_ID:
                valid_patient_name = True
                sickness_data[0].append(patient_ID)
            else:
                print('not valid name')

        sickness = input("Enter the sickness : ")
        sickness_data[0].append(sickness)

        # Returns the current local date
        today = date.today()
        sickness_data[0].append(today)

        #description
        sickness = input("Enter the description : ")
        sickness_data[0].append(sickness)

        # writing the data rows
        csvwriter.writerows(sickness_data)

        print("successfully save sickness data!!!")


def get_sickness_detail(patient_id='', doctor_id=''):
    sickness_data=[]

    if patient_id == '':
        valid_patient_name = False
        while not valid_patient_name:

            patient_name = input("Enter the patient's Name : ")

            if patient_name == "e":
                return

            patient_ID = get_userID_by_username(patient_name, 'dataset/user.csv')
            if patient_ID:
                patient_id = patient_ID
                valid_patient_name = True
            else:
                print('not valid name')

    if doctor_id == '':
        valid_doctor_name = False
        while not valid_doctor_name:

            doctor_name = input("Enter the doctor's Name : ")

            if doctor_name == "e":
                return

            doctor_ID = get_userID_by_username(doctor_name, 'dataset/user.csv')
            if doctor_ID:
                doctor_id = doctor_ID
                valid_doctor_name = True

            else:
                print('not valid name')

    with open('dataset/sickness_details.csv', mode='r') as file:
        csvFile = csv.reader(file)
        for data in csvFile:

            # if user == fields:
            # pass

            if data[2] == patient_id and data[1] == doctor_id:
                print(data)
                sickness_data.append(data)

        else:
            if len(sickness_data) < 1:
                print("not found")
                return False
            else:
                return sickness_data
# save_sickness_detail()
