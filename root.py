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
        winner = "tie"

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
def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()

    winner = check_winner(cpu_choice, player_choice)

    print("the AI chose", cpu_choice)
    print("you chose", player_choice)
    return winner
player_wins = 0
cpu_wins = 0
ties = 0
while player_wins < 3 and cpu_wins < 3:
    winner = play_round()
    print(f"The result stored in \"winner\" is {winner}")

    if winner == "you win":
        player_wins += 1
    elif winner == "AI":
        cpu_wins += 1
    else:
        ties += 1
    print("score:")
    print("you WON", player_wins)
    print("AI won (do better):", cpu_wins)
    print("You both tied", ties)
    print()
if player_wins == 3:
    print("You won the tournament!")
else:
    print("the AI unfortunatly wins the tournament!")