from main import dataset_student, dataset_student_math, dataset_student_english

students_scored_higher_in_G2 = dataset_student_math['G2'].values > dataset_student_math['G3'].values
c = 0
for value in students_scored_higher_in_G2:
  if value:
    c += 1
print(f"Total of {c} students have higher score in Math in G2 than G3")