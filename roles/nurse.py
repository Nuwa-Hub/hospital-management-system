from controllers.drug_prescription import save_drug_prescription, get_drug_prescription
from controllers.sickness_details import save_sickness_detail, get_sickness_detail
from controllers.test_prescriptions import save_test_prescription, get_test_prescription
from controllers.user_profile import update_profile

def nurseHandler(currentuser_id):
    while True:
        print(
              'Add sickness details => press asd \n'
              'Get drug prescription => press gdp \n'
              'Get lab test prescription => press glp \n'
              'Get sickness details => press gsd \n'
              'Update user details => press upd \n')

        userinput = input("Enter your choice : ")

        if userinput == 'asd':
            save_sickness_detail()
        elif userinput == 'gdp':
            get_drug_prescription(doctor_id=currentuser_id)
        elif userinput == 'glp':
            get_test_prescription(doctor_id=currentuser_id)
        elif userinput == 'gsd':
            get_sickness_detail(doctor_id=currentuser_id)
        elif userinput == 'upd':
            update_profile(user_id=currentuser_id)
        elif userinput == "e":
            exit()
        else: print("wrong input!!")