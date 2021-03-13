import sys, collections
r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
# print(graph)

# dr = [0, 0, 1, 1, 1, -1, -1, -1]
# dc = [1, -1, 0, -1, 1, 0, -1, 1]
dir = [(0,1), (0,-1), (1,0), (1,-1), (1,1), (-1,0), (-1,-1), (-1,1)]
answer = []

check = [[0 for _ in range(c)] for _ in range(r)]

q = collections.deque()

for i in range(r):
    for j in range(c):

        if graph[i][j] == '.':
            graph[i][j] = 0
            q.append([i,j])
        else:
            graph[i][j] = int(graph[i][j])

# print(graph, q)
while q:
    cr, cc = q.popleft()
    for i in range(8):
        nr, nc = cr+dir[i][0], cc+dir[i][1]
        if 0 > nr or nr >= r or 0 > nc or nc >= c:
            continue
        # if 0 <= nr < r and 0 <= nc < c:
        if graph[nr][nc] != 0:
            graph[nr][nc] -= 1
            if graph[nr][nc] == 0:
                check[nr][nc] = check[cr][cc] + 1
                q.append([nr,nc])
                # answer = max(answer, check[nr][nc])
                answer.append(check[nr][nc])

print(max(answer))