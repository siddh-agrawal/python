letter = "hey my name is {} and i am from {}"
country = "india"
name = "harry"
# print(letter.format(country, name)) its the old format technique
print(f"hey my name is {name} and i am from{country}")
print(f" we us ef- string like that: hey my name is {{name}} and i am from{{country}}")

price = 49.09
txt = f"for only{price:.2f} dollars!"
# print(txt.format())
print(txt)
print(type(f"{2*30}"))