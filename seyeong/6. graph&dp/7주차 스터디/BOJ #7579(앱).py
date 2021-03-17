import sys,heapq

input = sys.stdin.readline

n, m = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
S = sum(cost)
dp = [0] * (S+1)
# print(dp)


# 총 코스트부터 얻을 수 있는 최대 메모리 조사
# 각 작업이 들어갔을 때 기존 메모리보다 크면 작업 포함
for i in range(n):
    for j in range(S, cost[i]-1, -1):
        dp[j] = max(dp[j], dp[j-cost[i]]+memory[i])
    # print(dp)

for i in range(S):
    if dp[i] >= m:
        print(i)
        break



# def knapsack2(i, W, w, c):
    
#     if i <= 0:
#         return 101

#     # print(i, W, w[i], c[i])

#     if w[i] < W:
#         return knapsack2(i-1, W-w[i], w, c)
    
#     else:
#         left = knapsack2(i-1, W, w, c)
#         right = knapsack2(i-1, W - w[i], w, c)
#         print(left, right+c[i])
#         return min(left, c[i]+right)


# print(knapsack2(n-1, m, memory, cost))