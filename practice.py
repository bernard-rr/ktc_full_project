# Import dependencies
# A dependency is a library or module that our code needs to function.

import time # to make the code interactive
from colorama import Fore, Style, init # color text on the terminal

# launch colorama 
init(autoreset=True)

player_score = 0

# def introduction():
#     # Welcome the player
#     print(Fore.GREEN+"Welcome to the Python Adventure")
#     time.sleep(1)

#     player_name = input(Fore.YELLOW + "What's your name?")
#     print(Fore.CYAN + f"Hello {player_name}!!! You find yourself in a mysterious Forest")

#     print("Make choices to navigate through the adventure")
#     time.sleep(1)

# show = introduction()

def make_choice(question, options, score_change):
    print(Fore.WHITE + Style.BRIGHT + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(Fore.CYAN + input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                # Update global score variable
                global player_score
                player_score += score_change[choice - 1]
                return choice
            else:
                print(Fore.RED + "Invalid choice. Try again")
        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number.")





make_choice("What is your favorite fruit", ["apple", "mango", "banana", "orange"], [1, -1])


