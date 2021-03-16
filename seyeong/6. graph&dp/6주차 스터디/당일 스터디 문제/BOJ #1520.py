import sys, collections

input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(r)]
dp = [[-1 for _ in range(c)] for _ in range(r)]


# print(graph)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(s1, s2):

    if s1 == r-1 and s2 == c-1:
        return 1

    if dp[s1][s2] != -1:
        return dp[s1][s2]
    
    result = 0 
    for i in range(4):
        nr, nc = s1 + dr[i] , s2 + dc[i]
        if 0 <= nr < r and 0 <= nc < c:
            if graph[nr][nc] < graph[s1][s2]:
                result += dfs(nr, nc)
    print(s1, s2, result)
    dp[s1][s2] = result
    return result 


                            
        
dfs(0, 0) 
print(dp[0][0])





# print(map)
# print(dp)
# for i in range(r):
#     for j in range(c):

#         if i == 0 and j == 0:
#             dp[i][j] = 1
#             map[i][j] = True

#         if map[i][j]:
#             for k in range(4):
#                 nr, nc = i+dr[k], j+dc[k]
#                 if 0 <= nr < r and 0 <= nc < c:
#                     if graph[nr][nc] < graph[i][j]:
#                         map[nr][nc] = True

# for i in range(r):
#     for j in range(c):

#         if map[i][j]:
#             for k in range(4):
#                 nr, nc = i+dr[k], j+dc[k]
#                 if 0 <= nr < r and 0 <= nc < c:
#                     if map[nr][nc] and graph[nr][nc] > graph[i][j]:
#                         if dp[nr][nc] > 1:
#                             dp[i][j] += dp[nr][nc]

#                         else:
#                             dp[i][j] += 1
                        