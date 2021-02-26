import sys, collections 

n, m, v = map(int, input().split())

def make_graph(m):
    graph = collections.defaultdict(list)
    for i in range(m):
        p1, p2 = map(int, sys.stdin.readline().split())
        graph[p1].append(p2)
        graph[p2].append(p1)
    return graph

def dfs(start, visited = []):
    
    if start in visited:
        return visited

    
    else:
        visited.append(start)
        for n in sorted(graph[start]):

            dfs(n, visited)
    
    return visited
def bfs(start): 
    
    q = collections.deque([start])
    visited = []
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            for n in sorted(graph[node]):
                q.append(n)
    return visited

graph = make_graph(m)
# print(graph)
print(*dfs(v))
print(*bfs(v))