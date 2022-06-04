import random

while True:
    player = input("Pick an option between R = rock, P = paper or S = scissors): ")
    R = "rock"
    P = "paper"
    S = "scissors"
    options = [R, P, S]
    
    cpu = random.choice(options)
    print(f"\nPlayer {player} : CPU {cpu}.\n")

    if player == cpu:
        print(f"You both chose {player}. It's a tie!")
        continue
    elif player == "rock":
        if cpu == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
        break
    elif player == "paper":
        if cpu == "rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
        break
    elif player == "scissors":
        if cpu == "paper":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")
        break
    else:
        print("You picked an invalid choice")
        continue
    
    