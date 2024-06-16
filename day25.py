# countries = ("spain", "italy", "india", "england", "germany" )
# temp = list(countries)
# temp.append("russia") # add item
# temp.pop(3)           # remove item
# temp[2] = "finland"
# countries = tuple(temp)
# print(countries)
# print(type(countries))

# countries = ("pakistan", "afghanistan", "bangladesh", "sri lanka")
# countries2 = ("vietnam", "india", "china")
# southeastasia = countries + countries2
# print(southeastasia)

tuple1 = (0, 1, 2, 3, 2, 31, 2, 3, 3,)
# res = tuple1.count(3)
# res = tuple1.index(3)    #index skips the first occurenence of that number and gives the count of rest
# res = tuple1.index(3, 4, 8 )
res = len(tuple1)
print("length of tuple is", res)