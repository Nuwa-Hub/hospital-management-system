import csv
import uuid
from helper_fuctions.user_details import get_userID_by_username
# Import date class from datetime module
from datetime import date


def save_drug_prescription():
    drug_prescription_data = [[]]

    # name of csv file
    filename = "dataset/drug_prescriptions.csv"

    # writing to csv file
    with open(filename, 'a', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        drug_prescription_data[0].append(uuid.uuid4())

        valid_doctor_name = False
        while not valid_doctor_name:

            doctor_name = input("Enter the doctor's Name : ")

            if doctor_name == "e":
                exit()

            doctor_ID = get_userID_by_username(doctor_name, 'dataset/user.csv')
            if doctor_ID:
                valid_doctor_name = True
                drug_prescription_data[0].append(doctor_ID)

        valid_patient_name = False
        while not valid_patient_name:

            patient_name = input("Enter the patient's Name : ")

            if patient_name == "e":
                exit()

            patient_ID = get_userID_by_username(patient_name, 'dataset/user.csv')
            if patient_ID:
                valid_patient_name = True
                drug_prescription_data[0].append(patient_ID)

        prescription = input("Enter the prescriptions : ")

        if prescription == "e":
            exit()
        drug_prescription_data[0].append(prescription)

        dose = input("Enter the dose : ")

        if dose == "e":
            exit()

        drug_prescription_data[0].append(dose)

        dose_period = input("Enter the dose period : ")

        if dose_period == "e":
            exit()

        drug_prescription_data[0].append(dose_period)

        # Returns the current local date
        today = date.today()
        drug_prescription_data[0].append(today)

        # writing the data rows
        csvwriter.writerows(drug_prescription_data)

        print("successfully save drug prescription data!!!")


def get_drug_prescription(patient_id='', doctor_id=''):
    drug_data = []

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

    with open('dataset/drug_prescriptions.csv', mode='r') as file:
        csvFile = csv.reader(file)
        for data in csvFile:

            # if user == fields:
            # pass

            if data[2] == patient_id and data[1] == doctor_id:
                print(data)
                drug_data.append(data)

        else:
            if len(drug_data) < 1:
                print("not found")
                return False
            else:
                return drug_data

# save_drug_prescription()
