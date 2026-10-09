from utils import generate_employee_id, get_current_time


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.employee_id = generate_employee_id()
        self.active = True
        self.created_at = get_current_time()

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Active: {self.active}")
        print(f"Created at: {self.created_at}")

    def work(self):
        print(f"{self.name} is working.")

    def calculate_bonus(self):
        return self.salary * 0.05

    def deactivate(self):
        self.active = False
        return True


class Developer(Employee):
    def __init__(self, name, salary, programming_language, level):
        super().__init__(name, salary)

        self.programming_language = programming_language
        self.level = level

    def work(self):
        print(f"{self.name} is writing {self.programming_language} code.")

    def show_info(self):
        super().show_info()
        print(f"Programming Language: {self.programming_language}")
        print(f"Level: {self.level}")

    def calculate_bonus(self):
        if self.level == "Junior":
            return self.salary * 0.05

        elif self.level == "Middle":
            return self.salary * 0.10

        else:
            return self.salary * 0.15


class Designer(Employee):
    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)

        self.specialization = specialization

    def work(self):
        print(f"{self.name} is creating {self.specialization} designs.")

    def show_info(self):
        super().show_info()
        print(f"Specialization: {self.specialization}")

    def calculate_bonus(self):
        return self.salary * 0.08


class Manager(Employee):
    def __init__(self, name, salary, department, team_name):
        super().__init__(name, salary)

        self.department = department
        self.team_name = team_name
        self.team = []

    def add_team_member(self, employee):
        if not employee.active:
            return False

        self.team.append(employee)
        return True

    def show_team(self):
        for employee in self.team:
            print(employee.name)

    def work(self):
        print(f"{self.name} is managing the {self.department} team.")

    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}")
        print(f"Team: {len(self.team)}")

    def calculate_bonus(self):
        return self.salary * 0.12
