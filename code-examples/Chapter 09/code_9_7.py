from collections import namedtuple

Employee = namedtuple('Employee', 'name id position')
emp = Employee('Alice', 'E123', 'Engineer')
print(emp)
