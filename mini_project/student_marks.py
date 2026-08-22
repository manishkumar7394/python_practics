# count the number of students 

num_of_students = int(input("Enter the num :   "))

# Data Storage
student_data = []

# inserting_data
for i in range(num_of_students):
    print(f"Enter the data of student:  {i+1}")
    name = input("Name: ")
    roll_no = int(input("Roll Number: "))
    marks = int(input("Marks:   "))
    if marks >95:
        grades = "A"
    elif marks >85:
        grades = "B"
    elif marks >60:
        grades = "C"
    else:
        grades= "F"

    students = {
        "name"     :  name,
        "roll_no"  :  roll_no,
        "marks"    :  marks,
        "grades"   :  grades
    }

    student_data.append(students)

print("All students Data:\n")

for s in student_data:
    print(f"{s['name']} - roll_number : {s['roll_no']} - Marks: {s['marks']} - Grades : {s['grades']}")