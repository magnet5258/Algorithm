import sys

N = int(sys.stdin.readline())
lst_1 = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lst_2 = list(map(int, sys.stdin.readline().split()))

output = []
for i in lst_2:
    output.append("1\n" if i in lst_1 else "0\n")

sys.stdout.write("".join(output))