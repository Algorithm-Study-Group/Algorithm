import sys, collections

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
broken = [[False for _ in range(m)] for _ in range(n)]
# print(graph)
answer = []

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(s1, s2):
    
    q = collections.deque()
    q.append([s1 , s2 , 1 , False])
    visited[s1][s2] = True

    while q:
        x, y, d, wall = q.popleft()

        if x == n-1 and y == m-1:
            answer.append(d)

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not wall:
                    if graph[nx][ny] == 0:
                        if not visited[nx][ny]:
                            q.append([nx, ny, d+1, wall])
                            visited[nx][ny] = True
                    
                    else:
                        if not broken[nx][ny]:
                            broken[nx][ny] = True
                            q.append([nx, ny, d+1, True])

                else:
                    if graph[nx][ny] == 0:
                        if not broken[nx][ny]:
                            broken[nx][ny] = True
                            q.append([nx, ny, d+1, wall])
        
    # print(answer)
    return min(answer) if answer else -1


    
    # return check


print(bfs(0,0))
# print(min(answer) if answer else -1)








