import sys, heapq

input = sys.stdin.readline

n = int(input().strip())

tasks = []

for i in range(n):
    s, e = map(int, input().split())
    tasks.append([s,e])

tasks.sort(key=lambda x: x[0])

# for i in range(n):
#     # print(heapq.heappop(tasks))
#     print(heapq.nsmallest(1, tasks))

queue = []

heapq.heappush(queue, tasks[0][1])

for i in range(1, n):
    if queue[0] > tasks[i][0]:
        heapq.heappush(queue, tasks[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, tasks[i][1])

    # print(queue)
print(len(queue))