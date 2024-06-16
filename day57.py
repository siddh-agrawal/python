class person:
    name = "harry"
    occupation = "software developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}") #self mean the object in which this function called

a = person()
a.name = "shubham"
a.occupation = "accountant"
# print(a.name, a.occupation)
a.info()
