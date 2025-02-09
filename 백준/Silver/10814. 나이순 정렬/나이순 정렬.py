N = int(input())
data = {}
for _ in range(N):
    age, name = input().split()
    age = int(age)
    if age in data:
        data[age].append(name)
    else:
        data[age] = [name]
sorted_data = sorted(data.items(), key=lambda x: x[0])
for age, names in sorted_data:
    for name in names:
        print(age, name)