def solution(arr1, arr2):
    x = sum(arr1)
    y = sum(arr2)
    if len(arr1) == len(arr2):
        if x > y:
            return 1
        elif x < y:
            return -1
        else:
            return 0
    elif len(arr1) > len(arr2):
        return 1
    else:
        return -1