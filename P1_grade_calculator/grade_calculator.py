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


print(get_average([90, 80]), get_letter(85), get_remark(50))