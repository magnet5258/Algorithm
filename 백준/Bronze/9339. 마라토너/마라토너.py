from collections import defaultdict

T = int(input())
for _ in range(T):
    K = int(input())
    students = list(map(int, input().split()))
    N = int(input())
    participants = defaultdict(list)
    for _ in range(N):
        num, hour, minute = map(int, input().split())
        participants[num].append((hour, minute))
    lst = []
    for key, value in participants.items():
        hour, minute = value[0]
        if key in students:
            if 0 <= hour < 6 or (hour == 6 and minute == 0):
                lst.append((key, hour, minute))
    lst.sort(key=lambda x: (x[1], x[2]))
    print(lst[0][0], len(lst))