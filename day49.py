# reading of a file

f = open("myfile.txt", "rb")
# print(f)  
text = f.read()
print(text)
f.close()
f = open("myfile.txt", "a")
f = open("myfile.txt", "a")
f.write("yoiiiiiiiiiiiiiiiiii")
f.close()


with open ("myfile.txt", "a") as f:
    f.write("hey i am inside with")


