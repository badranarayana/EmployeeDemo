import pandas as pd
from flask_restful import Resource
from flask import jsonify
from flask import request

from employee_crud.db import EmployeeModel


class EmployeeAPI(Resource):

    def post(self):
        # lets load upload file into pandas data frame
        data_frame = pd.read_csv(request.files.get('file'))

        # Rename file columns as per db column names
        data_frame.rename(columns={'EMP ID': 'emp_id',
                                   'EMAIL': 'email',
                                   'NAME': 'name',
                                   'NUMBER': 'mobile_number',
                                   'GENDER': 'gender',
                                   'COMPANY': 'company',
                                   'MANAGER': 'manager'
                                   }, inplace=True)

        employee_table = EmployeeModel()
        employee_table.insert_from_data_frame(data_frame)

        return jsonify({
            'message': "File processed successfully"})

    def get(self, emp_id):
        employee_table = EmployeeModel()
        employee_dict = employee_table.get_by_id(emp_id)

        return jsonify(employee_dict)

    def put(self, emp_id):
        pass

    def delete(self, emp_id):
        pass
