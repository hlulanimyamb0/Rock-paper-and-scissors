from random import choice
from time import sleep

# scores
player_score: int = 0
computer_score: int = 0

# rules
print(
    """
    Rules:
    1. You can choose either r or rock for ROCK, p or paper for PAPER, s or scissors for SCISSORS.
    2. if you want to quit type q or quit or QUIT.
    3. If you type anything that is not specified here you will get a message telling you that you \n       chose a wrong option hence chose a different option.
    """
)

# main function
sleep(3)
def main() -> None:
    # The preferred name from the user
    player_username: str = str(input("Enter a username:\n"))
    global player_score
    global computer_score
    sleep(1)
    # greetings.
    print(f"Hello, {player_username}.")
    sleep(2)
    # loop for the game
    while True:
        # computer choice
        options: list[str] = ["rock", "paper", "scissors"]
        computer_choice: str = choice(options)

        # player choice
        player_choice: str = str(input("\nChoose your option:\n").lower())
        if player_choice in ['q', 'quit']:
            # player wins by over all score
            if player_score > computer_score:
                print(f"By the overall score,{player_username} wins. {player_score} : {computer_score}.")
                break
            # computer wins by over all score
            else:
                print(f"The computer wins by {computer_score} where as {player_username} have {player_score}.")
                break
        # when the user chooses the wrong option
        elif player_choice not in ['s', 'scissors', 'r', 'rock', 'p', 'paper']:
            sleep(1)
            print("Wrong choice!!\nYou chose valid options...")
            sleep(1)
            print("Note: You can type rock instead of r, scissors instead of s and paper instead of p.")
            sleep(4)
        else:
            # draw
            if (player_choice in ['s', 'scissors'] and computer_choice == 'scissors') or (
                    player_choice in ['p', 'paper'] and computer_choice == 'paper') or (
                    player_choice in ['r', 'rock'] and computer_choice == 'rock'):
                print(f"You both chose {player_choice}.\nDraw!!")
            # player wins
            elif (player_choice in ['r', 'rock'] and computer_choice == 'scissors') or (
                    player_choice in ['p', 'paper'] and computer_choice == 'rock') or (
                    player_choice in ['s', 'scissors'] and computer_choice == 'paper'):
                print(f"The computer chose {computer_choice}.\n{player_username} wins!!")
                player_score += 1

            # computer wins
            else:
                print(f"The computer chose {computer_choice}.\nTherefore the computer wins!!")
                computer_score += 1
        # over all score tracker
        print(f"\nSCORE:\n{player_username}: {player_score} vs Computer: {computer_score}")
        continue

if __name__ == '__main__':
    main()