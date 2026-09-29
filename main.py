import random
def get_cpu_choice():
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    return cpu_choice
def get_player_choice():
    while True:
        player_choice = input("Choose rock, paper, or scissors: ")

        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        winner = "Tie"

    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "you win"
        else:
            winner = "AI"

    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "you win"
        else:
            winner = "AI"

    elif player_choice == "paper":
        winner = "AI"

    else:
        winner = "you win"

    return winner


cpu_choice = get_cpu_choice()

player_choice = get_player_choice()

winner = check_winner(cpu_choice, player_choice)

print(winner)