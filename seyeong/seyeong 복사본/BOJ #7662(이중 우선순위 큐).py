import heapq
import collections

T = int(input())

for _ in range(T):
    k = int(input())
    maxheap, minheap = [], []
    c = collections.defaultdict(int)
    for _ in range(k):
        operator, num = input().split(" ")
        num = int(num)
        if operator == 'I':
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
            c[num] += 1
        else:
            if num == 1:
                while maxheap and c[-maxheap[0]] == 0:
                    heapq.heappop(maxheap)
                if maxheap:
                    c[-1 * maxheap[0]] -= 1
                    heapq.heappop(maxheap)
                    
            
            else:
                while minheap and c[minheap[0]] == 0:
                    heapq.heappop(minheap)
                if minheap:
                    c[minheap[0]] -= 1
                    heapq.heappop(minheap)
                    

    while maxheap and c[-maxheap[0]] == 0:
        heapq.heappop(maxheap)
    while minheap and c[minheap[0]] == 0:
        heapq.heappop(minheap)
    
    if maxheap or minheap:
        print(-maxheap[0], minheap[0])
    else:
        print("EMPTY")




