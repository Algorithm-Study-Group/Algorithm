import sys, collections

answer = False

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = collections.defaultdict(list)

for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    # print(l)
    for j in range(n):
        if l[j] == 1:
            graph[i+1].append(j+1)

def bfs(start, target):
    visited = [False for _ in range(n+1)]
    q = collections.deque()
    q.append(start)
    visited[start] = True
    while q:
        # print(q, visited)
        cur_node = q.popleft()
        for node in graph[cur_node]:
            if node == target:
                return True
            if not visited[node]:
                q.append(node)
                # print(q)
                visited[node] = True
    return False


plan = list(map(int, sys.stdin.readline().split()))

# print(graph, plan)

for i in range(len(plan)-1):
    if bfs(plan[i], plan[i+1]):
        answer = True
    else:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")