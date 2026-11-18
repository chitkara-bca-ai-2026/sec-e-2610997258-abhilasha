def append_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")
    print("New entry logged to", filename)
def display_log(filename):
    with open(filename, "r") as file:
        content = file.read()
    if content == "":
        print("No log entries available.")
    else:
        print("\n========== DAILY LOG BOOK ==========")
        entries = content.splitlines()
        for i, entry in enumerate(entries, start=1):
            print(f"[{i:02}] {entry}")
        print("\nTotal Logged Entries:", len(entries))
filename = "daily_log.txt"
with open(filename, "a") as file:
    pass
while True:
    print("\n========== OFFICE DAILY LOG BOOK ==========")
    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")
    choice = input("\nEnter choice (1-3): ")
    if choice == "1":
        entry = input("Enter log entry: ")
        append_entry(filename, entry)
    elif choice == "2":
        display_log(filename)
    elif choice == "3":
        print("Thank you for using the Daily Log Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 3.")