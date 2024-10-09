import random
import time
Open = input("Do You Want To Play Rock, Paper, Scissors ? (YES or No) : ")
if Open.upper() == "YES" :
    score = 0
    comp_score = 0
    while score < 3 and comp_score < 3 :
        choices = ["ROCK", "PAPER", "SCISSORS"]
        for words in choices:
            print(words)
            time.sleep(0.5)
        choice = random.choice(choices)
        user_choice = input("Your Choice : ").upper()
        if choice == user_choice:
            print("This Round Was A Draw!")
            print(f"Your Score : {score}")
            print(f"My Score : {comp_score}")
        elif (user_choice == "ROCK" and choice == "SCISSORS") or \
             (user_choice == "SCISSORS" and choice == "PAPER") or \
             (user_choice == "PAPER" and choice == "ROCK"):
            print("You Won! This Round")
            score += 1
            print(f"Your Score : {score}")
            print(f"My Score : {comp_score}")
        elif user_choice != "ROCK" or "SCISSORS" or "PAPER" :
           print("Error Not A Valid Choice ")
        else:
            print("I Won! This Round")
            comp_score +=1
            print(f"Your Score : {score}")
            print(f"My Score : {comp_score}")
    if score == 3 :
        print("Congratulations! You Won This Game!")
    elif comp_score == 3:
        print("Better Luck Next Time, I Won This Game!")

else:
    print("Okay comeback later!")
