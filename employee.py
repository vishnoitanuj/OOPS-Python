class Employee:
    def __init__(self, first,last, pay):
         self.first = first
         self.last = last
         self.email = first + '.' + last + '@company.com'
         self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first,self.last)


emp1= Employee('Corey','Schafer',500000)
emp2 = Employee('Test','User',60000)

print(emp1.full_name())
print(Employee.full_name(emp2))