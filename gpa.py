import math
import numpy as np

def letter_to_gpa(letter):
    # Define the grade scale
    grade_scale = {
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.0
    }
    return grade_scale[letter]    

def gpa(data):
    total_gpa = 0
    sum_credit = 0
    course_name = ""
    course_letter_grade = ""
    course_credit = 0
    list_of_courses = []
    
    for line in data:
        course_name, course_letter_grade, course_credit = line.strip().split()
        list_of_courses.append(course_name)
        sum_credit += int(course_credit)
        total_gpa += letter_to_gpa(course_letter_grade) * int(course_credit)
    # Calculate the GPA
    
    return [round(total_gpa / sum_credit, 2), list_of_courses]    

if __name__ == '__main__':
    gpa_data = open('gpa_data.txt', 'r').readlines()
    gpa_res, course_list = gpa(gpa_data)
    print(gpa_res)
    print(sorted(course_list))