import sys
answer = True

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):

            if i == j:
                graph[i][j] = 1
                
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

plan = list(map(int, sys.stdin.readline().split()))

for i in range(m-1):
    if graph[plan[i] - 1][plan[i+1] -1] != 1:
        
        answer = False
        break
if answer:
    print("YES")
else:
    print("NO")


# print(graph)
