from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date

if __name__ == '__main__':
    calculate_salary('John', 23, 50)
    get_employees('Bill', 32, 'driver')
    print (date.today())