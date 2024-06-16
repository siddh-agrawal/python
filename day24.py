tup = (1, 2,  3, 4, 5, 6, 6, True, "green") #if we cant use comma at last in only one element then its class changes to int
# tup[0] = 90 
print(type(tup), tup)
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])
print(tup[-1])
if 900 in tup:
    print("yes 900 is presen tin tuple")
else:
    print("900 is not present you nigger")

tup2 = tup[1:4] #slicing is same as list
print(tup2)

# tuples are immutable
# stirngs are immutable
# lists are mutable