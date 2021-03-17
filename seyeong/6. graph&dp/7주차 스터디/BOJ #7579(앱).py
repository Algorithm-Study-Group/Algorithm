import sys,heapq

input = sys.stdin.readline

n, m = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

ratio = []
for i in range(n):

    if cost[i] == 0:
        heapq.heappush(ratio, [-sys.maxsize, i])
    else:
        r = memory[i]/ cost[i]
        heapq.heappush(ratio, [-r, i])

result = 0
while ratio:

    _, idx = heapq.heappop(ratio)
    print(idx)

    m -= memory[idx]
    result += cost[idx]

    if m <= 0:
        break

print(result)