import random

# Define the possible moves
moves = ["rock", "paper", "scissors"]

# Get the user's move
user_move = input("Choose rock, paper, or scissors: ")

# Get the computer's move
computer_move = random.choice(moves)

# Display the moves
print("You chose:", user_move)
print("Computer chose:", computer_move)

# Determine the winner
if user_move == computer_move:
  print("It's a tie!")
elif user_move == "rock" and computer_move == "scissors":
  print("You win!")
elif user_move == "paper" and computer_move == "rock":
  print("You win!")
elif user_move == "scissors" and computer_move == "paper":
  print("You win!")
else:
  print("Computer wins!")
