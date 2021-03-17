import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [0] * n

for i in range(n):
    temp = list(map(int, input().split()))
    cnt = temp[1]
    if cnt == 0:
        dp[i] = temp[0]
    else:
        longest = 0
        for task in temp[2:]:
            longest = max(dp[task-1], longest)
        dp[i] += longest
        dp[i] += temp[0]
    # print(temp)
print(max(dp))