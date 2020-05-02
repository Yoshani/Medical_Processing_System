from src.shared.hash import *
import json


class Admin:

    def set_codes(self):
        doctor, receptionist = '', ''
        print("Press 1 to edit doctor code\nPress 2 to edit receptionist code\nPress 3 to create admin account\nPress -1 to exit\n")
        while True:
            role_number = input()
            if role_number == '1':
                doctor = hash_password(input("Enter new doctor code: "))
                print("Press next number: ")
            elif role_number == '2':
                receptionist = hash_password(input("Enter new receptionist code: "))
                print("Press next number: ")
            elif role_number == '3':
                self.create_admin()
                print("Press next number: ")
            elif role_number == '-1':
                print("Thank you admin")
                break
            else:
                print("Invalid input")

        with open("config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            doc_code = data['codes'].get('doctor')
            rec_code = data['codes'].get('receptionist')
            if doctor:
                doc_code = doctor
            if receptionist:
                rec_code = receptionist
            data['codes'] = {
                'doctor': doc_code,
                'receptionist': rec_code,
            }

        with open("config.json", 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def create_admin():
        name = input('Admin username: ')
        temp_password = hash_password(input('Temporary password: '))

        # read and write user to config file
        with open("config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            admin_id = len(data['users'])+1
            data['users'].append({
                'id': admin_id,
                'name': name,
                'password': temp_password,
                'user_type': "admin",
                'privilege_level': '1'
            })
        with open("config.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Account created successfully")
        print("Please enter personal details of admin")

        admin_name = input('Admin name: ')
        age = input('Age: ')
        nic_no = input('NIC number: ')
        tel = input('Telephone number: ')

        # read and write admin details to data file
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['personal_details'].append({
                'id': admin_id,
                'name': admin_name,
                'age': age,
                'nic_no': encode(nic_no),
                'tel': encode(tel)
            })
        with open("data.json", 'w') as outfile:
            json.dump(data, outfile)




