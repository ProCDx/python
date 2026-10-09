 
import random


def get_choices():
    player_choice=input("Enter your choice(rock,paper,scissor)")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    print(check_win(player_choice,computer_choice))
    

def check_win(player,computer):
    print(f"You chose: {player} , computer chose: {computer}")
    if player==computer:
        return "its a tie"
    elif player=="rock":
        if computer=="paper":
            return "You lose."
        else:
            return "you win!"
    elif player=="paper":
        if computer=="scissor":
            return "You lose."
        else:
            return "You win!"
    elif player=="scissor":
        if computer=="rock":
            return "You lose."
        else:
            return "You win!"
get_choices()
    