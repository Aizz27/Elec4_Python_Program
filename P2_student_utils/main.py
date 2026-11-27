import student_utils


def main():
    first = input("First name: ")
    last = input("Last name: ")
    grades = [float(g) for g in input("Enter grades separated by spaces: ").split()]

    average = student_utils.compute_average(grades)

    print("\n--- Student Summary ---")
    print("Name    :", student_utils.format_name(first, last))
    print("Average :", round(average, 2))
    print("Highest :", student_utils.get_highest(grades))
    print("Lowest  :", student_utils.get_lowest(grades))
    if student_utils.is_passing(average):
        print("Result  : Passed")
    else:
        print("Result  : Failed")


main()
