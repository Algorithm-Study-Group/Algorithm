import sys, heapq

input = sys.stdin.readline

n = int(input().strip())

cost = list(map(int, input().split()))

cost.insert(0, 0)

dp = [0 for _ in range(n+1)]

dp[1] = cost[1]

# print(cost)

for i in range(2, n+1):
    temp = 0 
    for j in range(0, i+1):
        temp = max(temp, dp[j] + cost[i-j])
    dp[i] = temp

print(dp)