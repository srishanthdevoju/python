class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
eo=Employee("Alice",80000)
mo=Manager("Bob",98909,"Sales")
eo.display()
mo.display()
    

        