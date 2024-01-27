import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Global variable to track the player's score
player_score = 0

def introduction():
    print(Fore.GREEN + "Welcome to the Python Adventure!")
    time.sleep(1)
    
    # Request player name
    player_name = input(Fore.YELLOW + "What's your name? ")
    
    print(Fore.CYAN + f"Hello, {player_name}! You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Make choices to navigate through the adventure.")
    time.sleep(1)

def make_choice(question, options, score_change):
    print(Fore.WHITE + Style.BRIGHT + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input(Fore.CYAN + "Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                # Update the global score variable
                global player_score
                player_score += score_change[choice - 1]
                return choice
            else:
                print(Fore.RED + "Invalid choice. Try again.")
        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number.")

def forest_path():
    print(Fore.WHITE + Style.BRIGHT + "You come across a fork in the path.")
    time.sleep(1)
    choice = make_choice("Which path do you take?", ["Go left", "Go right"], [1, -1])

    if choice == 1:
        print(Fore.GREEN + "You encounter a friendly squirrel. It leads you to safety.")
    else:
        print(Fore.RED + "Oh no! You stumble into a spider web and get trapped.")

def mountain_climb():
    print(Fore.WHITE + Style.BRIGHT + "You reach a steep mountain. What do you do?")
    time.sleep(1)
    choice = make_choice("How do you climb it?", ["Use a rope", "Climb without equipment"], [1, -1])

    if choice == 1:
        print(Fore.GREEN + "Smart choice! The rope helps you climb safely.")
    else:
        print(Fore.RED + "Uh-oh! Climbing without equipment is risky. You slip, but luckily, you catch yourself.")

def mystical_cave():
    print(Fore.WHITE + Style.BRIGHT + "You discover a mystical cave filled with glowing crystals.")
    time.sleep(1)
    choice = make_choice("What do you do?", ["Enter the cave", "Continue on your journey"], [1, 0])

    if choice == 1:
        print(Fore.GREEN + "The cave is enchanted! You gain magical powers.")
    else:
        print(Fore.YELLOW + "You decide to continue your journey.")

def river_crossing():
    print(Fore.WHITE + Style.BRIGHT + "You reach a wide river blocking your way.")
    time.sleep(1)
    choice = make_choice("How do you cross it?", ["Build a raft", "Swim across"], [1, -1])

    if choice == 1:
        print(Fore.GREEN + "Great idea! You successfully build a raft and cross the river.")
    else:
        print(Fore.RED + "Oh no! Swimming across was a bad idea. You struggle but manage to reach the other side.")

def hidden_treasure():
    print(Fore.WHITE + Style.BRIGHT + "You stumble upon a hidden treasure chest.")
    time.sleep(1)
    choice = make_choice("What do you do?", ["Open the chest", "Leave it alone"], [1, -1])

    if choice == 1:
        print(Fore.GREEN + "Congratulations! You find valuable treasures inside the chest.")
    else:
        print(Fore.YELLOW + "You decide to leave the chest untouched.")

# Display the final score
def display_score():
    print(Fore.WHITE + Style.BRIGHT + f"\nYour adventure is complete! Your total score is: {player_score}")

# Main game loop
def play_game():
    introduction()

    # Start of the adventure
    forest_path()

    # Continue the adventure based on previous choices
    mountain_climb()

    # More sections
    mystical_cave()
    river_crossing()
    hidden_treasure()

    # Display final score
    display_score()

if __name__ == "__main__":
    play_game()
