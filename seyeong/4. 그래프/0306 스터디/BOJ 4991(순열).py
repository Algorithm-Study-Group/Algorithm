import sys, collections, itertools

dir = [(0, 1), (0,-1), (1, 0), (-1, 0)]
answer = 0 

def bfs(start, target, distance):
     
    dq = collections.deque()
    s1, s2 = start
    dq.append([s1,s2,0])
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[s1][s2] = True
    
        
    while dq:
        cr, cc, distance = dq.popleft()
        for i in range(len(dir)):
            
            nr, nc  = cr + dir[i][0], cc + dir[i][1] 
            if 0 <= nr < r and 0 <= nc  < c:
                if not visited[nr][nc] and graph[nr][nc] != 'x':
                    if [nr, nc] == target:
                        

                        return distance+1
                    else:
                        dq.append([nr,nc,distance+1])
                        visited[nr][nc] = True
    
    return -1



while True:
    answer = []
    c, r = map(int, sys.stdin.readline().split())
    if c == 0 and r == 0:
        break
    start = []
    candidate = []
    graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'o':
                start.append([i,j])
            if graph[i][j] == '*':
                candidate.append([i,j])
                # graph[i][j] = '.'
                # print(bfs(i, j, 0))

    # print(candidate)

    for point in itertools.permutations(candidate):
        path = start + list(point)
        # print(path)
        result = 0
        for j in range(len(path)-1):
            dist = bfs(path[j], path[j+1], result)
            if dist == -1:
                answer.append(-1)
                break
            else:
                result += bfs(path[j], path[j+1], result)
            # print(result)
        else:
            answer.append(result)
        
        
    print(min(answer))

    