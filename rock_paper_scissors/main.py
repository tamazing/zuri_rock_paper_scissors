import random

while True:
    player = input(
        "Pick an option between rock, paper or scissors): ")
    R = "rock"
    P = "paper"
    S = "scissors"
    options = [R, P, S]

    cpu = random.choice(options)
    print(f"\nPlayer {player.title()} : CPU {cpu.title()}.\n")

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
        print("You picked an invalid option")
        continue

git pull remotename master:dev
git add --all
git commit -m "some message"
git pull remotename master:dev
git push remotename master:dev

git init
git add .
git commit -m "first commit"
git remote add origin **<YOUR URL>**
git pull --rebase origin master
git push -f origin master