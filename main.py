# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from controllers.register_login import register, login
from roles.doctor import doctorHandler
from roles.employee import employeeHandler
from roles.labAssistante import labAssistantHandler
from roles.nurse import nurseHandler
from roles.patient import patientHandler

currentUser = False


def start():
    while True:
        startup = input("For Register 'Press r' For Login 'Press l' : ")
        if startup == "r":
            register()
        if startup == "l":
            userdata = login()
            if userdata:
                currentUser= userdata[1]
                if userdata[0] == "1":
                    print('welcome doctor!!!')
                    doctorHandler(currentUser)
                elif userdata[0] == "2":
                    print('welcome employee!!')
                    employeeHandler(currentUser)
                elif userdata[0] == "3":
                    print('welcome patient!!')
                    patientHandler(currentUser)
                elif userdata[0] == "4":
                    print('welcome nurse!!')
                    nurseHandler(currentUser)
                elif userdata[0] == "5":
                    print('welcome lab assistant!!')
                    labAssistantHandler(currentUser)
        if startup == "e":
            exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
