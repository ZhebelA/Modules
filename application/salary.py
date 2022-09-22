from russian_coast import RussianCost

def calculate_salary(name, working_days, salary_per_day):
    salary_for_month = RussianCost(working_days*salary_per_day)
    print(f'Зарплата работника за месяц составит: {salary_for_month}')