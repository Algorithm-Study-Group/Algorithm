import collections


n = int(input())

def dp_pibo(n):
    dp = collections.defaultdict(int)

    dp[1], dp[2] = 1, 1
    
    for i in range(3, n+3):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n+2] * 2

print(dp_pibo(n))
