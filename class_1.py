class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}")
        
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} has received a raise of ${amount}. New salary: ${self.salary}") 
        
    def salary_payment(self, noofdays):
        self.noofdays = noofdays
        total_payment = self.salary * noofdays
        print
        print(f"{self.name} has worked for {self.noofdays} days and been paid ${total_payment}.")
        
        
# This code defines a simple Employee class with an initializer that takes a name and age, and a method to display the employee's information.


emp1 = Employee("Alice", 30, 50000)
emp2 = Employee("Bob", 25, 60000)
emp3 = Employee("Charlie", 35, 70000)

emp1.display_info()

emp1.give_raise(5000)
emp1.salary_payment(20)
emp2.salary_payment(15)



