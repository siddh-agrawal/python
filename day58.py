class person:
    def __init__(self, name , occ):
        # print('hey i am a person')
        self.name = name
        self.occ = occ

        
    # name = ("harry")
    # occ = ("developer")

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("harry", "developer")
b = person("divya", "hr")
c = person(1, 2)
a.info()
b.info()
