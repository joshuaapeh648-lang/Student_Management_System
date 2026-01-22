import csv
import os

FILENAME = "students.csv"

def add_student():
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        course = input("Enter Student Course: ")
        writer.writerow([student_id, name, age, course])
    print("✅ Student added successfully!\n")

def view_students():
    if not os.path.exists(FILENAME):
        print("⚠️ No records found.\n")
        return
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        print("\n--- Student Records ---")
        for row in reader:
            print(row)
    print()

def search_student():
    student_id = input("Enter Student ID to search: ")
    found = False
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == student_id:
                print("🎯 Record found:", row)
                found = True
    if not found:
        print("❌ Student not found.\n")

def update_student():
    student_id = input("Enter Student ID to update: ")
    updated_rows = []
    found = False
    if not os.path.exists(FILENAME):
        print("⚠️ No records found.\n")
        return
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == student_id:
                found = True
                print("Current record:", row)
                name = input("Enter new name: ")
                age = input("Enter new age: ")
                course = input("Enter new course: ")
                updated_rows.append([student_id, name, age, course])
            else:
                updated_rows.append(row)

    if found:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("✅ Record updated successfully!\n")
    else:
        print("❌ Student not found.\n")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    updated_rows = []
    found = False
    if not os.path.exists(FILENAME):
        print("⚠️ No records found.\n")
        return
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != student_id:
                updated_rows.append(row)
            else:
                found = True

    if found:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("🗑️ Record deleted successfully!\n")
    else:
        print("❌ Student not found.\n")

def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting program... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
