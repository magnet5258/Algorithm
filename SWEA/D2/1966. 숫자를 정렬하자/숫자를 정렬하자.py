T = int(input())
for test_case in range(1, T + 1):
    _ = int(input())
    lst = sorted(map(int, input().split()))
    print(f"#{test_case} {' '.join(map(str, lst))}")
