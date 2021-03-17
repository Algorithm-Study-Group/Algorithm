import collections
pos_max = 200000

c_pos, b_pos = map(int, input().split())

def bfs(c_pos, b_pos):
    time = 0
    visited = [[False for _ in range(pos_max+1)] for _ in range(2)]
    q = collections.deque()
    q.append([b_pos, 0])
    while True:
        
        c_pos += time

        if visited[time % 2][c_pos]:
            return time

        if c_pos > pos_max:
            return -1

        for i in range(len(q)):
            cur_pos, next_time = q.popleft()
            next_time = (next_time+1) % 2

            next_pos = cur_pos - 1
            if next_pos >= 0 and not visited[next_time][next_pos]:
                visited[next_time][next_pos] = True
                q.append([next_pos, next_time])
            
            next_pos = cur_pos + 1
            if next_pos <= pos_max and not visited[next_time][next_pos]:
                visited[next_time][next_pos] = True
                q.append([next_pos, next_time])
            
            next_pos = cur_pos * 2
            if next_pos <= pos_max and not visited[next_time][next_pos]:
                visited[next_time][next_pos] = True
                q.append([next_pos, next_time])
            
        

        print(q, c_pos)
        time += 1
        

print(bfs(c_pos, b_pos))
        