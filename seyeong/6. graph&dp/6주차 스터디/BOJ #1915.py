import sys

input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(r)]

# print(graph)

dp = [[0 for _ in range(c)] for _ in range(r)]

moves = [[0, -1], [-1, -1], [-1, 0]]
answer = 0
for i in range(r):
    for j in range(c):

        if i < 1 or j < 1:
            if graph[i][j] == 1:
                dp[i][j] = 1

        else:
            if graph[i][j] == 1:
                # for dr, dc in moves:
                    dp[i][j] += min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        answer = max(dp[i][j], answer)

print(answer**2)
