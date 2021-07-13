
# Inheritance allows us to inherit attributes and methods from a parent class
# We can create sub classes and and get all the funcionalities of the parent class
# or overide these functionalities in the sub class without affeting the parent class

class Employee:

    raise_amount = 1.5
    
    def __init__(self,fistName,lastName,gender,pay): # This is the constructor and gets called each time the class is used
        self.first = fistName
        self.last =  lastName
        self.gender =  gender
        self.p =  pay
        self.email = fistName + '.' + lastName + "@gmail.com"

    def fullName(self):
        return '{} {}'.format(self.first, self.last)


# Lets create two classes called developer and manager and inherit the attributes from Employee class
# since they both belong to employee

class Developer(Employee):
    raise_amount = 8.3

    def __init__(self,fistName,lastName,gender,pay,prog_language): 
        super().__init__(fistName,lastName,gender,pay) # We want the parent class to handle all these attributes
        self.prog_language = prog_language

class Manager(Employee):

    def __init__(self,fistName,lastName,gender,pay,employees =None): 
        super().__init__(fistName,lastName,gender,pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)


    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(emp.fullName())

# Create class Instances
dev_1 = Developer('James','Hunter','Male',100000,'Python')
dev_2 = Developer('Luvas','Gasper','Female',300000,'dotnet')
dev_3 = Developer('Hunter','HHHH','Female',7890000,'Java')
dev_4 = Developer('Leonard','Shelly','Male',9870000,'Node JS')

# manager supervises developers thus taking a list 
mgr = Manager('Cherio','Santas','Female',6000000,[dev_1,dev_2])

print(mgr.email)
# mgr.print_employees()
mgr.add_employee(dev_4)
# mgr.print_employees()
mgr.remove_employee(dev_1)
# mgr.print_employees()

print(isinstance(mgr,Manager)) # is this an instance of the class?
print(issubclass(Manager,Employee)) # is class sub class?