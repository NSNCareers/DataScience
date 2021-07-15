

class Employee:
    
    def __init__(self,fistName,lastName,gender,pay): # This is the constructor and gets called each time the class is used
        self.first = fistName
        self.last = lastName
        self.gender = gender
        self.p = pay
        self.email = fistName + '.' + lastName + "@gmail.com"
        
    # Helps display user output 
    def __str__(self): # special method. This will overide repr
        return '{} - {}, '.format(self.first, self.email)


    def __repr__(self): # special method
        return '{}, {}, {}, {}, {}'.format(self.first, self.last, self.gender, self.p,self.email)

emp_1 = Employee('James','Hunter','Male',100000)
emp_2 = Employee('Luvas','Gasper','Female',300000)

print(emp_1)