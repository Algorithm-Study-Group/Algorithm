import sys
sys.setrecursionlimit(5000)

N, M, k = map(int, input().split(" "))
expense = list(map(int, input().split(" ")))
visited = [False] * (N+1)
MIN = 0
relationship = [[] for _ in range(N+1)]
min_expense = [0] * (N+1)
payment = 0

for _ in range(M):
    a, b = map(int, input().split(" "))
    relationship[a].append(b)
    relationship[b].append(a)

def solution():
    global payment, MIN

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            MIN = int(1e9)
            dfs(i)
            min_expense[i] = MIN
    if sum(min_expense) > k:
        print("Oh no")
    else:
        print(sum(min_expense))


def dfs(node):
    global MIN
    MIN = min(MIN, expense[node-1])

    for i in relationship[node]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
    return


solution()