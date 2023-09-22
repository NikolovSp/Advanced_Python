number_of_students = int(input())
grade_book = {}
sum_grades = 0
for student in range(number_of_students):
    name, grade = input().split()
    if name not in grade_book:
        grade_book[name] = []
    grade_book[name].append(float(grade))
# print(grade_book.items())
for name in grade_book.keys():
    print(f'{name} -> ', end='')
    for grades in grade_book[name]:
        print(f'{grades:.2f}', end=' ')
        sum_grades += grades
    avg_grades = sum_grades / len(grade_book[name])
    sum_grades = 0
    print(f'(avg: {avg_grades:.2f})')
