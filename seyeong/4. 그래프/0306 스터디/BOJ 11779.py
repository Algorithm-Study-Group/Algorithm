import sys, heapq, collections

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

max_value = sys.maxsize

graph = collections.defaultdict(list)

for _ in range(m):
    dep, arr, weight = map(int, sys.stdin.readline().split())
    graph[dep].append([weight, arr])

dep, arr = map(int, sys.stdin.readline().split())

# print(graph)

def Dijkstra(graph, start):

    distances = [ max_value for _ in range(n+1)]
    distances[start] = 0
    prev = [ [] for _ in range(n+1)]
    prev[start] = [start]
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        for weight, adjacent in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
                prev[adjacent] = prev[current_node] + [adjacent]
    
    print(distances[arr])
    print(len(prev[arr]))
    print(*prev[arr])

Dijkstra(graph, dep)
    


    

