import sys

input = sys.stdin.readline

n, k = map(int, input().split())

w = []
p = []

for i in range(n):
    w1, p1 = map(int, input().split())
    w.append(w1)
    p.append(p1)

# print(w,p)

dp = [0] * (k+1)

for i in range(n):
    if w[i] > k:
        continue
    else:
        for j in range(k, w[i]-1, -1):
            dp[j] = max(dp[j], dp[j-w[i]] + p[i])
    print(dp)

        