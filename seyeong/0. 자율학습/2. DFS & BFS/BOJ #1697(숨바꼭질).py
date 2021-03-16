from collections import deque

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            return visit[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not visit[nx]:
                visit[nx] = visit[x] + 1
                q.append(nx)



MAX = 100000
visit = [0] * (MAX + 1)
n, k = map(int, input().split())             
print(bfs())