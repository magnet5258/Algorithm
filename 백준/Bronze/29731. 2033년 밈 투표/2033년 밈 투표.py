promise = set()
promise.add('Never gonna give you up')
promise.add('Never gonna let you down')
promise.add('Never gonna run around and desert you')
promise.add('Never gonna make you cry')
promise.add('Never gonna say goodbye')
promise.add('Never gonna tell a lie and hurt you')
promise.add('Never gonna stop')

N = int(input())
in_promise = True
for _ in range(N):
    word = input()
    if word not in promise:
        in_promise = False

if in_promise:
    print('No')
else:
    print('Yes')