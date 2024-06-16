class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


    def showDetails(self):
        print(f"the name of employee: {self.id} is {self.name}")

class programmer(employee):
    def showLanguage(self):
        print("The default Language is Python")


e1 = employee("rohan das", 400)
e1.showDetails()
e2 = programmer("harry", 4100)
e2.showDetails()
e2.showLanguage()