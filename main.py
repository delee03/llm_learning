passed_students = {
    "Alex": 12,
    "Beth": 23,
    "Caroline": 35,
    "Dave": 1,
    "Elanor": 100,
    "Catherine": 99,
}

new_dic_comprehend = {student:value for (student, value) in passed_students.items() if value % 2 == 0}
print(new_dic_comprehend)

for (key, value) in passed_students.items():
    print(f"{key}  + {value}")

import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [1,2,5]
}

data = pd.DataFrame(student_dict)
print(data)

for (index, row) in data.iterrows():
    print(row.student if not row.score >6 else None )

def add(*agrs):
    print(agrs[1])
    print(type(agrs))
    sum = 0
    for n in agrs:
        sum += n
    return sum

print(add(1,4,6,7))

