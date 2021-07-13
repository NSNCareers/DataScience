
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

# Create class Instances
dev_1 = Developer('James','Hunter','Male',100000,'Python')
dev_2 = Developer('Luvas','Gasper','Female',300000,'dotnet')

# This shows we can still access all the attributes of the parent class
# print(emp_1.email)
# print(emp_2.fullName())

# This shows we can change an attribute of the sub class without altering
# that of the parent class
print(dev_1.raise_amount)

# This shows us the method resolution
# print(help(Developer))


print(dev_1.prog_language)
print(dev_2.prog_language)