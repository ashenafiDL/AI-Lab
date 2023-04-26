"""A text analyzer program that analyzes text files and
prints out the number of words, characters, and lines of text
"""
from word_frequency import word_frequency
from clean_text import clean_text
from character_frequency import character_frequency
from statistics import statistics


def menu():
    choice = None

    while choice != 0:
        print("1. Word Frequency")
        print("2. Character Frequency")
        print("3. Statistical Information")

        try:
            choice = int(input("\nEnter your choice: "))
        except (TypeError, ValueError):
            print("Invalid choice")
            menu()

        match choice:
            case 1:
                word_frequency()
            case 2:
                character_frequency()
            case 3:
                statistics()
            case 0:
                exit()
            case _:
                print("Invalid choice")
                menu()


if __name__ == "__main__":
    print("====================================")
    print("Welcome to the text analyzer program")
    print("====================================")

    while True:
        menu()
