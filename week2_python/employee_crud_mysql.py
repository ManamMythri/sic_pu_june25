import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.Connect(host='localhost', user="root", password="mythri", datebase='mythri_db', port=3306, charset="utf8")
        print('Database Connected')
    except:
        print('Database Connection Failed')
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('DB disconnected')
    except:
        print('DB disconnection failed')

def create_db():
    query = 'create database IF NOT EXISTS mythri_db'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Database created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Database creation failed')

def create_table():
    query = 'create table IF NOT EXISTS employees(id int primary key auto_increment, name varcahr(50) not null, designation varchar(30), phone_number	bigint unique, salary float, commission		float default(0), years_of_experience tinyint, technology		varchar(30)	not null)'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Table creation failed')

def read_all_employees():
    query = 'select * from employees'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchAll()
        for row in rows:
            print(row)
        print('All rows retrived')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Rows retrival failed')

def search_employee():
    id = int(input('Enter Id of the employee to search: '))
    query = f'select * from employees where id = {id}'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('All rows retrived')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Rows retrival failed')

def read_employee_details():
    name = input('Enter employee name: ')
    designation = input('Enter employee designation: ')
    phone_number = int(input('Enter employee phone number: '))
    salary = float(input('Enter employee salary: '))
    commission = float(input('Enter employee commission: '))
    years_of_experience = input('Enter employee years of experience: ')
    technology = input('Enter employee technology: ')
    return (name, designation, phone_number, salary, commission, years_of_experience, technology)  

def insert_employee():
    employee = read_employee_details()
    query = 'insert in to employees(name, designation, phone_number, salary, commission, years_of_experience, technology) values(%s, %s, %s, %s, %s, %s, %s)'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        value = cursor.execute((query, employee))
        cursor.close()
        disconnect_db()
        if value == 1:
            print('Row inserted')
        else:
            print('Row insertion failed')
    except:
        print('Row insertion failed')

def update_employee():
    salary = float(input('Enter employee salary: '))
    years_of_experience = input('Enter employee years of experience: ')
    id = int(input('Enter id of the employee to be updated: '))
    query = f'update employees set years_of_experience = {years_of_experience}, salary = {salary} where id = {id}'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Employee with id = {id} not found')
        else:
            print(f'Employee with id = {id} updated')
    except:
        print('Employee update failed')

def delete_employee():
    id = int(input('Enter id of the employee to be deleted: '))
    query = f'delete from employees where id = {id}'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Employee with id = {id} not found')
        else:
            print(f'Employee with id = {id} deleted')
    except:
        print('Employee delete failed')