def gather_credits(number_of_credits, *args):
    courses_list = []
    total_credits = 0
    for course_name, credits in args:
        if total_credits >= number_of_credits:
            break
        if course_name in courses_list:
            continue
        courses_list.append(course_name)
        total_credits += credits

    result = []
    if total_credits >= number_of_credits:
        result.append(f"Enrollment finished! Maximum credits: {total_credits}.")
        result.append(f"Courses: {', '.join(sorted(courses_list))}")
    else:
        result.append(f"You need to enroll in more courses! You have to gather {number_of_credits - total_credits} credits more.")

    return "\n".join(result)


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("zdvanced", 30),
    ("aasics", 27),
    ("gundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
