#Grading Program
#You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 
#Write a program that converts their scores to grades.
#By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


student_grades={}
for key in student_scores:
    if student_scores[key]>=91 and student_scores[key]<=100:
        student_grades[key]="Outstanding"
    elif student_scores[key]>=81 and student_scores[key]<=90:
        student_grades[key]="Exceeds Expectations"
    elif student_scores[key]>=71 and student_scores[key]<=80:
        student_grades[key]="Acceptable" 
    else:
        student_grades[key]="Fail"
        

print(student_grades)