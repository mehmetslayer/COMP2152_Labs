import random

def main():

    choices = ["Rock", "Paper", "Scissors"]

    playerChoice = input("Enter a number between 1 to 3 for the following choices: 1-Rock, 2-Paper, 3-Scissors: ")

    playerChoice = int(playerChoice)

    if playerChoice < 1 or playerChoice > 3:
        print("Error: Choice should be between 1 to 3! ")

        # Develop the game logic using if/elif/else

    computerChoice = random.randint(1,3)

    if playerChoice > computerChoice:
        print("User won")
    elif playerChoice < computerChoice:
        print("Computer won")
    else:
        print("It's a tie")

main()
