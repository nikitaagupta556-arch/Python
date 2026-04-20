class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self._emp_id = emp_id
        self._name = name
        self._basic_salary = basic_salary
    @property
    def emp_id(self):
        return self._emp_id
    @property
    def name(self):
        return self._name
    @property
    def basic_salary(self):
        return self._basic_salary
    @basic_salary.setter
    def basic_salary(self, amount):
        if amount >= 0:
            self._basic_salary = amount
        else:
            raise ValueError("Basic salary cannot be negative")
    def calculate_hra(self):
        return self._basic_salary * 0.20
    def calculate_da(self):
        return self._basic_salary * 0.50
    def calculate_gross_salary(self):
        return self._basic_salary + self.calculate_hra() + self.calculate_da()
    def calculate_tax(self):
        gross = self.calculate_gross_salary()
        if gross > 50000:
            return gross * 0.10
        elif gross > 30000:
            return gross * 0.05
        return 0.0
    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax()
    def generate_payslip(self):
        print("=" * 40)
        print("EMPLOYEE PAYSLIP".center(40))
        print("=" * 40)
        print(f"Employee ID   : {self._emp_id}")
        print(f"Employee Name : {self._name}")
        print(f"Basic Salary  : ₹{self._basic_salary:,.2f}")
        print("-" * 40)
        print(f"HRA (20%)     : ₹{self.calculate_hra():,.2f}")
        print(f"DA (50%)      : ₹{self.calculate_da():,.2f}")
        print("-" * 40)
        print(f"Gross Salary  : ₹{self.calculate_gross_salary():,.2f}")
        print(f"Tax Deducted  : ₹{self.calculate_tax():,.2f}")
        print("-" * 40)
        print(f"Net Salary    : ₹{self.calculate_net_salary():,.2f}")
        print("=" * 40)
class SalaryManagementSystem:
    def __init__(self):
        self._employees = []
    def add_employee(self, emp_id, name, basic_salary):
        employee = Employee(emp_id, name, basic_salary)
        self._employees.append(employee)
    def generate_all_payslips(self):
        if not self._employees:
            print("No employees in the system.")
            return
        for employee in self._employees:
            employee.generate_payslip()
            print()
if __name__ == "__main__":
    system = SalaryManagementSystem()
    while True:
        print("\n--- Enter Employee Details ---")
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        while True:
            try:
                basic_salary = float(input("Enter Basic Salary: "))
                if basic_salary < 0:
                    print("Salary cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for salary.")
        system.add_employee(emp_id, name, basic_salary)
        add_more = input("\nDo you want to add another employee? (y/n): ").strip().lower()
        if add_more != 'y' and add_more != 'yes':
            break
    print("\n" + "*" * 40)
    print("GENERATING ALL PAYSLIPS".center(40))
    print("*" * 40 + "\n")
    system.generate_all_payslips()