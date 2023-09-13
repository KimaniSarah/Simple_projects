#!/usr/bin/python3
def new_notes():
    """
    new_notes: this function takes new notes
    """
    Title = input("Enter the Title: ")
    if len(Title) > 30:
        raise ValueError("the title is too long")

    try:
        with open(f"{Title}.txt", "x"):
            pass
    except FileExistError:
        print("The file {Title} already exist")

    Body = []
    print("enter Notes and an empty line when done: ")
    while True:
        line = input()
        if line == "":
            break
        Body.append(line)

    if len(Body) > 500:
        raise ValueError("the Notes input is too long")

    with open(f"{Title}.txt", "w", encoding="utf-8") as notes:
        for line in Body:
            notes.write(line + '\n')

    print(f"{Title} was created successfully")
