import sys
r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
# print(graph)

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, 0, -1, 1, 0, -1, 1]

def bfs(s1, s2):
    cnt = 0

    for i in range(8):
        nr, nc = s1+dr[i], s2+dc[i]
        if graph[nr][nc] == '.':
            cnt += 1
        # print([s1, s2],cnt)
    if cnt >= int(graph[s1][s2]):
        print([s1,s2], ans)
        # graph[s1][s2] = '.'
        return True
    else:
        return False

ans = 0 
while True:
    answer = []
    ans += 1
    for i in range(r):
        for j in range(c):

            if graph[i][j] != '.':
                if int(graph[i][j]) < 9:
                    
                    if bfs(i,j):
                        # print(graph)
                        # print("\n")
                        answer.append([i,j])
    if answer:
        for r, c in answer:
            graph[r][c] = '.'
            print(graph)
                    
    # break
        
    
    else:
        
        break
    

print(ans)
# print(graph)