#!/usr/bin/python3
import os
def delete_notes():
    notes = input("Enter the file you want to delete: ")
    try:
        os.remove(f"{notes}.txt")
    except FileNotFoundError:
        print(f"{notes} file does not exist")
    except PermissionError:
        print(f"you do not have permission to delete {notes}")
    except Exception as error:
        print(f"{error} has occured")
