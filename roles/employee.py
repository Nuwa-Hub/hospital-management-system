from controllers.drug_prescription import save_drug_prescription, get_drug_prescription
from controllers.sickness_details import save_sickness_detail, get_sickness_detail
from controllers.test_prescriptions import save_test_prescription, get_test_prescription
from helper_fuctions.user_details import getall_patient_details
from controllers.user_profile import update_profile

def employeeHandler(currentuser_id):
    while True:
        print('Get patients details => press gpd \n'
              'Get drug prescription => press gdp \n'
              'Get lab test prescription => press glp \n'
              'Get sickness details => press gsd \n'
              'Update user details => press upd \n')
        userinput = input("Enter your choice : ")
        if userinput == 'gpd':
            getall_patient_details('dataset/user.csv')
        elif userinput == 'gsd':
            get_sickness_detail()
        elif userinput == 'gdp':
            get_drug_prescription()
        elif userinput == 'glp':
            get_test_prescription()
        elif userinput == 'upd':
            update_profile(user_id=currentuser_id)
        elif userinput == "e":
            exit()
        else:
            print("wrong input!!")


#employeeHandler()
