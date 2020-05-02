from src.authentication.login import Login
from src.users.admin import Admin
from src.users.receptionist import Receptionist
from src.users.doctor import Doctor
from src.users.patient import Patient
from src.shared.edit_account import *
from src.shared.check_patient_id import check_patient_id


def main():

    current_user = Login().auth_user()
    if current_user:
        current_user_id = str(current_user.get('id'))

        # user is admin
        if current_user.get('privilege_level') == '1':
            Admin().set_codes()

        # user is a receptionist
        elif current_user.get('privilege_level') == '3':

            print("Press 1 to create patient account\nPress 2 to edit personal account\nPress 3 to view personal account\nPress 4 to set new password\nPress -1 to exit\n ")
            while True:
                option = input()
                if option == '1':
                    Receptionist().create_patient_account()
                    print("Press next number: ")
                elif option == '2':
                    edit_account(current_user_id)
                    print("Press next number: ")
                elif option == '3':
                    view_account(current_user_id)
                    print("Press next number: ")
                elif option == '4':
                    renew_password(current_user_id)
                    print("Press next number: ")
                elif option == '-1':
                    print("Thank you receptionist")
                    break
                else:
                    print("Invalid input. Try again")

        # user is a doctor
        if current_user.get('privilege_level') == '2':
            print("Press 1 to add sickness details \nPress 2 to add drug prescription \nPress 3 to add lab test prescription \nPress 4 to view sickness details \nPress 5 to view previous drug prescriptions \nPress 6 to view lab test prescription \nPress 7 to edit account \nPress 8 to renew password \nPress 9 to view account\nPress -1 to exit\n ")

            while True:
                option = input()
                if option in ['1', '2', '3', '4', '5', '6']:

                    while True:
                        patient_id = input("Enter patient id: ")
                        if check_patient_id(patient_id):
                            break
                        else:
                            print("Invalid patient id")

                    if option == '1':
                        Doctor().add_sickness_details(patient_id)
                        print("Press next number: ")
                    elif option == '2':
                        Doctor().add_drug_prescription(patient_id)
                        print("Press next number: ")
                    elif option == '3':
                        Doctor().add_labtest_prescription(patient_id)
                        print("Press next number: ")
                    elif option == '4':
                        Doctor().read_sickness_details(patient_id)
                        print("Press next number: ")
                    elif option == '5':
                        Doctor().read_drug_prescription(patient_id)
                        print("Press next number: ")
                    elif option == '6':
                        Doctor().read_labtest_prescription(patient_id)
                        print("Press next number: ")
                elif option == '7':
                    edit_account(current_user_id)
                    print("Press next number: ")
                elif option == '8':
                    renew_password(current_user_id)
                    print("Press next number: ")
                elif option == '9':
                    view_account(current_user_id)
                    print("Press next number: ")
                elif option == '-1':
                    print("Thank you doctor")
                    break
                else:
                    print("Invalid input. Try again")

        # user is a patient
        if current_user.get('privilege_level') == '4':
            print("Press 1 to change password \nPress 2 to update account \nPress 3 to view account details\nPress 4 to view sickness details \nPress 5 to view previous drug prescriptions \nPress 6 to view lab test prescription \nPress -1 to exit\n ")
            while True:
                option = input()
                if option == '1':
                    renew_password(current_user_id)
                    print("Press next number: ")
                elif option == '2':
                    edit_account(current_user_id)
                    print("Press next number: ")
                elif option == '3':
                    view_account(current_user_id)
                    print("Press next number: ")
                elif option == '4':
                    Patient().read_sickness_details(current_user_id)
                    print("Press next number: ")
                elif option == '5':
                    Patient().read_drug_prescription(current_user_id)
                    print("Press next number: ")
                elif option == '6':
                    Patient().read_labtest_prescription(current_user_id)
                    print("Press next number: ")
                elif option == '-1':
                    print("Thank you")
                    break
                else:
                    print("Invalid input. Try again")






