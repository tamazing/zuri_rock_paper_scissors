import random

while True:
    print("\n Welcome to the Rock, Paper and Scissors Game! \n")
    player = input(
        "Pick an option;  R for rock, P for paper or S for scissors): ")
    player = player.upper()
    R = "rock"
    P = "paper"
    S = "scissors"
    options = [R, P, S]

    computer = random.choice(options)

    #print(f"\nYou chose {player.upper()} : computer chose {computer[:][0].upper()}.\n")
    if player == computer:
        print(f"You both chose the same thing. It's a tie! \n")
        continue
    elif player == "R":
        if computer == "S":
            print("\n Player R : computer S ")
            print(" \n Rock smashes scissors! You win! \n")
        else:
            print("\n Player R : computer P")
            print(" \n Paper covers rock! You lose. \n")
        break
    elif player == "P":
        if computer == "R":
            print("\n Player P : computer R")
            print(" \n Paper covers rock! You win! \n")
        else:
            print("\n Player P : computer S")
            print(" \n Scissors cuts paper! You lose. \n")
        break
    elif player == "S":
        if computer == "P":
            print("\n Player S : computer P")
            print(" \n Scissors cuts paper! You win! \n")
        else:
            print("\n Player S : computer R")
            print(" \n Rock smashes scissors! You lose. \n")
        break
    else:
        print("You made an invalid choice \n")
        continue
