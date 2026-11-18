def write_notes(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("Notes successfully saved to", filename)
def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
        return content
    else:
        return None
import os
while True:
    print("\n====== STUDENT NOTES MANAGEMENT SYSTEM ======")
    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")
    choice = input("\nEnter choice (1-3): ")
    if choice == "1":
        content = input("Enter notes to save: ")
        write_notes("notes.txt", content)
    elif choice == "2":
        notes = read_notes("notes.txt")
        if notes is not None:
            print("\n----- Saved Notes -----")
            print(notes)
        else:
            print("No notes file found. Please save notes first.")
    elif choice == "3":
        print("Thank you for using Student Notes Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 3.")