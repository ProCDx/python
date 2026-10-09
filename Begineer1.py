 
def get_choices():
    player_choice=input("Enter your choice(rock,paper,scissor)")
    computer_choice="paper"
    choices={"player":player_choice,"computer":computer_choice}
    return choices

choices=get_choices()
print(choices)

dict={"name":"player","shape":choices}