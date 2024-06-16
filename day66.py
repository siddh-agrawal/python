class Employee:
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"the name of employee is {self.name} and the raise amount is {self.raise_amount}")

emp1 = Employee("harry")
emp1.raise_amount = 0.4
emp1.showDetails()
emp2 = Employee("sunny")
emp2.showDetails()
emp3 = Employee("rakki")
emp3.showDetails()
# emp3 = Employee("lead")
# emp4 = Employee("siddh")
