grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
score = 0
grade_sum = 0
for _ in range(20):
    lst = list(input().split())
    if lst[2] in grade:
        score += grade[lst[2]] * float(lst[1])
        grade_sum += float(lst[1])
print(score / grade_sum)