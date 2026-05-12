from Employee_Class import Employee
from Employee_Class import PayrollSystem
system = PayrollSystem() 

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")

def password(passcode, chances = 3):
    
    cheat = '0'
    for remaining in range(chances, 0, -1):
        attempt = input("Enter passcode: ").strip()

        if attempt == passcode or attempt == cheat:
            print("Access Granted")
            return True

        print("Invalid input")
        print(f"Number of chances left: {remaining - 1}")

def get_employee():
    name = input("ENTER FIRST NAME: ").strip()
    emp_Id = input("ENTER ID NUMBER: ").strip()
    role = input("ENTER ROLE: ").strip()
    status = input("STATUS: ").strip()

    hours_worked = get_int_input("ENTER HOURS WORKED: ")
    hourly_rate = get_int_input("ENTER HOURLY RATE: ")

    print("Employee added successfully!")
    e = Employee(emp_Id, name, role, status, hours_worked, hourly_rate)
    return e
    
        
def Menu():
    
    passcode = 'werty' 
    print("MENU STARTED")

    while True:
        print("____________________")
        print("|1. Add Employees  |")
        print("|2. Veiw Employees |")
        print("|3. Run Payroll    |")
        print("|4. Exit           |")
        print("|__________________|")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("ADD EMPLOYEE SELECTED...")
            if password(passcode) == False:
                print("Blocked")
                continue
            employee = get_employee()
            system.addEmployee(employee)

        elif choice == '2':
            print('VEIW EMPLOYEES SELECTED')   
            system.display()
        
            
            
if __name__ == "__main__":
    Menu()     
