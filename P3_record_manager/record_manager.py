students = []        # list: keeps the order I added the names
sections = set()     # set: keeps only unique section names


def add_student():
    name = input("Student name: ").strip().title()
    section = input("Section (e.g. IV-BSIT A): ").strip().upper()
    if name in students:
        print("That student is already in the list.")
        return
    students.append(name)
    sections.add(section)
    print(f"{name} was added.")


def remove_student():
    name = input("Name to remove: ").strip().title()
    if name in students:
        students.remove(name)
        print(f"{name} was removed.")
    else:
        print("Student not found.")


def show_students():
    if len(students) == 0:
        print("The list is empty.")
        return
    print("\nStudents (A-Z):")
    for number, name in enumerate(sorted(students), start=1):
        print(f"{number}. {name}")
    print("Total students:", len(students))


def show_sections():
    print("\nUnique sections:", sorted(sections))


def compare_groups():
    group_a = set(input("Names in group A (comma separated): ").title().replace(", ", ",").split(","))
    group_b = set(input("Names in group B (comma separated): ").title().replace(", ", ",").split(","))
    print("In both groups :", sorted(group_a & group_b))
    print("In A only      :", sorted(group_a - group_b))
    print("In A or B      :", sorted(group_a | group_b))


def main():
    while True:
        print("\n=== Student Record Manager ===")
        print("1. Add student")
        print("2. Remove student")
        print("3. Show all students")
        print("4. Show unique sections")
        print("5. Compare two groups (sets)")
        print("6. Exit")
        choice = input("Choose (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            show_students()
        elif choice == "4":
            show_sections()
        elif choice == "5":
            compare_groups()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
