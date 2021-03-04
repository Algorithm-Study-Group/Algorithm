import collections, sys 
r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip())for _ in range(r)]
# visited = [[False for _ in range(c)] for _ in range(r)]
# print(visited)
answer = 0
dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(s1, s2):
    ans = 0
    visited = [[False for _ in range(c)] for _ in range(r)]
    # dist = [[0 for _ in range(c)] for _ in range(r)]
    q = collections.deque()
    q.append([s1, s2, 0])
    visited[s1][s2] = True

    while q:
        cur_r, cur_c, time = q.popleft()
        # ans.append(time)
        for i in range(4):
            nr, nc = cur_r + dr[i] , cur_c + dc[i]
            
            if 0 <= nr < r and 0 <= nc < c:
                if not visited[nr][nc] and graph[nr][nc] == 'L':
                    visited[nr][nc] = True
                    ans = max(ans, time+1)
                    q.append([nr, nc, time+1])
                    
    
    
    return ans



# print(graph)
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            answer = max(answer, bfs(i,j))
            # print([i,j], answer[-1])

print(answer)

