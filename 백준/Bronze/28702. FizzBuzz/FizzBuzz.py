lst = [input() for _ in range(3)]

for i in lst:
    if i not in ['Fizz', 'Buzz', 'FizzBuzz']:
        num = i
        plus = lst.index(i)
        break

ans = int(num) + 3 - plus

if ans % 3 == 0:
    if ans % 5 ==0:
        ans = 'FizzBuzz'
    else:
        ans = 'Fizz'
elif ans % 5 == 0:
    ans = 'Buzz'
else:
    ans = str(ans)

print(ans)