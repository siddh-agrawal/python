class Employee:
    def __init__(self):
        self._name = "harry"

a = Employee()
# a.emp1 = 5
print(a._name)
print(a.__dir__())