def search_keyword(filename, keyword):
    matches = []
    total_count = 0
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                matches.append((line_number, line.strip()))
                total_count += line.lower().count(keyword.lower())
    for number, line in matches:
        print(f"Line {number}: {line}")
    print("\nTotal occurrences:", total_count)
def display_document(filename):
    with open(filename, "r") as file:
        print("\n========== FULL REPORT ==========")
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number}: {line}", end="")
filename = "report.txt"
import os
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Manual Technology and AI Progress Report.\n")
        file.write("The adoption of Artificial Intelligence accelerated across business units.\n")
        file.write("AI algorithms improved diagnostic accuracy in healthcare operations.\n")
        file.write("Data engineering pipelines were upgraded to support real-time data streaming.\n")
        file.write("The company plans further investments in AI research and machine learning.")
while True:
    print("\n========== KEYWORD SEARCH UTILITY ==========")
    print("\nSelect an operation:")
    print("1. Search Keyword in Document")
    print("2. View Full Document")
    print("3. Exit")
    choice = input("\nEnter choice (1-3): ")
    if choice == "1":
        keyword = input("Enter keyword to search: ")
        try:
            if keyword == "":
                print("Please enter a valid keyword.")
            else:
                search_keyword(filename, keyword)
        except FileNotFoundError:
            print("Error: Document not found!")
    elif choice == "2":
        try:
            display_document(filename)
        except FileNotFoundError:
            print("Error: Document not found!")
    elif choice == "3":
        print("Thank you for using Keyword Search Utility. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 3.")