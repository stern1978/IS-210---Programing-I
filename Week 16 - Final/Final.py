#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Finds the best schools for sudents"""

import json

SCHOOL = open('schools.json', 'r')
STUDENT = open('students.json', 'r')

def school_spending():
    """Return the top school with the least amount spent per student."""

    data = json.load(SCHOOL)
    spending = data['data']
    school = spending[0] #needs to step through all the data.
    students = school['students']
    spending = school['per_student_spending']
    grades = school['grades']
    district = school['district_code']

    d = sum([x * grades[x] for x in grades])
    #print d

    #for grade, num in grades.iteritems():
        #total_grades = float(grade) * float(num)
        #sum total of total_grades

    SCHOOL.close()
    #total_per_school = students * spending
    #Return school with best spending per student.
    #return max(total_per_school / total_grades)

def student_spending():
    """Returns the top district with the least amout spent per student."""

    data = json.load(STUDENT)
    spending = data['data']

    for student in spending.itervalues():
        school_id = student['school_id']
        score = student['score']
        #Format for output best = {school_id: sum(score)}
        #return t
    STUDENT.close()


if __name__ == '__main__':
    school_spending()
    student_spending()
