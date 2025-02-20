N = int(input())
pillars = [tuple(map(int, input().split())) for _ in range(N)]
pillars.sort()
positions, heights = zip(*pillars)
max_idx = heights.index(max(heights))
area = heights[max_idx]

left_max = 0
for i in range(max_idx):
    left_max = max(left_max, heights[i])
    width = positions[i + 1] - positions[i]
    area += left_max * width

right_max = 0
for i in range(N - 1, max_idx, -1):
    right_max = max(right_max, heights[i])
    width = positions[i] - positions[i - 1]
    area += right_max * width

print(area)