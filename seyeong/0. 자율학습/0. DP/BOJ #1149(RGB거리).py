import collections

n = int(input())

R = collections.defaultdict(int)
G = collections.defaultdict(int)
B = collections.defaultdict(int)

R[0], G[0], B[0] = 0, 0, 0

for i in range(1, n+1):
    r, g, b = map(int, input().split())
    R[i] = min(G[i-1], B[i-1]) + r
    G[i] = min(R[i-1], B[i-1]) + g
    B[i] = min(R[i-1], G[i-1]) + b

print(min(R[n], B[n], G[n]))