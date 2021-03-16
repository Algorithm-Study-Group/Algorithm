import sys

input = sys.stdin.readline

n,m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

pack = []
for i in range(n+1):
    pack.append([])
    for c in range(m+1):
        if i == 0 and c == 0:
            pack[i].append(0)

print(pack)