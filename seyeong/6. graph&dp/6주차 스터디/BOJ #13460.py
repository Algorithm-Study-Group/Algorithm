import sys, collections, heapq

input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

visited = [[False for _ in range(c)] for _ in range(r)]

def move(mode, cur_r, cur_c):
    if mode == 1:
        while graph[cur_r][cur_c] == '.' or graph[cur_r][cur_c] == 'R' or graph[cur_r][cur_c] =='B' and not visited[cur_r][cur_c] :
            cur_r -= 1
            if graph[cur_r][cur_c] == 'O':
                return cur_r, cur_c, True
            visited[cur_r][cur_c] = True
        return cur_r, cur_c, False

    if mode == 3:
        while graph[cur_r][cur_c] == '.' or graph[cur_r][cur_c] == 'R' or graph[cur_r][cur_c] =='B' and not visited[cur_r][cur_c] :
            cur_r += 1
            if graph[cur_r][cur_c] == 'O':
                return cur_r, cur_c, True
            visited[cur_r][cur_c] = True
        return cur_r, cur_c, False

    if mode == 0:
        while graph[cur_r][cur_c] == '.' or graph[cur_r][cur_c] == 'R' or graph[cur_r][cur_c] =='B' and not visited[cur_r][cur_c] :
            cur_c -= 1
            if graph[cur_r][cur_c] == 'O':
                return cur_r, cur_c, True
            visited[cur_r][cur_c] = True
        return cur_r, cur_c, False

    
    if mode == 2:
        while graph[cur_r][cur_c] == '.' or graph[cur_r][cur_c] == 'R' or graph[cur_r][cur_c] =='B' and not visited[cur_r][cur_c] :
            cur_c += 1
            if graph[cur_r][cur_c] == 'O':
                return cur_r, cur_c, True
            visited[cur_r][cur_c] = True
        return cur_r, cur_c, False

def is_align_horizontally(r2, b2):
    
        return r2 > b2

def is_align_vertically(r1, r2, b1, b2):
    if r2 == b2:
        return r1 > b1

def bfs(s1,s2):
    
    visited[s1][s2] = True
    q = collections.deque()
    q.append([s1,s2,0,''])
    result = []
    
    while q:
        cr, cc, cnt, path = q.popleft()
        for i in range(4):
            a1, a2, a3 = move(i, cr, cc)
            answer = a3
            # print(a1)
            if answer:
                heapq.heappush(result, [cnt+1, path+str(i)])
                # break
            # q.append([a1,a2,cnt+1,path+str(i)])

    print(visited)
    return result


# print(graph)

for i in range(1, r-1):
    for j in range(1, c-1):

        if graph[i][j] == 'R':
            r1, r2 = i, j
        if graph[i][j] == 'B':
            b1, b2 = i, j
        if graph[i][j] == 'O':
            t1, t2 = i, j

print(bfs(r1, r2))
# print(s1, s2, t1, t2)

