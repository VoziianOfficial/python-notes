from employees import Employee, Developer, Manager, Designer
from company import Company
import reports

# -------------------------
# 1. СОТРУДНИКИ
# -------------------------

developer1 = Developer("Yuliia", 50000, "Python", "Junior")

developer2 = Developer("Alex", 70000, "JavaScript", "Senior")

designer = Designer("Anna", 60000, "UI/UX")

manager = Manager("Max", 80000, "Development", "Development Team")


# -------------------------
# 2. COMPANY
# -------------------------

company = Company("TechNova")


# -------------------------
# 3. ДОБАВЛЯЕМ СОТРУДНИКОВ
# -------------------------

company.add_employee(developer1)
company.add_employee(developer2)
company.add_employee(designer)
company.add_employee(manager)


# -------------------------
# 4. КОМАНДА MANAGER
# -------------------------

manager.add_team_member(developer1)
manager.add_team_member(developer2)
manager.add_team_member(designer)

print("\n--- MANAGER TEAM ---")
manager.show_team()


# -------------------------
# 5. ПОКАЗАТЬ СОТРУДНИКОВ
# -------------------------

print("\n--- EMPLOYEES ---")

for employee in company.employees:
    employee.show_info()
    print()


# -------------------------
# 6. РАБОЧИЙ ДЕНЬ
# -------------------------

print("\n--- WORKDAY ---")

company.run_workday()


# -------------------------
# 7. БОНУСЫ
# -------------------------

print("\n--- BONUSES ---")

for employee in company.employees:
    bonus = employee.calculate_bonus()

    print(f"Name: {employee.name}")
    print(f"Salary: {employee.salary}")
    print(f"Bonus: {bonus}")
    print()


# -------------------------
# 8. ЗАРПЛАТНЫЕ ОТЧЁТЫ
# -------------------------

total_salary = reports.calculate_total_salary(company.employees)
total_bonuses = reports.calculate_total_bonuses(company.employees)

total_payroll = total_salary + total_bonuses

print("\n--- PAYROLL REPORT ---")
print("Total salary:", total_salary)
print("Total bonuses:", total_bonuses)
print("Total payroll:", total_payroll)


# -------------------------
# 9. ПОИСК ПО ID
# -------------------------

print("\n--- FIND EMPLOYEE ---")

developer_id = developer1.employee_id

found_employee = company.find_employee_by_id(developer_id)

if found_employee is not None:
    print("Employee found:", found_employee.name)
else:
    print("Employee not found")


unknown_employee = company.find_employee_by_id("EMP-0000")

print("Unknown employee:", unknown_employee)


# -------------------------
# 10. УВОЛЬНЕНИЕ
# -------------------------

print("\n--- DEACTIVATE EMPLOYEE ---")

deactivate_result = company.deactivate_employee(designer.employee_id)

print("Deactivate result:", deactivate_result)
print("Designer active:", designer.active)


# Проверяем рабочий день ещё раз

print("\n--- WORKDAY AFTER DEACTIVATION ---")

company.run_workday()


# -------------------------
# 11. ПРОВЕРКА НАСЛЕДОВАНИЯ
# -------------------------

print("\n--- ISINSTANCE ---")

print(isinstance(developer1, Developer))
print(isinstance(developer1, Employee))
print(isinstance(manager, Manager))
print(isinstance(manager, Employee))


print("\n--- ISSUBCLASS ---")

print(issubclass(Developer, Employee))
print(issubclass(Designer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Employee, Developer))


# -------------------------
# 12. ПОЛИМОРФИЗМ
# -------------------------


def show_employee_work(employee):
    if not employee.active:
        print(f"{employee.name} is inactive")
        return

    employee.work()


print("\n--- POLYMORPHISM ---")

show_employee_work(developer1)
show_employee_work(designer)
show_employee_work(manager)
