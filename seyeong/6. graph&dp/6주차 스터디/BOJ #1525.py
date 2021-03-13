import collections

answer = [[1,2,3], [4,5,6], [7,8,0]]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

graph = [list(map(int, input().split())) for _ in range(3)]

# print(graph)

for i in range(3):
    for j in range(3):
        if graph[i][j] == 0:
            s1, s2 = i, j

def bfs(s1, s2):
    q = collections.deque()
    q.append([s1,s2,0])
    visited = [[False for _ in range(3)] for _ in range(3)]
    visited[s1][s2] = True
    result = []

    while q:
        
        cr, cc, cnt = q.popleft()
        # print(cr, cc, cnt, graph)
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < 3 and 0 <= nc < 3:
                
                if not visited[nr][nc] and graph[nr][nc] == answer[cr][cc]:
                    # graph[nr][nc], graph[cr][cc] = graph[cr][cc], graph[nr][nc]
        
                    visited[nr][nc] = True
                    q.append([nr,nc,cnt+1])
                if [nr, nc] == [2, 2]:
                    for i in range(3):
                        for j in range(3):
                            if not visited[i][j]:
                                if graph[i][j] == answer[i][j]:
                                    result.append(cnt+1)

    return min(result) if result else -1


            

# print(s1,s2)
print(bfs(s1,s2))