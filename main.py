import numpy as np
import pandas as pd

xlsx = pd.ExcelFile("Task.xlsx")
dataset_student = pd.read_excel(xlsx, "Dataset-student")
dataset_student_math = pd.read_excel(xlsx, "Dataset-student-math")
dataset_student_english = pd.read_excel(xlsx, "Dataset-student-english")

