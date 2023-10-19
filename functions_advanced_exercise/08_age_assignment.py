def age_assignment(*args, **kwargs):
    age_dict = {}
    for name in args:
        age_dict[name] = kwargs[name[0]]
    sorted_result = dict(sorted(age_dict.items(), key=lambda kvp: -kvp[1]))

    result = []
    for name, age in sorted_result.items():
        result.append(f"{name} is {age} years old.")

    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))