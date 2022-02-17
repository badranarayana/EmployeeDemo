import sqlite3


# using context manager to close connection even when unexpected errors occurred
class DbConnection:
    def __enter__(self):
        # Create a SQL connection to our SQLite database
        self.con = sqlite3.connect("employee.sqlite")
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()


def create_employee_table():
    create_sql_statement = """
    CREATE TABLE IF NOT EXISTS employee (
        emp_id integer NOT NULL,
        email text NOT NULL,
        name text NOT NULL,
        mobile_number NULL,
        gender text NOT NULL,
        company text NOT NULL,
        manager text NOT NULL
    )
    """
    with DbConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(create_sql_statement)


def drop_employee_table():
    create_sql_statement = """
        DROP table employee
        """
    with DbConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(create_sql_statement)


class EmployeeModel:
    """
    Employee table crud operations
    """

    def get_by_id(self, id):
        sql_query = "select * from employee where emp_id={id}"
        sql_query = sql_query.format(id=id)

        with DbConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            emp_record = cursor.fetchone()
            if emp_record:
                data = {}
                #data['id'] = emp_record[0]
                # data['name'] = emp_record[1]
                # data['email'] = emp_record[2]
                # data['mobile_number'] = emp_record[3]
                # data['gender'] = emp_record[4]
                # data['company'] = emp_record[5]
                # data['emp_id'] = emp_record[6]
                # data['manager'] = emp_record[7]
                data['name'] = emp_record[0]
                data['email'] = emp_record[1]
                data['mobile_number'] = emp_record[2]
                data['gender'] = emp_record[3]
                data['company'] = emp_record[4]
                data['emp_id'] = emp_record[5]
                data['manager'] = emp_record[6]
                return data

            return {}

    def update(self, employee_data):
        sql_update_statement = """
        UPDATE employee set name='{name}', 
                            email='{email}', 
                            mobile_number='{mobile_number}',
                            gender='{gender}',
                            company='{company}',
                            emp_id={emp_id},
                            manager='{manager}'
                            WHERE id={id}
        """
        # bind values with sql statement
        sql_update_statement = sql_update_statement.format(**employee_data)

        with DbConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_update_statement)
            cursor.connection.commit()
            rows_affected = cursor.rowcount
            if rows_affected:
                print("db updated successfully")

    def delete(self, id):
        sql_delete_statement = """
        DELETE FROM employee where id={id}
        """
        sql_delete_statement = sql_delete_statement.format(id=id)

        with DbConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_delete_statement)
            cursor.connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted:
                print("record deleted successfully")

    def insert(self, employee_data):

        sql_insert_statement = """
        INSERT INTO employee(name,email,mobile_number,gender,company,emp_id,manager)
                    VALUES('{name}','{email}','{mobile_number}','{gender}','{company}',{emp_id},'{manager}') 
        
        """
        # bind the value into query params
        sql_insert_statement = sql_insert_statement.format(**employee_data)

        with DbConnection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_insert_statement)
            cursor.connection.commit()
            print("Successfully inserted into db")

    def insert_from_data_frame(self, data_frame):
        with DbConnection() as conn:
            # if_exists param will add record if not available already in db(duplicates will be skipped)
            data_frame.to_sql('employee', con=conn, if_exists='append')


if __name__ == '__main__':
    # create employee table
    #create_employee_table()
    #drop_employee_table()

    emp_table = EmployeeModel()

    # Insert operation data
    # emp_data = {
    #     'name': 'Nagaraj',
    #     'email': 'nag@mail.com',
    #     'mobile_number': '955562234',
    #     'gender': 'male',
    #     'company': "myCompany",
    #     'emp_id': 2345,
    #     'manager': "myManager"
    # }

    # lets insert data into employee table
    #emp_table.insert(emp_data)

    # get the inserted employee details
    print(emp_table.get_by_id(124))

    # lets delete employee id 16 record from database
    #emp_table.delete(16)


    # Update operation data

    # lets update employee by id
    emp_data = {
        'name': 'Nagaraj',
        'email': 'nagrajuuu@mail.com',
        'mobile_number': '955562234',
        'gender': 'male',
        'company': "myCompany",
        'emp_id': 2345,
        'manager': "myManager"
    }

    #emp_table.update(emp_data)
    #print(emp_table.get_by_id(15))

    import pandas as pd

    # Create dataframe
    data = pd.DataFrame({
        'name': ['nagaraju'],
        'email': ['nag@gmail.com'],
        'mobile_number': ['9010326666'],
        'gender': ['male'],
        'company': ['mycompany'],
        'emp_id': [124],
        'manager': ['mymanager']
    })

    # setting emp_id as index
    data.set_index('emp_id', inplace=True)

    emp_table.insert_from_data_frame(data)

