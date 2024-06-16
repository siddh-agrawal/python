questions = [["which language was use to create facebook",'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],
["which language was use to create facebook", 'python', 'french', 'javascript', 'php', 'none', 4],]

levels = [1000, 2000, 3000, 4000, 10000, 200000, 160000, 320000, 700000, 88888888, 999999999999, 1000100101001, 10102020202020]
money = 0

for i  in range (0, len(questions)):
    question = questions[i]
    print(f"{questions[i]}question for rs. {levels[i]}")
    print(f"a. {question[1]}              b. {question[2]} ")
    print(f"c. {question[3]}              d. {question[4]} ")
    reply = int(input("enter your answer (1-4)"))
    if(reply == question[-1]):
        print(f"correct answer, you have won rs.{levels[i]}" )
        if(i == 14):
            money = 7000000
        elif(i == 9):
            money = 320000
        elif(i == 4):
            money = 10000
    else:
        print("wrong answer!")
        break

print(f"your total winning money was {money}")