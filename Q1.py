from main import dataset_student, dataset_student_math, dataset_student_english

finalgrade_difference_between_mathandenglish = abs(dataset_student_math['G3'] - dataset_student_english['G3'])

print(finalgrade_difference_between_mathandenglish)