import sys, heapq

input = sys.stdin.readline

n = int(input().strip())

cost = list(map(int, input().split()))

heap = []

for cnt, c in enumerate(cost):
    ratio = c / (cnt+1)
    heapq.heappush(heap, [-ratio, cnt+1, -c])

# print(heap)
answer = 0
while heap:
    if n == 0:
        break
    
    r, c, p = heapq.heappop(heap)
    r = -r
    
    p = -p
    
        
    # print(r,c)
    
    while n - c >= 0:
        answer += p
        n -= c

print(int(answer))