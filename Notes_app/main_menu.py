#!/usr/bin/python3
from new_notes import new_notes


def main_menu():
    """
    main_menu:the notes app main menu
    """

    print("Main Menu of Notes app")
    print("1.Take new notes")
    Choice = input("Enter option:")

    if Choice == '1':
        new_notes()

    else:
        print("Invalid option")


if __name__ == "__main__":
    main_menu()
