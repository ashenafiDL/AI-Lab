"""A text analyzer program that analyzes text files and
prints out the number of words, characters, and lines of text
"""
from clean_text import clean_text


def menu():
    print("1. Word Frequency")
    print("2. Character Frequency")
    print("3. Statistical Information")

    choice = None

    try:
        choice = int(input("\nEnter your choice: "))
    except (TypeError, ValueError):
        print("Invalid choice")
        menu()

    match choice:
        case 1:
            # word_frequency()
            pass
        case 2:
            # character_frequency()
            pass
        case 3:
            # statistical_information()
            pass
        case _:
            print("Invalid choice")
            menu()


if __name__ == "__main__":
    print("====================================")
    print("Welcome to the text analyzer program")
    print("====================================")
    menu()
