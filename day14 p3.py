num = int(input("type the number babe"))
if (num < 0):
    print("no. is negative")
elif (num > 0):
    if (num <= 10):
        print("number is beetween 1-10")
    elif (num >10 and num <=20):
        print("number is beetween 11-20")
    else: 
        print("number is greater than 20")
else:
    print("number is zero")

         