# dic = {
#     5687: "human being",
#     567:  "object"

# }
# print(dic[5678])

info = {'name': 'karan', 'age': '19', 'eligible':True}
# print(info)                       # it prints the whole info
# print(info['name'])               # it gives us the specific vaue of name
# print(info.get('name'))           # it was same as info[name but it cant give error if name was not present]
# print(info.keys())                # it gives us the value of all keys
# print(info.values())              # it gives us the value of all values

# for key in info.keys():
#     print(f"the value corresponding to the {key} is {info[key]}")           

print("i am not a gangster vmroooooooooo")
print(info.items())   
for key, value in info.items():
     print(f"the value corresponding to the key {key} is {value}")
