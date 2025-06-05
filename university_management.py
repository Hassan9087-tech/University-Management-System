
import json
import os

STUDENTS_FILE = "students.json"
COURSES_FILE = "courses.json"

def load_data(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    students = load_data(STUDENTS_FILE)
    student = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Student Name: "),
        "department": input("Enter Department: "),
        "courses": []
    }
    students.append(student)
    save_data(STUDENTS_FILE, students)
    print("✅ Student added successfully!")

def view_students():
    students = load_data(STUDENTS_FILE)
    if not students:
        print("📭 No students found.")
        return
    for s in students:
        print(f'ID: {s["id"]}, Name: {s["name"]}, Department: {s["department"]}, Courses: {", ".join(s["courses"])}')

def delete_student():
    sid = input("Enter Student ID to delete: ")
    students = load_data(STUDENTS_FILE)
    new_students = [s for s in students if s["id"] != sid]
    if len(new_students) != len(students):
        save_data(STUDENTS_FILE, new_students)
        print("🗑️ Student deleted.")
    else:
        print("❌ Student not found.")

def add_course():
    courses = load_data(COURSES_FILE)
    course = {
        "code": input("Enter Course Code: "),
        "name": input("Enter Course Name: "),
        "credit_hours": input("Enter Credit Hours: ")
    }
    courses.append(course)
    save_data(COURSES_FILE, courses)
    print("✅ Course added!")

def view_courses():
    courses = load_data(COURSES_FILE)
    if not courses:
        print("📭 No courses found.")
        return
    for c in courses:
        print(f'Code: {c["code"]}, Name: {c["name"]}, Credit Hours: {c["credit_hours"]}')

def delete_course():
    code = input("Enter Course Code to delete: ")
    courses = load_data(COURSES_FILE)
    new_courses = [c for c in courses if c["code"] != code]
    if len(new_courses) != len(courses):
        save_data(COURSES_FILE, new_courses)
        print("🗑️ Course deleted.")
    else:
        print("❌ Course not found.")

def assign_course_to_student():
    students = load_data(STUDENTS_FILE)
    courses = load_data(COURSES_FILE)

    sid = input("Enter Student ID: ")
    student = next((s for s in students if s["id"] == sid), None)
    if not student:
        print("❌ Student not found.")
        return

    code = input("Enter Course Code to assign: ")
    if any(c["code"] == code for c in courses):
        if code not in student["courses"]:
            student["courses"].append(code)
            save_data(STUDENTS_FILE, students)
            print("📘 Course assigned!")
        else:
            print("⚠️ Course already assigned.")
    else:
        print("❌ Course not found.")

def menu():
    while True:
        print("\n--- University Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Add Course")
        print("5. View Courses")
        print("6. Delete Course")
        print("7. Assign Course to Student")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            add_course()
        elif choice == '5':
            view_courses()
        elif choice == '6':
            delete_course()
        elif choice == '7':
            assign_course_to_student()
        elif choice == '8':
            print("👋 Exiting system. Shukriya!")
            break
        else:
            print("❌ Invalid choice. Try again.")

menu()
