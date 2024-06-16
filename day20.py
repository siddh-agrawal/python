def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

def isLesser(a, b):
    if a == 0:
         print("first number is zero")
    elif(a<b):
        print("first number is lesser")
    else:
        print("second number is greater or equal")

a = int(input("enter the first no. sir"))
b = int(input("enter the second no. sir"))
# if(a>b):
#     print("first number is greater")
# else:
#     print("second number is greater or equal")


calculateGmean(a, b)
isGreater(a, b)
isLesser(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c =  int(input("enter the first no. sir"))
d = int(input("enter the second no. sir"))
# if(c>d):
#     print("first number is greater")
# else:
#     print("second number is greater or equal")
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d)
isGreater(c, d)
isLesser(c, d)