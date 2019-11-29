class Employee:

    raise_amount = 1.04
    num_of_emp = 0
    def __init__(self, first,last, pay):
         self.first = first
         self.last = last
         self.email = first + '.' + last + '@company.com'
         self.pay = pay

         Employee.num_of_emp += 1

    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1= Employee('Corey','Schafer',500000)
emp2 = Employee('Test','User',60000)

print(emp1.__dict__)
print(Employee.__dict__)
emp1.raise_amount = 1.05
print(emp1.__dict__)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print("Num of emp = ",Employee.num_of_emp)

print(emp1.full_name())
print(Employee.full_name(emp2))