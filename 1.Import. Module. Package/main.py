from application.salary import Accountant
from application.db.people import Hr
from datetime import date

if __name__ == '__main__':
    acc = Accountant('Василий')
    hr = Hr('Мария')
    print(date.today())
    acc.calculate_salary()
    hr.get_employees()


