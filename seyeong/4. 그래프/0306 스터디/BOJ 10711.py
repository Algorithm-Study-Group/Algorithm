import sys, collections
r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
# print(graph)

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, -1, 1, 0, -1, 1]
answer = 0

def bfs(s1, s2):
    result = []
    q = collections.deque()
    q.append([s1,s2])
    visited[s1][s2] = True
    while q:
        r, c = q.popleft()
        cnt = 0
        for i in range(8):
            nr, nc = r+dr[i], c+dc[i]
            if not visited[nr][nc]:
                if graph[nr][nc] == '.':
                    cnt += 1
                else:
                    if int(graph[nr][nc]) < 9:
                        q.append([nr,nc])
                        visited[nr][nc] = True
        if cnt >= int(graph[r][c]):
            result.append([r,c])
        print(result)
    return result if result else None


while True:
    answer += 1
    visited = [[False for _ in range(c)] for _ in range(r)]
    result = []
    for i in range(1, r-1):
        for j in range(1, c-1):

            if graph[i][j] != '.' and not visited[i][j]:
                result.append(bfs(i,j))
    if result:
        print("result:",result)
        break
        # for i, j in result:
        #     graph[i][j] = '.'
    else:
        print(answer)
        break
