import random


def get_cpu_choice():
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    return cpu_choice


def get_player_choice():
    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower

        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice


def check_winner(cpu_choice, player_choice):
    if player_choice == cpu_choice:
        winner = "Tie"

    elif cpu_choice == "rock":
        if player_choice == "paper":
            winner = "PLAYER"
        else:
            winner = "CPU"

    elif cpu_choice == "paper":
        if player_choice == "scissors":
            winner = "PLAYER"
        else:
            winner = "CPU"

    elif player_choice == "paper":
        winner = "CPU"

    else:
        winner = "PLAYER"

    return winner


def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()

    winner = check_winner(cpu_choice, player_choice)

    print("CPU chose:", cpu_choice)
    print("Winner:", winner)

    return winner


# Keep track of the score
player_wins = 0
cpu_wins = 0
ties = 0


# Tournament continues until someone gets 3 wins
while player_wins < 3 and cpu_wins < 3:

    winner = play_round()

    if winner == "PLAYER":
        player_wins += 1

    elif winner == "CPU":
        cpu_wins += 1

    else:
        ties += 1

    print("Score:")
    print("Player:", player_wins)
    print("CPU:", cpu_wins)
    print("Ties:", ties)
    print()


# Display the overall winner
if player_wins == 3:
    print("PLAYER wins the tournament!")

else:
    print("CPU wins the tournament!")