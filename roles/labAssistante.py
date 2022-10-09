from controllers.drug_prescription import save_drug_prescription, get_drug_prescription
from controllers.sickness_details import save_sickness_detail, get_sickness_detail
from controllers.test_prescriptions import save_test_prescription, get_test_prescription
from controllers.user_profile import update_profile

def labAssistantHandler(currentuser_id):
    while True:
        print(
              'Add lab test prescription => press alp \n'
        
            
              'Get lab test prescription => press glp \n'
           
              'Update user details => press upd \n')

        userinput = input("Enter your choice : ")
        if userinput == 'alp':
            save_test_prescription()
        elif userinput == 'glp':
            get_test_prescription(doctor_id=currentuser_id)
        elif userinput == 'upd':
            update_profile(user_id=currentuser_id)
        elif userinput == "e":
            exit()
        else: print("wrong input!!")