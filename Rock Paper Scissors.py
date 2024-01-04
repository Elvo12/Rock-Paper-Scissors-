import random

def play_game():
    print('Welcome to Rock, Paper, Scissors Game')

    Options = ['rock', "paper", "scissors"]

    Computer_turn = random.choice(Options)
    User_input = input("rock, paper or scissors?: ")
    if User_input not in Options:
        print("Please input one of the options provided")
        return
    else:
        print(f"Computer's move is: {Computer_turn}") 
             
    if User_input == Computer_turn:
        print("Its a draw")

    elif (User_input == 'rock' and Computer_turn == 'scissors') or \
    (User_input == 'paper' and Computer_turn == 'rock') or \
    (User_input == 'scissors' and Computer_turn == 'paper'): 
        print("You have won!!!")
    else:
        print("You have lost !!!")

play_game()
    