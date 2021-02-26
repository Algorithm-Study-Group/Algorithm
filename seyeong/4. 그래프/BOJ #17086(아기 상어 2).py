import sys, collections

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [] 
# print(graph)

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [-1, 1, 0, -1, 1, 0, -1, 1]

def bfs(x, y):
    check = [ [0 for _ in range(m)] for _ in range(n)]
    q = collections.deque()
    q.append([x,y])
    check[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(8):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == 0:
                    if graph[nx][ny] == 1:
                        answer.append(max(abs(nx-x),abs(ny-y)))
                        return
                    else:
                        check[nx][ny] = 1
                        q.append([nx, ny])
        
    # print(check)

for i in range(n):
    for j in range(m):

        if graph[i][j] == 0:
            bfs(i, j)
        # print([i,j] , answer)
        
print(max(answer))
 
# dist = [ [0 for _ in range(m)] for _ in range(n)]


# for i in range(n):
#     for j in range(m):
#         # print(graph[i][j])
#         if graph[i][j] == 0:
            
#             dist[i][j] = sys.maxsize

#         else:
#             pass
    



# # print(dist)
