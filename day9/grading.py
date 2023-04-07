student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
# This is the Right Version!
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

        
# This is my Version
# for key in student_scores:
#     if key == "Harry":
#         student_grades[key] = "Exceeds Expectation"
#     elif key == "Ron":
#         student_grades[key] = "Acceptable"
#     elif key == "Hermione":
#         student_grades[key] = "Outstanding"
#     elif key == "Draco":
#         student_grades[key] = "Acceptable"
#     elif key == "Neville":
#         student_grades[key] = "Fail"

print(student_grades)

