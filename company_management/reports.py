from employees import Developer, Designer, Manager


def calculate_total_salary(employees):
    total = 0

    for employee in employees:
        if employee.active:
            total += employee.salary

    return total


def calculate_total_bonuses(employees):
    total = 0

    for employee in employees:
        if employee.active:
            total += employee.calculate_bonus()

    return total


def calculate_total_payroll(employees):
    total = 0

    for employee in employees:
        if employee.active:
            total += employee.salary + employee.calculate_bonus()

    return total


def count_employees_by_type(employees):
    result = {"developers": 0, "designers": 0, "managers": 0}

    for employee in employees:
        if isinstance(employee, Developer):
            result["developers"] += 1

        elif isinstance(employee, Designer):
            result["designers"] += 1

        elif isinstance(employee, Manager):
            result["managers"] += 1

    return result
