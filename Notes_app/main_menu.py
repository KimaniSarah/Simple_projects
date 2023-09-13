#!/usr/bin/python3
from new_notes import new_notes
from view_notes import view_notes
from edit_note import edit_notes

def main_menu():
    """
    main_menu:the notes app main menu
    """

    print("Main Menu of Notes app")
    print("1.Take new notes")
    print("2.View existing notes")
    print("3.Edit the notes")

    Choice = input("Enter option:")

    if Choice == '1':
        new_notes()

    elif Choice == '2':
        view_notes()

    elif Choice == '3':
        edit_notes()

    else:
        print("Invalid option")


if __name__ == "__main__":
    main_menu()
