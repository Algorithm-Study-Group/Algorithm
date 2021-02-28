import sys, collections

r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
# print(graph)

answer = []
dx = [1, 0, -1]
dy = [1, 1, 1]

check = [[0 for _ in range(c)] for _ in range(r)]

# print(check)

def dfs(s1, s2):
    
    stack = []
    stack.append([s1,s2])
    # check[s1][s2] = 1

    while stack:
        # print(stack)
        x, y = stack.pop()
        check[x][y] = 1
        if y == c-1:
            answer.append(x)
            return answer
            
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if check[nx][ny] == 0 and graph[nx][ny] == '.':
                    
                    # check[nx][ny] = 1
                    stack.append([nx,ny])
                
    return answer 
    


for i in range(r):
    dfs(i, 0)

print(len(answer))