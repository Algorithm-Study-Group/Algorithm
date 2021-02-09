import heapq, collections, sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    minheap, maxheap = [], []
    c = collections.defaultdict(int)
    for _ in range(n):
        operator, num = sys.stdin.readline().split()
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
                    a = heapq.heappop(maxheap)
                    c[-a] -= 1

            else:
                while minheap and c[minheap[0]] == 0:
                    heapq.heappop(minheap)
                if minheap:
                    a = heapq.heappop(minheap)
                    c[a] -= 1
        
        

    while minheap and c[minheap[0]] == 0:
        heapq.heappop(minheap)
    while maxheap and c[-maxheap[0]] == 0:
        heapq.heappop(maxheap)
            
    if minheap or maxheap:
        print(-maxheap[0], minheap[0])
    else:
        print("EMPTY")
        

# print(minheap, maxheap)