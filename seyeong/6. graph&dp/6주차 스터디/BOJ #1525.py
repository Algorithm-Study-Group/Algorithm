import collections

answer = '1234567890'

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

graph = [list(map(int, input().split())) for _ in range(3)]

print(graph)

for i in range(3):
    for j in range(3):
        if graph[i][j] == 0:
            s1, s2 = i, j

initial = ''
for row in graph:
    for a in row:
        initial += str(a)
print(initial)

def bfs(s1, s2):
    q = collections.deque()
    q.append([s1,s2,initial,0])
    visited = [[False for _ in range(3)] for _ in range(3)]
    visited[s1][s2] = True
    result = []

    while q:
        
        cr, cc, path, cnt = q.popleft()
        # print(cr, cc, cnt, graph)
        if path == answer:
            result.append(cnt)
            
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < 3 and 0 <= nc < 3:
                
                if not visited[nr][nc]:
                    # graph[nr][nc], graph[cr][cc] = graph[cr][cc], graph[nr][nc]
                    temp = path[:]
                    temp[nr*3+nc], temp[cr*3+cc] = temp[cr*3+cc], temp[nr*3+nc]
                    print(temp)
                    visited[nr][nc] = True
                    q.append([nr,nc,temp,cnt+1])
                

    return result


            

# # print(s1,s2)
print(bfs(s1,s2))