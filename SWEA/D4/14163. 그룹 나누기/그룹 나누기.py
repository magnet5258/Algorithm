class DisjointSet:
    def __init__(self, n):
        self.p = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
 
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
 
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
 
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.p[py] = px
            elif self.rank[px] < self.rank[py]:
                self.p[px] = py
            else:
                self.p[py] = px
                self.rank[px] += 1
 
def count_disjoint_sets(n, edges):
    ds = DisjointSet(n)
 
    for x, y in edges:
        ds.union(x, y)
 
    unique_roots = set(ds.find(i) for i in range(1, n + 1))
    return len(unique_roots)
 
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    start = [lst[i] for i in range(0, len(lst), 2)]
    end = [lst[i] for i in range(1, len(lst), 2)]
    edges = list(zip(start, end))
    print(f'#{test_case} {count_disjoint_sets(N, edges)}')