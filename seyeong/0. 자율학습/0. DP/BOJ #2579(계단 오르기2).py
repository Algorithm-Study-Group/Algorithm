import collections
n = int(input())

s = collections.defaultdict(int)
dp = collections.defaultdict(int)

s[0] = 0
dp[0] = 0
for i in range(1, n+1):
    s[i] = int(input())
    if i == 1:
        dp[i] = s[i]
    elif i == 2:
        dp[i] = max(s[0] + s[2], s[1] + s[2])
    else:
        dp[i] = max(dp[i-3] + s[i-1] + s[i],
                dp[i-2] + s[i])

print(dp[n])