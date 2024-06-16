# import time
# timestamp = (time.strftime("%H:%M:%S"))
# print(timestamp)
# hour = int(time.strftime("%H"))
# print(timestamp)

# def time():
#     if (hour>0 and hour<12):
#         print("good morning sir")
#     elif (hour>=12 and hour<17):
#         print("good afternoon sir")
#     else:
#         print("soo ja bhai raat ho ri")

# time()

    


# if(int("%H" <= 10 )):
#     print("good morning")
# elif(int("%H" == 12)):
#     print("good noon sir")
# elif(int( "%H"<=18)):
#     print("good evening sir")
# else:
#     print("good night")
import time

hour = int(input("enter the value of hour of your time zone"))
# hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
second = int(time.strftime("%S"))

print("Current Time:", hour, ":", minute, ":", second)


if hour < 10:
    print("Good morning!")
elif hour == 12:
    print("Good noon, sir!")
elif hour < 18:
    print("Good evening, sir!")
else:
    print("Good night!")
