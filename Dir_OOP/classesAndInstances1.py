
# Classes help us logically group our data and functions for ease of usability and build upon

# Create a class
class Employee:
    pass # so that the compiler does not trow an error

# class Instances
emp_1 = Employee()
emp_2 = Employee()

# Both have different locations in memory
print(emp_1)
print(emp_2)

# Set attributes for both employees instances
emp_1.fistName = 'James'
emp_1.lastName = 'Hunter'
emp_1.gender = 'Male'
emp_1.pay      = 100000
emp_1.emailAddress = 'james@gmail.com'

emp_2.fistName = 'Luvas'
emp_2.lastName = 'Gasper'
emp_2.gender = 'Female'
emp_2.pay      = 300000
emp_2.emailAddress = 'Luvas@gmail.com'

print(emp_1.emailAddress)
print(emp_2.emailAddress)

# The above code is prone to mistakes and below is another way of acheiving above in the next file