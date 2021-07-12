import datetime as dt
# Regular methods pass the class instance as the first argument = self
# Class methods pass in the class as the first argument = cls
# Static methods do not pass anything but behave like regular functions

class Employee:
    
    raise_amount = 10.04
    gmail = '@gmail.com'
    yahoo = '@yahoo.com'
    num_of_employees = 0
    
    def __init__(self, fistName, lastName, gender, pay):
        self.first = fistName
        self.last = lastName
        self.gender = gender
        self.p = pay
        self.email = fistName + '.' + lastName + self.gmail
        Employee.num_of_employees += 1

    def apply_raise(self): # Regular method
        self.p = int(self.p + self.raise_amount)
        return self.p
    
    @classmethod
    def set_raised_amount(cls,amount):  # class becomes first argument
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str): # Using class methods as contructors
        firstName, lastName , gender, pay = emp_str.split('-')
        return cls(firstName, lastName, gender, pay)

    @staticmethod
    def is_workDay(day): # static method
        if day.weekday == 5 or day.weekday == 6:
            return False
        else:
            return True



emp_1 = Employee('James','Hunter','Male',100000)
emp_2 = Employee('Luvas','Gasper','Female',300000)

# we can set this using the class method
Employee.set_raised_amount(30) # This sets the class variable to 30

# If we run this we get 10.04
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'Jimmy-Kim-Male-450000'
emp_str_2 = 'Kameron-Straus-Female-900000'
emp_str_3 = 'Young-loo-Female-760000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)


my_date = dt.date(2021, 6, 10)
workDay = Employee.is_workDay(my_date)
print(workDay)