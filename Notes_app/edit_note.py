#!/usr/bin/python3
def edit_notes():
    Notes = input("Enter file to be edited: ")
    if Notes != "":
        print("1.Want to add text after a line")
        print("2.Want to add text at the beginning")
        print("3.Want to add text at the end")
        print("4.Want to edit the entire file")
        print("5.Want to replace a line")
        print("6.Want to remove a line")
        choice = input("Enter action to be done on the file: ")

        try:
            with open(f"{Notes}.txt", "r+", encoding="utf-8") as new_notes:
                if choice == '1':
                    line = int(input("Line you want to add text after: "))
                    text = input("Enter the text you want to add: ")
                    lists = new_notes.readlines()
                    lists.insert(line, text + '\n')
                    new_notes.seek(0)#so move the pointer to the beginning
                    new_notes.writelines(lists)#write the edited info into the original file
                elif choice == '2':
                    line = 0
                    text = input("Enter text you want to add: ")
                    lists = new_notes.readlines()
                    lists.insert(line, text + '\n')
                    new_notes.seek(0)
                    new_notes.writelines(lists)
                elif choice == '3':
                    text = input("Enter text you want to add: ")
                    lists = new_notes.readlines()
                    lists.append(text + '\n')
                    new_notes.seek(0)
                    new_notes.writelines(lists)
                elif choice == '4':
                    print("Enter text you want to add: ")
                    edited_lines = []
                    while True:
                        line = input()
                        if line == "":
                            break
                        edited_lines.append(line + '\n')
                    new_notes.seek(0)
                    new_notes.writelines(edited_lines)
                    new_notes.truncate()
                elif choice == '5':
                    line = int(input("Enter line you want to replace: "))
                    text = input(f"Enter text you want to replace line {line} with: ")
                    lists = new_notes.readlines()
                    if line >= 1 and line <= len(lists):
                        lists[line - 1] = text + '\n'
                        new_notes.seek(0)
                        new_notes.writelines(lists)
                        new_notes.truncate()
                elif choice == '6':
                    line = int(input("Enter line you want to remove: "))
                    lists = new_notes.readlines()
                    if line >= 1 and line <= len(lists):
                        lists[line - 1] = ""
                        new_notes.seek(0)
                        new_notes.writelines(lists)
                        new_notes.truncate()
                else:
                    print("Invalid entry")

        except FileNotFoundError as error:
            print(f"{Notes} file doesnt exist")
