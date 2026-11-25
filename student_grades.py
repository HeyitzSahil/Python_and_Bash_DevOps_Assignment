students = {
    "Alice": 'B',
    "Bob": 'A',
    "Charlie": 'C',
    "David": 'B'
}

def get_student_grade(name):
    if name in students:
        print(f"{name}'s grade is: {students[name]}")
    else:
        print(f"{name} is not in the student list.")

def update_student_grade(name, grade):
    if name in students:
        students[name] = grade
        print(f"{name}'s grade has been updated to: {grade}")
    else:
        print(f"{name} is not in the student list. Cannot update grade.")
def add_student(name, grade):
    if name not in students:
        students[name] = grade
        print(f"{name} has been added with grade: {grade}")
    else:
        print(f"{name} is already in the student list. Cannot add.")
def all_students():
    print("All students and their grades:")
    for name, grade in students.items():
        print(f"{name}: {grade}")
while True:

    option = int(input("Choose an option:\n1. Get Student Grade\n2. Update Student Grade\n3. Add Student\n4. List All Students\n5. Exit\nEnter option (1-5): "))

    if option == 1:
        name = input("Enter student name: ")
        name = name.capitalize()
        get_student_grade(name)
    elif option == 2:
        name = input("Enter student name: ")
        name = name.capitalize()
        grade = input("Enter new grade (A-F): ").upper()
        update_student_grade(name, grade)
    elif option == 3:
        name = input("Enter student name: ")
        name = name.capitalize()
        grade = input("Enter grade (A-F): ").upper()
        add_student(name, grade)
    elif option == 4:
        all_students()
    elif option == 5:
        print("Exiting the program.......")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")