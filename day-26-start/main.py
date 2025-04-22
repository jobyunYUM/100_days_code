import random
# List comprehenshion
# new_list = [new_item for item in list if test]
numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
name = "Angela"
letters_list = [letter for letter in name]
range_list = [num + 2 for num in range(1,5)]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]

upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)

# Dictionary comprehension
# new_dict = {new_key : new_value for (key,value) in dict.items() if test}
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student : random.randint(0,100) for student in names}

passed_students = {student : score for (student,score) in students_scores.items() if score >= 70}
# print(passed_students)

import pandas as pd

student_dict = {"Angela": 56,"James":76,"Lily":98}

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)