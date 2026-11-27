def get_average(grades):
    """Return the average of a list of grades."""
    return sum(grades) / len(grades)


def get_letter(average):
    """Return the letter grade for an average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_remark(average):
    """Return Passed or Failed."""
    if average >= 60:
        return "Passed"
    return "Failed"


def ask_grade(subject):
    """Keep asking until the user types a valid grade from 0 to 100."""
    while True:
        value = input(f"Enter your grade in {subject}: ")
        if value.replace(".", "", 1).isdigit() and 0 <= float(value) <= 100:
            return float(value)
        print("Invalid grade. Please type a number from 0 to 100.")


def main():
    name = input("Enter student name: ")
    subjects = ["Math", "Science", "English", "Filipino"]
    grades = []
    for subject in subjects:
        grades.append(ask_grade(subject))

    average = get_average(grades)
    print("\n--- Grade Report ---")
    print(f"Student : {name}")
    print(f"Average : {average:.2f}")
    print(f"Letter  : {get_letter(average)}")
    print(f"Remark  : {get_remark(average)}")


main()

