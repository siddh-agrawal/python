i = 0
while i<7:
    print(i)
    i = i + 1

    # if i == 4:
    #     break
else:
    print("sorry i is not defined")

for x in range(5):
    print("iteration no. {} in for loop".format(x+1))
else:
    print("else block is loop")
print("out of loop")