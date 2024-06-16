s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
# print(s1.union(s2))                            #it means print the union of s1 and s2
s1.update(s2)   
print(s1)                                        #it means update s1 with the addition of elements of s2
# print(s1, s2)
cities = {"tokyo", "kabuo", "leftino", "madrid"}
cities2 = {"delhi", "seoul", "janpad", "kalos", "tokyo"}
# cities3 = cities.symmetric_difference(cities2) # it means make an cities 3 which contain the intersection elements
cities.intersection_update(cities2)            # it meansupdate cities with the intersection of cities 2
# cities3 = cities.difference(cities2)           # it means a-b
# print(cities.isdisjoint(cities2))              # it means disjoin sets means both are totally different
# print (cities.issuperset(cities2))             # it means cities 2 is subset of cities
# print (cities2.issuperset(cities))             # it means cities is subset of cities 2
# cities.add("helsink")                          # it simply adds one thing
# cities.remove("tokyo")                         # it used to remove thing from the set
# we can also use cities.discard("tokyo") it cannot raise any error if tokyo was not present but remove will produce an error if tokyo was not present
# item = cities.pop                              # it can randomly pop one value from the set that we gave
# del cities                                     # it can delete the whole  set
# info = {"carla", 19, False, 5.9}               
# if "carla" in info:
#     print("carla is present nigger")           # same as list and tuple i cant say it every time nigger
# else:
#     print("carla is not present nigger")
# print(item)
# print(cities)


print(cities2)