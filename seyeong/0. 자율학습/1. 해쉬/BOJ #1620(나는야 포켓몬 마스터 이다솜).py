import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}
dict2 = {}
for i in range(1,n+1):
    s = sys.stdin.readline().strip()
    dict2[s] = i
    dict[i] = s
    
for i in range(m):
    s = sys.stdin.readline().strip()
    if s.isdigit():
        print(dict[int(s)])
    else:
        print(dict2[s])