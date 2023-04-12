import random


def get_inputs():
    """A function to accept user input and randomly generated pc choice
    :returns: Letters representing user and pc choices
    """
    alternatives = ['r', 'p', 's']

    user_choice = input("\nEnter your choice (r, p, s): ")

    if user_choice not in ["r", "p", "s", "="]:
        print("Invalid input")
        return get_inputs()
    pc_choice = random.choice(alternatives)

    return user_choice, pc_choice


def compare(user, pc):
    """A function to determine who wins or loses the round
    :param user: The choice of the user
    :param pc: The choice of the computer
    :returns: 0 if draw occurred, 1 if user wins, -1 if computer wins
    """
    if user == pc:
        return 0  # draw
    elif user == "r":
        if pc == "s":  # rock vs scissors
            return 1
        elif pc == "p":  # rock vs paper
            return -1
    elif user == "p":
        if pc == "r":  # paper vs rock
            return 1
        elif pc == "s":  # paper vs scissors
            return -1
    elif user == "s":
        if pc == "r":  # scissors vs rock
            return -1
        elif pc == "p":  # scissors vs paper
            return 1


def main():
    count = {"Wins": 0, "Loses": 0, "Draw": 0}

    while True:
        user_choice, pc_choice = get_inputs()

        if user_choice is "=":
            break

        res = ""
        match compare(user_choice, pc_choice):
            case -1:
                res = "You lose"
                count["Loses"] += 1
            case 0:
                res = "Draw"
                count["Draw"] += 1
            case 1:
                res = "You win"
                count["Wins"] += 1
        print(f"{user_choice} VS {pc_choice} => {res}")

    total = count["Wins"] + count["Loses"] + count["Draw"]

    print("=====================")
    print(f"Total rounds: {total}")
    for k, v in count.items():
        percentage = round(((v / total) * 100), 2)
        print(f"{k}: {v} ({percentage}%)")
    print("=====================")


if __name__ == "__main__":
    print("====================================")
    print("Welcome to rock paper scissors game.")
    print("Type '=' if you want to exit.")
    print("====================================")

    main()
