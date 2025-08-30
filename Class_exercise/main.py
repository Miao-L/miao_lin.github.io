class Employee:

# Initilize METHOD
# The __init__ method Initialises a new instance (object) of the class.  is "SELF", you can name it something else too but by convention we should name it self
# SELF = Instance
# The keyword self represents the instance of a class and binds the attributes with the given arguments.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'.gmail.com'

    def fullname(self):
        return self.first + self.last

# Instance Variable
# Each employee will be unique "INSTANCE" of this Employee CLASS
# We can skip the instance(SELF) below, the "instance" is passed on automatically
# Need to pass the augument in order
emp_1 = Employee('Jeff','Shefer',50000)
emp_2 = Employee('Leah','lin', 1000000)


emp_1.fullname()
print(Employee.fullname(emp_1_))
print(emp_2.fullname())