# Python OOP Tutorial 5: Special (Magic/Dunder) Methods

# By defining our own special methods, we can make our classes behave like built-in types.
# These special methods are surrounded by _ _ underscore characters.

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    
    # repr is an unambigous representation of an object
    # used for debugging and logging
    # want to display the object in a way that is easy to read / can copy into python code
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # str is a more readable representation of an object
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))