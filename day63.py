import random
def check(comp, user):
    if comp ==user:
        return 0
    elif (comp == 0 and user ==1):
        return -1
    elif (comp == 1 and user ==2):
        return -1
    elif (comp == 2 and user ==0):
        return -1
    else:
        return 1
user = int(input(" 0 for rock, 1 for scissor, and 2 for paper"))
comp = random.randint(0, 2)

score = check(comp,user)

print("you: ", user)
print("computer: ", comp)
if(score == 0):
    print("its a draw")
elif (score == -1):
    print("you lose")
else:
    print("you won")
    bool("we ewant int("())):