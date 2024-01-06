# Pig game. Multiplayer game. Roll a die, whatever number you roll besides a 1
# will be added to your score. When you roll a 1 your turn is done and score 
# is removed. Every roll is gamble. Decide when you want to stop. Current points
# gets added to score. Max score is 50.

# Generate random number
import random

# define a function, a reusable block of code
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid number of players, try again")

# Generate empty list for scores
max_score = 50
player_scores = [0 for _ in range(players)]

# Simulates the turns
while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

# Show the winning player and score
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player player", winning_idx + 1, "is the winner with a score of:", max_score)