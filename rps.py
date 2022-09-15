# A rock-paper scissors game with the computer

import random

def play():

    # Computer chooses and user enters their choice
    choices = ["r", "p", "s"]
    cpu_choice = random.choice(choices)
    your_choice = input("Enter your choice: r, p, s\n")

    # Ensure valid choice
    while your_choice not in choices:
        your_choice = input("Try a new input: ")

    # Tie
    if your_choice == cpu_choice:
        print(f"tie: {cpu_choice} vs {your_choice}")
    # Lose 
    elif your_choice == 'r' and cpu_choice == 'p' or your_choice == 'p' and cpu_choice == 's' or your_choice == 's' and cpu_choice == 'r':
        print(f'you lose! {cpu_choice} vs {your_choice}')
    # W
    else:
        print(f'you win! {cpu_choice} vs {your_choice}')

# Play game until the user decides not to.
start = 'y'
while start == 'y':
    play()
    start = input("Play again? y/n\n").lower()
    while start != 'y' and start != 'n':
        start = input("Invalid option. Try again: y/n?\n")

print('Thanks for playing!')