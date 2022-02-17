from flask import Flask
from flask_restful import Api

from employee_crud.api import EmployeeAPI


app = Flask(__name__)
api = Api(app)


def register_resources(api_instance):
    # we will keep all api endpoints here

    api_instance.add_resource(EmployeeAPI, '/employee/<int:emp_id>', endpoint='employee')


if __name__ == '__main__':
    register_resources(api_instance=api)
    app.run(debug=True, host='127.0.0.1', port=5555)

