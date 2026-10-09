class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        return True

    def find_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee

        return None

    def show_all_employees(self):
        for employee in self.employees:
            employee.show_info()

    def run_workday(self):
        for employee in self.employees:
            if employee.active:
                employee.work()

    def deactivate_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.deactivate()
                return True

        return False
