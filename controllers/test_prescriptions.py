import csv
import uuid
from helper_fuctions.user_details import get_userID_by_username
# Import date class from datetime module
from datetime import date


def save_test_prescription():
    test_prescription_data = [[]]

    # name of csv file
    filename = "dataset/test_prescriptions.csv"

    # writing to csv file
    with open(filename, 'a', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        test_prescription_data[0].append(uuid.uuid4())

        valid_doctor_name = False
        while not valid_doctor_name:

            doctor_name = input("Enter the labassistant's Name : ")

            if doctor_name == "e":
                return

            doctor_ID = get_userID_by_username(doctor_name, 'dataset/user.csv')
            if doctor_ID:
                valid_doctor_name = True
                test_prescription_data[0].append(doctor_ID)

        valid_patient_name = False
        while not valid_patient_name:

            patient_name = input("Enter the patient's Name : ")

            if patient_name == "e":
                return

            patient_ID = get_userID_by_username(patient_name, 'dataset/user.csv')
            if patient_ID:
                valid_patient_name = True
                test_prescription_data[0].append(patient_ID)

        prescription = input("Enter the prescriptions : ")
        test_prescription_data[0].append(prescription)
        dose = input("Enter the dose : ")
        test_prescription_data[0].append(dose)
        dose_period = input("Enter the dose period : ")
        test_prescription_data[0].append(dose_period)


        # Returns the current local date
        today = date.today()
        test_prescription_data[0].append(today)

        description = input("Enter the dose description : ")
        test_prescription_data[0].append(description)

        lab_type = input("Enter the dose Lab Type : ")
        test_prescription_data[0].append(lab_type)
        # writing the data rows
        csvwriter.writerows(test_prescription_data)

        print("successfully save test prescription data!!!")


def get_test_prescription(patient_id='', doctor_id=''):
    test_data = []

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

    with open('dataset/test_prescriptions.csv', mode='r') as file:
        csvFile = csv.reader(file)
        for data in csvFile:

            # if user == fields:
            # pass

            if data[2] == patient_id:
                print(data)
                test_data.append(data)

        else:
            if len(test_data) < 1:
                print("not found")
                return False
            else:
                return test_data

# save_test_prescription()
