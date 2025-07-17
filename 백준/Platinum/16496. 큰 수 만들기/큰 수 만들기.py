import functools

N = int(input())
nums = input().split()

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

nums.sort(key=functools.cmp_to_key(compare))
print(str(int(''.join(nums))))