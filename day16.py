x = int(input("enter the value of x:"))
#x is variable to match
match x:
    case 0:
        print("x is zero ")
    case 4:
        print("case is 4 ")
# case wwuth if condition
    case _ if x==90:
        print("x,is not 90")
    case _ if x==80:
        print("x,is not 80")
    case _ if x<=555 :
        print("tum kuch nhi kr skta re baba")
    case _:
        print("bhut dukh hua ")