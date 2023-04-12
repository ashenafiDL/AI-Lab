import tkinter as tk
import random

# define global variables
machine_score = 0
your_score = 0

# define function for game logic
def play_game(user_action):
    global machine_score, your_score
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        result = "It's a tie!"
    elif user_action == "rock": 
        if computer_action == "scissors":
            result = "You win! Rock smashes scissors."
            your_score += 1
        else:
            result = "You lose! Paper covers rock." 
            machine_score += 1
    elif user_action == "paper":
        if computer_action == "rock":
            result = "You win! Paper covers rock."
            your_score += 1
        else:
            result = "You lose! Scissors cuts paper."
            machine_score += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            result = "You win! Scissors cuts paper."
            your_score += 1
        else:
            result = "You lose! Rock smashes scissors."
            machine_score += 1
    
    return "You chose: " + user_action + "\nComputer chose: " + computer_action + "\n" + result

# define function for button click
def button_click():
    # get user input
    user_input = entry.get().strip().lower()
    if user_input == "":
        output.delete('1.0', tk.END)
        output.insert(tk.END, "Invalid input! \nPlease enter 'rock', 'paper', or 'scissors'." + "\n")
        return
    # clear text entry box
    entry.delete(0, tk.END)
    # update game output
    output.delete('1.0', tk.END)
    try:
        output.insert(tk.END, play_game(user_input) + "\n")
    except ValueError:
        output.insert(tk.END, "Invalid input! \nPlease enter 'rock', 'paper', or 'scissors'." + "\n")
    # update score
    score.delete('1.0', tk.END)
    score.insert(tk.END, "Machine: " + str(machine_score) + "     You: " + str(your_score))

# set up main window
root = tk.Tk()
root.title("Paper-Scissors-Rock Game")

# create label and entry for user input
label = tk.Label(root, text="Choose 'rock', 'paper', or 'scissors':")
label.pack(pady=10)
entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.pack()

# create button for submitting user input
button = tk.Button(root, text="Submit", command=button_click, font=('Arial', 14))
button.pack(pady=10)

# create label for game output
output_label = tk.Label(root, text="Game output:")
output_label.pack(pady=10)

# create text box for game output
output = tk.Text(root, height=5, width=30, font=('Arial', 14))
output.pack()

# create label for score
score_label = tk.Label(root, text="Score:")
score_label.pack(pady=10)

# create text box for score
score = tk.Text(root, height=1, width=30, font=('Arial', 14))
score.pack()

# start main loop
root.mainloop()
