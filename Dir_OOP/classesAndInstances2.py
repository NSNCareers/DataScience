
# Classes help us logically group our data and functions for ease of usability and build upon

# Create a class and a method 
# self is the instance of the class
# We can use the special init function to initialize our class
class Employee:

    def __init__(self,fistName,lastName,gender,pay): # This is the constructor and gets called each time the class is used
        self.first = fistName
        self.last = lastName
        self.gender = gender
        self.p = pay
        self.email = fistName + '.' + lastName + "@gmail.com"

    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def emailAddress(self):
        return '{}'.format(self.email)


# Create class Instances
emp_1 = Employee('James','Hunter','Male',100000)
emp_2 = Employee('Luvas','Gasper','Female',300000)

# You can now call directly
# print(emp_1.email)
# print(emp_2.gender)

# Create methods in the class and call the methods

print(emp_1.emailAddress())
print(emp_2.fullName())

