def get_document_statistics(filename):
    with open(filename, "r") as file:
        content = file.read()
    line_count = len(content.splitlines())
    words = content.split()
    word_count = len(words)
    char_count = len(content)
    return line_count, word_count, char_count
def display_document(filename):
    with open(filename, "r") as file:
        line_number = 1
        for line in file:
            print(f"{line_number}: {line}", end="")
            line_number += 1
filename = "document.txt"
import os
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Artificial intelligence is transforming modern industries.\n")
        file.write("Python provides powerful libraries for text processing and data analysis.\n")
        file.write("Developers use file handling to store and retrieve important records.\n")
        file.write("Modular programming makes code clean, reusable, and easy to maintain.")
while True:
    print("\n========== DOCUMENT STATISTICS ANALYZER ==========")
    print("\nSelect an operation:")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")
    choice = input("\nEnter choice (1-3): ")
    if choice == "1":
        try:
            line_count, word_count, char_count = get_document_statistics(filename)
            print("\n========== DOCUMENT REPORT ==========")
            print("Target File:", filename)
            print("Total Lines:", line_count)
            print("Total Words:", word_count)
            print("Total Characters:", char_count)
        except FileNotFoundError:
            print("Error: Document file not found!")
    elif choice == "2":
        try:
            print("\n========== DOCUMENT PREVIEW ==========")
            display_document(filename)
        except FileNotFoundError:
            print("Error: Document file not found!")
    elif choice == "3":
        print("Thank you for using Document Statistics Analyzer. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 3.")