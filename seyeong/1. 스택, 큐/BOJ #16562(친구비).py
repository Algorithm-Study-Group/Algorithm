import collections

n, m, cash = list(map(int, input().split()))

cost = list(map(int, input().split()))

graph = collections.defaultdict(list)

for _ in range(m):
    i, j = map(int, input().split())

    graph[i-1].append(j-1)
    graph[j-1].append(i-1)

visited = [False] * n
money = float('inf')
answer = 0

def dfs(start):
    if visited[start]:
        return 0 
    money = float('inf')
    stack = [start]
    while stack:
        node = stack.pop()
        money = min(money, cost[node])
        for e in graph[node]:
            if not visited[e]:
                visited[e] = True
                stack.append(e)
    
    return money
    
for i in range(n):
    answer += dfs(i)


print("Oh no" if answer > cash else answer)

