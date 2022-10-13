from main import dataset_student, dataset_student_math, dataset_student_english

students_with_score16 = []
for i in dataset_student_math.values:
    if i[-1] == 16:
        students_with_score16.append(i[0])

# print(students_with_score16)

for i in dataset_student_english.values:
    if i[0] in students_with_score16:
        print(i[-1])
