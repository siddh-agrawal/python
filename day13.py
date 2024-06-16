# strings are immutable
a = "mayank'' yo yo yoy oy yoy yoynyo yoy oy yoyn''''''''''"

print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("'"))
print(a.replace("mayank", "john"))
print(a.split(" "))


leadroll = "introducTION OF LEAD YOIIIIIIIIIIIIIK"
print(leadroll.capitalize())
str1 = "welcome to the console!!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(a.count("mayank"))
str1 = "welcome to the console!!!"
print(str1.endswith("!!!"))
str1 = "welcome to the console!!!"
print(str1.endswith("to", 4, 10))

str2 = "he's name is dan. is "
print(str2.find("is"))
print (str2.index("is"))
# split can give us the list after the word that we gave it basically it separate the words after the space if we gave space in the split function 
# capitalize can convert first letter to capital and all other in small
# center is used for giving the spaces in starting it basically makes the word at center 
# count says us about occurence of the word thsat we gave it 
# endswith says us the boolian data that the word will end with that word or not 
# find can find the word in that string and if that word is not present then it shows -1
# index is same as find but if it cant find the word then it can produce an error 
str1 = "welcome to theconsole"
print(str1.isalnum())  #if string are alpha numeric string the islanum says true otherwise false

str1 = "welcome"       #if string are only alphabet containig then it says true
print(str1.isalpha())

str1 = "hello world"
print(str1.islower()) #if all characters are in lowercase then it say true otherwise it writtens false

str1 = "we wish you a merry christmas\n"
print(str1.isprintable()) #if all character are printable then it says true otherwise false 
str1 = "            "   #using space
print(str1.isspace())    #it says true if white spaces are there then it says true
str2 = "                " #using tab
print(str2.isspace())   #it says true if white spaces are there then it says true

str1 = "World Health Organization"
print(str1.istitle()) #it says true if all the first alphabet of our string are in capita then it says true otherwise false

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "python is a interpretated language"
print(str1.startswith("python")) #same as enddswith but it state about the starting word

str1 = "Python is A INterpretated Language"
print(str1.swapcase()) #it swap alphabets from lower to upper and vice versa

str1 = "his name is dan. dan is an honest man"
print(str1.title()) #it convert all the first letters of word in capital 