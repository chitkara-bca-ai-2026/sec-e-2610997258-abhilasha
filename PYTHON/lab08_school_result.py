# Lab 08 - School Result Processing

print("========================================")
print("       SCHOOL RESULT PROCESSING         ")
print("========================================")
student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number  : ")
print("\n--- Enter Marks for 5 Subjects (0-100) ---")
marks = []
has_failed_subject = False

for i in range(1, 6):
    while True:
        mark = float(input(f"Enter marks for Subject {i}: "))
        if 0 <= mark <= 100:
            marks.append(mark)
            if mark < 40:
                has_failed_subject = True
            break
        else:
            print("Error: Marks must be between 0 and 100. Please try again.")
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
if has_failed_subject:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    else:
        grade = "E"
        remarks = "Pass"
print("\n" + "=" * 40)
print("          STUDENT REPORT CARD           ")
print("========================================")
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("-" * 40)
print(f"Total Marks  : {total_marks} / 500.0")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remarks}")
print("========================================")