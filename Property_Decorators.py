#PropertyDecorators.py

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Setting up the email as a function call
    # However anyone who uses the class would have to update the function call
    # Using @property decorator, we can call the email as an attribute rather than a function call
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # Also want an ability to change the fullname and have it update all the other relevant field
    # Can do this using a setter. Splits name into firt, last and updates email

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # What gets run when we delete an attirbute
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Doe')

# print(emp_1.email)
# print(emp_1.fullname())

emp_1.fullname = 'Corey Schafer'

# if there was no setter, the first name could be changed but it wouldn't update the email
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
