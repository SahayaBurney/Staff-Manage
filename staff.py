import json
from datetime import datetime

# File to store teacher records
FILE_NAME = "teachers.json"


# Function to load existing data from file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Function to display all teachers
def show_all_teachers():
    data = load_data()
    if not data:
        print("No teachers found.")
    else:
        for teacher in data:
            print_teacher_details(teacher)

# Function to add a new teacher
def add_teacher():
    full_name = input("Enter full name of the teacher: ")
    age = int(input("Enter age: "))
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    classes = int(input("Enter number of classes taught: "))

    data = load_data()
    new_teacher = {
        "Full Name": full_name,
        "Age": age,
        "Date of Birth": dob,
        "Number of Classes": classes
    }
    data.append(new_teacher)
    save_data(data)
    print("Teacher added successfully.")

# Function to display teacher details
def print_teacher_details(teacher):
    print("\nFull Name:", teacher["Full Name"])
    print("Age:", teacher["Age"])
    print("Date of Birth:", teacher["Date of Birth"])
    print("Number of Classes:", teacher["Number of Classes"])

# Function to filter teachers by age
def filter_by_age():
    age = int(input("Enter age to filter by: "))
    data = load_data()
    filtered_teachers = [teacher for teacher in data if teacher["Age"] == age]
    if not filtered_teachers:
        print("No teachers found with that age.")
    else:
        for teacher in filtered_teachers:
            print_teacher_details(teacher)

# Function to search for a teacher by name
def search_teacher():
    name = input("Enter the full name of the teacher to search: ")
    data = load_data()
    found = False
    for teacher in data:
        if teacher["Full Name"].lower() == name.lower():
            print("Teacher found:")
            print_teacher_details(teacher)
            found = True
            break
    if not found:
        print("Teacher not found.")

# Function to update a teacher's record
def update_teacher():
    name = input("Enter the full name of the teacher to update: ")
    data = load_data()
    updated = False
    for teacher in data:
        if teacher["Full Name"].lower() == name.lower():
            print("Teacher found. Please provide updated information:")
            full_name = input("Enter full name of the teacher: ")
            age = int(input("Enter age: "))
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            classes = int(input("Enter number of classes taught: "))

            teacher["Full Name"] = full_name
            teacher["Age"] = age
            teacher["Date of Birth"] = dob
            teacher["Number of Classes"] = classes
            updated = True
            break
    if updated:
        save_data(data)
        print("Teacher record updated successfully.")
    else:
        print("Teacher not found.")

# Function to delete a teacher's record
def delete_teacher():
    name = input("Enter the full name of the teacher to delete: ")
    data = load_data()
    deleted = False
    for teacher in data:
        if teacher["Full Name"].lower() == name.lower():
            data.remove(teacher)
            deleted = True
            break
    if deleted:
        save_data(data)
        print("Teacher record deleted successfully.")
    else:
        print("Teacher not found.")

# Function to calculate and display the average number of classes
def display_average_classes():
    data = load_data()
    total_classes = sum(teacher["Number of Classes"] for teacher in data)
    if data:
        average = total_classes / len(data)
        print(f"The average number of classes taken by teachers: {average}")
    else:
        print("No teachers found.")
#
def filter_by_classes():
    classes = int(input("Enter number of classes to filter by: "))
    data = load_data()
    filtered_teachers = [teacher for teacher in data if teacher["Number of Classes"] == classes]
    if not filtered_teachers:
        print("No teachers found with that number of classes.")
    else:
        for teacher in filtered_teachers:
            print_teacher_details(teacher)

# Updated main menu to include new functionalities
def main_menu():
    while True:
        print("\nTeacher Management Application")
        print("1. Show all teachers")
        print("2. Add a teacher")
        print("3. Filter teachers by age")
        print("4. Filter teachers by number of classes")
        print("5. Search for a teacher")
        print("6. Update a teacher's record")
        print("7. Delete a teacher")
        print("8. Display average number of classes")
        print("9. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            show_all_teachers()
        elif choice == "2":
            add_teacher()
        elif choice == "3":
            filter_by_age()
        elif choice == "4":
            filter_by_classes()
        elif choice == "5":
            search_teacher()
        elif choice == "6":
            update_teacher()
        elif choice == "7":
            delete_teacher()
        elif choice == "8":
            display_average_classes()
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()


# Main menu
def main_menu():
    while True:
        print("\nTeacher Management Application")
        print("1. Show all teachers")
        print("2. Add a teacher")
        print("3. Filter teachers by age")
        print("4. Filter teachers by number of classes")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            show_all_teachers()
        elif choice == "2":
            add_teacher()
        elif choice == "3":
            filter_by_age()
        elif choice == "4":
            filter_by_classes()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()
