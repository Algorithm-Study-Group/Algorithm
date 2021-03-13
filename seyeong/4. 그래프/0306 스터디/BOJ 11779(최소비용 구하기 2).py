import sys, heapq, itertools

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

max_value = sys.maxsize
graph = {}
# heap = []

for i in range(m):
    
    dep, arr, fare = map(int, sys.stdin.readline().split())
    if graph.get(dep-1) is None:
        graph[dep-1] = [(fare, arr-1)]
    else:
        graph[dep-1].append((fare, arr-1))

dep, arr = map(int, sys.stdin.readline().split())
dep, arr = dep-1 , arr-1
# print(graph)

def Dijkstra(Graph, dep):
    distances = [max_value for _ in range(n)]
    distances[dep] = 0
    queue = []
    prev = [ [] for _ in range(n) ]
    prev[dep].append(dep+1)
    heapq.heappush(queue, [distances[dep], dep])
    
    # heapq.heappush(dist, (0, dep))
    # heapq.heapify(dist)
    # print(heapq.heappop(dist))
    # prev[dep] = 0

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        # 저장된 최단거리가 더 작은 경우
        
        if distances[cur_node] < cur_dist:
            continue
        if graph.get(cur_node) is not None:
            
            for fare, adjacent in graph[cur_node]:
                distance = cur_dist + fare
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    prev[adjacent] = prev[cur_node] + [adjacent+1]
                    heapq.heappush(queue, (distance, adjacent))

    print(distances[arr])
    print(len(prev[arr]))
    print(*prev[arr])


Dijkstra(graph, dep)
# print(graph)