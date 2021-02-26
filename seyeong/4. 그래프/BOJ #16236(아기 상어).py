import sys, collections

n = int(sys.stdin.readline().strip())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# print(graph)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(s1, s2):
    time = 0
    shark = 2
    cnt = 0
    q = collections.deque()
    q.append([s1, s2, 0])
    check = [[0 for _ in range(n)] for _ in range(n)]
    check[s1][s2] = 1
    candidate = []
    while True:
        while q:
            # print(q)
            # print([s1,s2], time, shark, cnt, sorted(candidate))
            x, y, d = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if check[nx][ny] == 0:
                        if graph[nx][ny] < shark and graph[nx][ny] != 0:
                            candidate.append([d+1, nx, ny])
                            
                        if graph[nx][ny] <= shark:
                            check[nx][ny] = 1
                            q.append([nx,ny,d+1])
        if not candidate: 
            return time
        else:
            candidate.sort()
            time += candidate[0][0]
            cnt += 1
            if cnt == shark:
                shark += 1
                cnt = 0
            px, py = candidate[0][1], candidate[0][2]
            graph[px][py] = 0
            s1, s2 = px, py
            check = [[0 for _ in range(n)] for _ in range(n)]
            check[s1][s2] = 1
            q = collections.deque()
            q.append([px, py, 0])
            candidate = []
            

for i in range(n):
    for j in range(n):

        if graph[i][j] == 9:
            graph[i][j] = 0
            print(bfs(i, j))
            break
# print(time)