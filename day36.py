# a = input("enter the number:")
# print(f"multiplication table of{a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except:
#     print("invalid input")
    

# print("some important lines of code")
# print("end of program")

try:
    num = int(input("enter an integer:"))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("number entered is not an integer")
except IndexError:
    print("Index Error")
    