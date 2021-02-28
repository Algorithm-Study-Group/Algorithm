import sys

m, n, h = map(int, sys.stdin.readline().split())

tomato = [ [ [] for _ in range(n)] for _ in range(h)]

# print(tomato[0])

for i in range(h):
    for j in range(n):
        
            
        t = list(map(int, sys.stdin.readline().split()))
        tomato[i][j] = t

pos = [[1, 0, 0], [-1, 0, 0], [0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0]]

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

def bfs(tomato):
    
    cnt = 0 
    # if cnt == 0 and 0 not in tomato:
    #     return 0

    while True:
        stack = []
        possible = True

        # if 0 not in tomato:
        #     return 0

        for i in range(h):
            for j in range(n):
                for k in range(m):
                    if tomato[i][j][k] == 1:
                        for dh, dn, dm in pos:
                            next_h, next_n, next_m = i+dh, j+dn, k+dm
                            if h > next_h >= 0 and n > next_n >= 0 and m > next_m >= 0:
                                if tomato[next_h][next_n][next_m] == 0:
                                    if [next_h, next_n, next_m] not in stack:
                                        stack.append([next_h, next_n, next_m])
                                    print(cnt, stack)   
                    elif tomato[i][j][k] == 0:
                        possible = False
        if not stack:
            if possible:
                return cnt
            else:
                return -1
            
            
        
        while stack:
            i, j, k = stack.pop()
            tomato[i][j][k] = 1
        
        cnt += 1


print(bfs(tomato))