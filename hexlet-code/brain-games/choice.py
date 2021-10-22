import brain_gcd,brain_calc,brain_even,brain_prime,brain_games_start,brain_progression
import time
from time import sleep

def choice():
    sleep(1)

    while True:
        print("Do you want to play a game?")
        print("Print yes or no")
        answer=input()

        if answer=="no":
            print("Goodbye",brain_games_start.name)
            exit()
        if answer=="yes":
            break
        else:
            return

    print("what game do you want to play ?")
    sleep(1)
    print("brain-gcd","brain-calc","brain-even","brain-prime","brain-progression")
    print("Print what game do you want to play")
    game=input()

    if game=="brain-gcd":
        brain_gcd.run()

    if game=="brain-calc":
        brain_calc.run()

    if game=="brain-even":
        brain_even.run()

    if game=="brain-prime":
        brain_prime.run()

    if game=="brain-progression":
        brain_progression.run()
