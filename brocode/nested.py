# nested loops = the "inner loop" will finish all of it's iterations before
#                 finishing one iteration of the "outer loop"

rows = int(input("how many rows?: "))
coloumns = int(input("how many coloumns?: "))
symbol = input("enter the symbol you want to use: ")

for i in range (rows):
    for j in range(coloumns):
        print(symbol, end="")
    print()
