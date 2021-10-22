import brain_games_start,time
from time import sleep


def run(game_name,game_instruction,qu1,ans1,qu2,ans2,qu3,ans3):
    print("Welcome to the "+str(game_name))
    sleep(1)
    print("Hello",brain_games_start.name)
    sleep(1)
    print(str(game_instruction))
    sleep(1)

    print("Question ",str(qu1))
    a1 = input("Your answer")

    if a1 ==str(ans1):
        print("Correct")
    else:
        print("Fail")
        print("Correct answer was ",str(ans1))
        print("Try again")
        return

    sleep(2)

    print("Question ",str(qu2))
    a2 = input("Your answer")

    if a2 ==str(ans2):
        print("Correct")
    else:
        print("Fail")
        print("Correct answer was ",str(ans2))
        print("Try again")
        return

    sleep(2)

    print("Question ",str(qu3))
    a3 = input("Your answer")

    if a3 == str(ans3):
        print("Correct")
    else:
        print("Fail")
        print("Correct answer was ",str(ans3))
        print("Try again")
        return

    sleep(1)

    print("Congratulations",brain_games_start.name)

