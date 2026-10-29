from random import choice
 
choices = ("rock", "paper", "scissors")
beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}
player_score = 0
computer_score = 0
 
while True:
    player = input("rock, paper, scissors, or quit: ").strip().lower()
 
    if player == "quit":
        print(f"Final score: you {player_score}, computer {computer_score}.")
        break
    if player not in choices:
        print("Choose rock, paper, scissors, or quit.")
        continue
 
    computer = choice(choices)
    print(f"Computer chose {computer}.")
 
    if player == computer:
        print("Draw.")
    elif beats[player] == computer:
        player_score += 1
        print("You win this round.")
    else:
        computer_score += 1
        print("Computer wins this round.")