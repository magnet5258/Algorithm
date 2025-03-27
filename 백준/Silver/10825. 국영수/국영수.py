N = int(input())
students = {}
for _ in range(N):
    name, K, E, M = input().split()
    students[name] = [int(K), int(E), int(M)]
sorted_students = sorted(students.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))
for key, value in sorted_students:
    print(key)