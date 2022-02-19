import requests
import json
import pprint


class EmployeeAPIClient:
    def __init__(self, url):
        self.url = url

    def upload_employees(self, file_path):
        """
        HTTP --> POST
        """
        response = requests.post(self.url, files={"file": open(file_path, 'rb')})
        return response.json()

    def get_employees(self):
        """
        HTTP --> GET
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()

    def get_employee(self, emp_id):
        """
        HTTP --> GET
        """
        url = self.url + '?emp_id={}'.format(emp_id)
        response = requests.get(url)
        return response.json()

    def update_employee(self, payload):
        """
        HTTP --> PUT
        """
        headers = {
            'Content-Type': 'application/json'
        }
        # converting python dict into json string
        payload = json.dumps(payload)
        response = requests.put(self.url, data=payload, headers=headers)

        return response.json()

    def delete_employee(self, emp_id):
        """
        HTTP --> DELETE
        """
        url = self.url + '?emp_id={}'.format(emp_id)
        response = requests.delete(url)
        return response.json()


# REST API Details
# employee crud rest api details
url = 'http://127.0.0.1:5000/employee'

client = EmployeeAPIClient(url=url)

# lets upload employee excel file into backend via rest api
file_path = r'C:\Users\91901\Downloads\New tst.xlsx'
#response = client.upload_employees(file_path)
#print(response)


# lets get the all employees
employees = client.get_employees()
#pprint.pprint(employees)


# lets get specific employee details by emp_id
employee_details = client.get_employee(2435)
print(employee_details)

# lets update the employee details
payload = {
    "company": "New Company Name",
    "email": "raju@gmail.com",
    "emp_id": 345,
    "gender": "male",
    "manager": "manager2",
    "mobile_number": "854579521",
    "name": "RAMU"
}

resp = client.update_employee(payload)
print(resp)

# Lets delete employee by emp_id
#out = client.delete_employee(2435)
#print(out)





