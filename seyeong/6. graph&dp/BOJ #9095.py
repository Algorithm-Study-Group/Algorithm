t = int(input())

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(t):
    n = int(input())
    if n <= 3:
        print(dp[n])
        continue
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
