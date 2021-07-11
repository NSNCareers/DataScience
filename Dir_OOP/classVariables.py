

# Class variables are those shared by all instances of a class

class Employee:

    raise_amount = 10.04
    gmail = '@gmail.com'
    yahoo = '@yahoo.com'
    num_of_employees = 0
    
    def __init__(self,fistName, lastName, gender, pay):
        self.first = fistName
        self.last = lastName
        self.gender = gender
        self.p = pay
        self.email = fistName + '.' + lastName + self.gmail
        Employee.num_of_employees += 1

    def apply_raise(self):
        self.p = int(self.p + self.raise_amount)
        return self.p
# print(Employee.num_of_employees)
emp_1 = Employee('James','Hunter','Male',100000)
emp_2 = Employee('Luvas','Gasper','Female',300000)

print(emp_1.p)
print(emp_1.apply_raise())
print(emp_2.email)
# Shows you the class attributes and instance attributes
print(Employee.__dict__) # This prints out the name space of Employee
print(emp_1.__dict__) # This prints out the name space of emp_1
print(emp_2.__dict__) # This prints out the name space of emp_2

# change class variable using class instance empl_1
emp_1.raise_amount = 30
# change class variable using class its self
Employee.raise_amount = 20

print(emp_1.raise_amount)
print(Employee.raise_amount)

print(emp_1.__dict__) # This prints out the name space of emp_1
print(emp_2.__dict__) # This prints out the name space of emp_2
print(Employee.num_of_employees)

