student_heights = input('Input a list of student heights ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

count = 0
total = 0
for student_height in student_heights:
    print(student_height)
    count += 1
    total += student_height

average = round(total / count)
print(average)