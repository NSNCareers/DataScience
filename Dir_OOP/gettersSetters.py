

class Employee:
    
    def __init__(self,fistName,lastName): # This is the constructor and gets called each time the class is used
        self.first = fistName
        self.last = lastName
     
    # getters
    @property
    def emailAddress(self): 
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    # getters
    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    # setters
    @fullName.setter
    def fullName(self, name):
        firstName, lastName = name.split(' ')
        self.first = firstName
        self.last = lastName

    # setters
    @fullName.deleter
    def fullName(self):
        print('Deleting names')
        self.first = None
        self.last = None

emp_1 = Employee('James','Hunter')
# use setters to set values
emp_1.fullName = 'kelly price'
# deletes names
del emp_1.fullName
print(emp_1.emailAddress)
print(emp_1.fullName)