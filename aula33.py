from itertools import groupby

students = [
    {'name': 'Luiz', 'grade': 'A'},
    {'name': 'Letícia', 'grade': 'B'},
    {'name': 'Fabrício', 'grade': 'A'},
    {'name': 'Rosemary', 'grade': 'C'},
    {'name': 'Joana', 'grade': 'D'},
    {'name': 'João', 'grade': 'A'},
    {'name': 'Eduardo', 'grade': 'B'},
    {'name': 'Anderson', 'grade': 'C'},
]


def sort_by_grade(student):
    return student['grade']


# Sort students by grade
sorted_students = sorted(students, key=sort_by_grade)

# Group students by grade
groups = groupby(sorted_students, key=sort_by_grade)

# Iterate through each group
for key, group in groups:
    print(key)
    for student in group:
        print(student)
