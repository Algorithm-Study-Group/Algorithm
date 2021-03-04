import sys, collections, heapq

dir = [(0, 1), (0,-1), (1, 0), (-1, 0)]

def bfs(s1, s2, answer):
    
    q = collections.deque()
    dist = []
    q.append([s1,s2,0])
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[s1][s2] = True
    while q:
        cur_r, cur_c, distance = q.popleft()
        for i in range(len(dir)):
            next_r, next_c = cur_r + dir[i][0], cur_c + dir[i][1] 
            if 0 <= next_r < r and 0 <= next_c < c:
                if not visited[next_r][next_c] and graph[next_r][next_c] != 'x':
                    if graph[next_r][next_c] == '.':
                        visited[next_r][next_c] = True
                        q.append([next_r, next_c, distance+1])
                    if graph[next_r][next_c] == '*':
                        visited[next_r][next_c] = True
                        q.append([next_r, next_c, distance+1])
                        heapq.heappush(dist, [distance+1, next_r, next_c])       
    
    if dist:
        ans, nr, nc = heapq.heappop(dist)
        answer += ans
        graph[nr][nc] = '.'
        graph[s1][s2] = '.'
        return bfs(nr,nc,answer)

    else:
        for i in range(r):
            for j in range(c):
                if not visited[i][j]:
                    if graph[i][j] == '*':
                        return -1
        return answer
    
    return answer

while True:
    c, r = map(int, sys.stdin.readline().split())
    if c == 0 and r == 0:
        break
    graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'o':
                print(bfs(i, j, 0))

    # print(graph)