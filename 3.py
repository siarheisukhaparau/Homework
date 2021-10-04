### Task 4.3
# File `data/students.csv` stores information about students in
# [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark.
# 1) Implement a function which receives file path and returns names of top performer students
# ```python

# def get_top_performers(file_path, number_of_top_students=5):

import csv

def sort_scv_file_by_age(file_path):
    with open(file_path, newline='') as file:
        reader_ = csv.reader(file)
        l = sorted(reader_, key=lambda x: x[1], reverse=True)
    with open('students_sorted_by_age.csv', 'w') as fileout:
        write_ = csv.writer(fileout)
        write_.writerows(l)
    print("New file students_sorted_by_age.csv was created")

def get_top_performers(file_path, number_of_top_students=5):

    with open(file_path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        dict_with_stud_and_their_marks = {}
        for row in file_reader:
            dict_with_stud_and_their_marks[(row["student name"])] = float(row["average mark"])
    sorted_tuples = sorted(dict_with_stud_and_their_marks.items(), key=lambda item: item[1])
    dict_with_stud_and_their_marks = {k: v for k, v in sorted_tuples}
    list_with_names = list(dict_with_stud_and_their_marks.keys())
    list_with_names.reverse()
    list_top_performers = list_with_names[:number_of_top_students]

    return list_top_performers

print(get_top_performers("students.csv", number_of_top_students=5))
print(sort_scv_file_by_age("students.csv"))
