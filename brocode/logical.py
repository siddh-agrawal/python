temp = int(input("what is the temprature"))

if not(temp >=0 and temp <=30):
    print("temp is bad \n stay at home")
elif not (temp < 0 or temp >30):
    print("temp is good today")
    print("go outside")
    # print("temp is bad \n stay at home")
else:
    print("temp is bad dont go outside")