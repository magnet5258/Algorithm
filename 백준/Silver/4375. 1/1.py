import sys

nums = list(map(int, sys.stdin.read().split()))
for n in nums:
    length = len(str(n))
    num = '1'
    while True:
        if int(num) % n == 0:
            print(len(num))
            break
        num += '1'