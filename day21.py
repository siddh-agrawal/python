# def average(a, b):
#     print("the average is", (a+b)/2)


# def name(fname, mname = "olas", lname = "pablo"):
#     print("yooo", fname, mname ,lname )


# # name("nich")
# a = int(input("type the first number sir."))
# b = int(input("type the second number sir."))
# average(a, b)

def average(*numbers):
    sum = 0
    # sum = 0
    for i in numbers:
        sum = sum + i
    # print("average of number is", sum / len(numbers))
    # return 7                                # return is equal to that we can back after taking the first value
    return sum / len(numbers)

c = average(4, 4, 4, 4)
print(c)

# def name(**name):
#     print(type(name))
#     print("hello", name["fname"], name["mname"], name["lname"])

# name(mname = "buchanan", lname = "pablo", fname = "nicholas")