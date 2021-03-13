# import collections
import sys

input = sys.stdin.readline

t = int(input().strip())

def do_dp(n):

    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = nums[0][0]
    dp[1][0] = nums[1][0]
    dp[0][1] = nums[0][1] + dp[1][0]
    dp[1][1] = nums[1][1] + dp[0][0]

    print(dp)
    if n <= 2:
        return max(dp[0][n-1], dp[1][n-1])

    else:
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + nums[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + nums[1][i]
            # print(dp[0][i])
            # print(dp[1][i])
        return max(dp[0][n-1], dp[1][n-1])

for _ in range(t):
    n = int(input().strip())

    

    nums = [list(map(int, input().split())) for _ in range(2) ]

    print(do_dp(n))
