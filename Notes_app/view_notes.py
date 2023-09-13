#!/usr/bin/python3
def view_notes():
    Notes = input("Notes to open: ")
    try:
        with open(f"{Notes}.txt", "r", encoding="utf-8") as notes_now:
            content = notes_now.read()
            print(f"  {Notes}  \n{content}")
    except FileNotFoundError as error:
        print(f"{Notes} file doesnt exist")
