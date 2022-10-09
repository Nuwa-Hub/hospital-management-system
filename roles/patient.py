from controllers.drug_prescription import get_drug_prescription
from controllers.sickness_details import get_sickness_detail
from controllers.test_prescriptions import get_test_prescription
from controllers.user_profile import update_profile


def patientHandler(currentuser_id):
    while True:
        print(
            'Get drug prescription => press gdp \n'
            'Get lab test prescription => press glp \n'
            'Get sickness details => press gsd \n')
        userinput = input("Enter your choice : ")
        if userinput == 'gsd':
            get_sickness_detail(patient_id=currentuser_id)
        elif userinput == 'gdp':
            get_drug_prescription(patient_id=currentuser_id)
        elif userinput == 'glp':
            get_test_prescription(patient_id=currentuser_id)

        elif userinput == "e":
            exit()
        else:
            print("wrong input!!")

# doctorHandler()
