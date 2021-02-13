from _collections import deque

N = int(input())

def solution():
    queue = []
    count = 0
    for _ in range(N):
        queue.append(input())

    while queue:
        temp = input()
        if queue[0] != temp:
            count += 1
            queue.remove(temp)
        else:
            del queue[0]
    print(count)

solution()