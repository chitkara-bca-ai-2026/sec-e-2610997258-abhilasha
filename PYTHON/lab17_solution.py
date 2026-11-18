students = {
    "101": {
        "Name": "Aman",
        "Marks": [85, 90, 78]
    },

    "102": {
        "Name": "Riya",
        "Marks": [92, 95, 88]
    },

    "103": {
        "Name": "Karan",
        "Marks": [75, 80, 85]
    }
}
def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)

    return total, average
def display_student(roll, student):
    name = student["Name"]
    marks = student["Marks"]
    total, average = calculate_results(marks)
    print(
        f"Roll No: {roll} | "
        f"Name: {name} | "
        f"Marks: {marks} | "
        f"Total: {total} | "
        f"Average: {average:.2f}%"
    )
def add_student(records, roll, name, marks):
    if roll in records:
        print("Error: Roll number already exists!")
    else:
        records[roll] = {
            "Name": name,
            "Marks": marks
        }
        print("Student added successfully!")
while True:
    print("\n===== STUDENT RECORDS MANAGEMENT SYSTEM =====")
    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")
    choice = input("\nEnter choice (1-4): ")
    if choice == "1":
        print("\n===== ALL STUDENT RECORDS =====")
        if len(students) == 0:
            print("No student records available.")
        else:
            for roll, student in students.items():
                display_student(roll, student)
    elif choice == "2":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = []
        for i in range(3):
            mark = int(input(f"Enter marks for subject {i+1}: "))
            marks.append(mark)
        add_student(students, roll, name, marks)
    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        if student:
            print("\nStudent Found:")
            display_student(roll, student)
        else:
            print("Student not found!")
    elif choice == "4":
        print("Thank you for using Student Records Management System!")
        break
    else:
        print("Invalid choice! Please select between 1 and 4.")