student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
} 
x=student_scores['Harry']+2
print(x)
student_grades={}
for i in student_scores:
    if 90 < student_scores[i] <=100:
        student_grades[i]="Outstanding"
    elif 80 < student_scores[i]<=90:
        student_grades[i]="Exceeds Expectations"
    elif 70 < student_scores[i]<=80:
        student_grades[i]=" Acceptable"
    else:
        student_grades[i]="Fail"


print(student_grades)