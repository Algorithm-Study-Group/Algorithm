import heapq, sys
read = sys.stdin.readline
T = int(read())

def solution(order, num, i):
    if order == "I":
        heapq.heappush(heap_min, [num, i])
        heapq.heappush(heap_max, [-num, i])
        visited[i] = True

    elif order == "D":
        if not heap_max or not heap_min:
            return

        if num == -1: # 최소값 삭제
            while heap_min and not visited[heap_min[0][1]]:
                heapq.heappop(heap_min)

            if heap_min:
                visited[heap_min[0][1]] = False
                heapq.heappop(heap_min)
        elif num == 1:
            while heap_max and not visited[heap_max[0][1]]:
                heapq.heappop(heap_max)

            if heap_max:
                visited[heap_max[0][1]] = False
                heapq.heappop(heap_max)

for _ in range(T):
    k = int(read())
    visited = [False] * 1000001
    heap_max, heap_min = [], []

    for i in range(k):
        order, num = read().split(" ")
        solution(order, int(num), i)

    while heap_max and not visited[heap_max[0][1]]:
        heapq.heappop(heap_max)

    while heap_min and not visited[heap_min[0][1]]:
        heapq.heappop(heap_min)

    if heap_max and heap_min:
        print(-heap_max[0][0], heap_min[0][0])

    else:
        print("EMPTY")