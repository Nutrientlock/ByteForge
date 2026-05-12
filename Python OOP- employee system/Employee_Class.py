class Employee:

    
    def __init__(self,emp_Id,name,role,status, hours_worked, hourly_rate):
        self.emp_Id = emp_Id
        self.name = name
        self.role = role
        self.status = status
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

        
        

    def calculate_GrossPay(self):
        return self.gross_pay
    
    def calculate_NIS(self):
        return self.nis
    
    def calculate_EduTax(self):
        return self.edu_tax
    
    def calculate_NetPay(self):
        return self.net_pay
    
    def complete_payslip(self):
        return self.gross_pay, self.nis, self.edu_tax, self.net_pay

    def display(self):
        print(f"-----------\nid: {self.emp_Id}\nname: {self.name}\nrole: {self.role}\nstatus: {self.status}")
        
e1 = Employee(123, "kar", "doctor","active",10,10)
e2 = Employee(143, "pin", "doctor","active",10,10)
e3 = Employee(153, "love", "RN","active",10,5)

class PayrollSystem:
    def __init__(self):
        self.employees = []
        self.gross_pay = self.hours_worked * self.hourly_rate
        self.nis = self.gross_pay * 0.025
        self.edu_tax = (self.gross_pay - self.nis) * 0.0225
        self.net_pay = self.gross_pay - self.nis - self.edu_tax

    def addEmployee(self, employee):
        self.employees.append(employee)

    def display(self):
        for employee in self.employees:
            employee.display()
    
    def calculate(self):
        for employee in self.employees:
            print("------------")
            print(employee.complete_payslip())
            
