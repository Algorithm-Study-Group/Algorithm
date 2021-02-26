import sys, collections
n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
answer = [] 
# print(graph)

def bfs(j, k):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = collections.deque()
    q.append([j,k])
    check[j][k] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            x, y = cx+dx[i], cy+dy[i]
            if 0 <= x < n and 0 <= y < n:
                if check[x][y] == 0:
                    check[x][y] = 1
                    q.append([x,y])

    return



for i in range(101):
    check = [ [0 for _ in range(n)] for _ in range(n)]
    # print(check)
    c = 0 
    for j in range(n):
        for k in range(n):

            if graph[j][k] <= i:
                check[j][k] = 1
    # print(check)
    for j in range(n):
        for k in range(n):
            if check[j][k] == 0:
                bfs(j, k)
                # print("dfd :" , check)
                c += 1
    
    # if c == 0:
    #     answer.append(c)
    #     break

    answer.append(c)
    # print(answer)
print(max(answer))

