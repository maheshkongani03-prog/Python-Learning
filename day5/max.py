student_scores=[180,23,398,243,758,845,2431,5643,653,739]
max_score=0
for score in student_scores:
    if max_score<score:
        max_score=score
print(f"the max score is: {max_score}")
        