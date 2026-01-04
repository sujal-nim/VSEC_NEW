# Student Result Management System
# Uses if-else, loops, functions, and user input

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 40:
        status = "PASS"
    else:
        status = "FAIL"

    grade = calculate_grade(percentage)
    return total, percentage, grade, status


print("===== STUDENT RESULT MANAGEMENT SYSTEM =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

subjects = ["Maths", "Science", "English", "Computer", "AI"]
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    
    if mark < 0 or mark > 100:
        print("Invalid marks! Please enter between 0 and 100")
        mark = int(input(f"Re-enter marks for {subject}: "))
    
    marks.append(mark)

total, percentage, grade, status = calculate_result(marks)

print("\n===== RESULT =====")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total      :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
print("Status     :", status)

if status == "PASS":
    print("Congratulations! You have passed ")
else:
    print("Better luck next time ")

