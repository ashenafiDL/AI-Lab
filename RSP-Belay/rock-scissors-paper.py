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
def button_click(user_input):
    global machine_score, your_score
    # update game output
    output.delete('1.0', tk.END)
    try:
        output.insert(tk.END, play_game(user_input) + "\n")
    except ValueError:
        output.insert(tk.END, "Invalid input! \nPlease press 'rock', 'paper', or 'scissors'." + "\n")
    # update score
    score.delete('1.0', tk.END)
    score.insert(tk.END, "Machine: " + str(machine_score) + "          You: " + str(your_score))

# set up main window
root = tk.Tk()
root.title("ROCK-PAPER-SCISSORS GAME")

# define colors
bg_color = "#ADD8E6"
button_color = "#FFFFFF"
text_color = "#000000"

# set window background color
root.config(bg=bg_color)

# create label for user input
label = tk.Label(root, text="   ROCK-PAPER-SCISSORS GAME   ", bg=bg_color, fg=text_color, font=('Arial', 18))
label.pack(pady=10)

# create buttons for rock, paper, and scissors
rock_button = tk.Button(root, text="Rock", bg="teal", fg=text_color, font=('Arial', 14), command=lambda: button_click("rock"))
rock_button.pack(side="bottom", padx=10, pady=10, expand=True, fill='both')

paper_button = tk.Button(root, text="Paper", bg="teal", fg=text_color, font=('Arial', 14), command=lambda: button_click("paper"))
paper_button.pack(side="bottom", padx=10, pady=10, expand=True, fill='both')

scissors_button = tk.Button(root, text="Scissors", bg="teal", fg=text_color, font=('Arial', 14), command=lambda: button_click("scissors"))
scissors_button.pack(side="bottom", padx=10, pady=10, expand=True, fill='both')
 
# create text box for score
score = tk.Text(root, height=1, width=30, font=('Arial', 14))
score.pack()
score.insert(tk.END, "Machine: 0            You: 0")

# create label for game output 
output_label = tk.Label(root, text="Game output:", bg=bg_color, fg=text_color, font=('Arial', 18))
output_label.pack(pady=20)

# create text box for game output
output = tk.Text(root, height=5, width=30, font=('Arial', 14))
output.pack()

# start main loop
root.mainloop()