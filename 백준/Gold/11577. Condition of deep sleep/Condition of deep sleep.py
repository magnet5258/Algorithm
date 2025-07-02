from collections import deque

N, K = map(int, input().split())
lights = list(map(int, input().split()))
flip = 0
cnt = 0
queue = deque()

for i in range(N):
    if queue and queue[0] == i:
        queue.popleft()
        flip ^= 1
    if lights[i] ^ flip == 1:
        if i + K > N:
            print('Insomnia')
            exit()
        cnt += 1
        flip ^= 1
        queue.append(i + K)

print(cnt)