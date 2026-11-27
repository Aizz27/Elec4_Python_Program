def format_name(first, last):
    "Return the name as 'Last, First' with proper capital letters."
    return f"{last.strip().title()}, {first.strip().title()}"


def compute_average(grades):
    "Return the average of a list of grades (0 if the list is empty)."
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


def is_passing(average, passing_grade=60):
    "Return True if the average is at or above the passing grade."
    return average >= passing_grade


def get_highest(grades):
    "Return the highest grade."
    return max(grades)


def get_lowest(grades):
    "Return the lowest grade."
    return min(grades)
