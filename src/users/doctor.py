import json
from datetime import datetime


class Doctor:

    @staticmethod
    def add_sickness_details(patient_id):

        sickness_details = input("Enter sickness details: \n")

        # write sickness details to data file
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['sickness_details'].append({
                'id': patient_id,
                'sickness': sickness_details,
                'date': str(datetime.now())[0:19],
            })
        with open("data.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Sickness details added")

    @staticmethod
    def add_drug_prescription(patient_id):

        drug_prescription = input("Enter drug prescription: \n")

        # write drug prescription to data file
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['drug_presc'].append({
                'id': patient_id,
                'drug_presc': drug_prescription,
                'date': str(datetime.now())[0:19],
            })
        with open("data.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Drug prescription details added")

    @staticmethod
    def add_labtest_prescription(patient_id):

        labtest_prescription = input("Enter lab test prescription: \n")

        # write lab test prescription to data file
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['labtest_presc'].append({
                'id': patient_id,
                'labtest_presc': labtest_prescription,
                'date': str(datetime.now())[0:19],
            })
        with open("data.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Lab test prescription details added")

    @staticmethod
    def read_sickness_details(patient_id):

        # read sickness details from data file
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['sickness_details']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['sickness'])

    @staticmethod
    def read_drug_prescription(patient_id):

        # read drug prescription from data file
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['drug_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['drug_presc'])

    @staticmethod
    def read_labtest_prescription(patient_id):

        # read lab test prescription from data file
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            details = data['labtest_presc']

            for detail in details:
                if detail['id'] == patient_id:
                    print(detail['date'] + ' - ' + detail['labtest_presc'])

