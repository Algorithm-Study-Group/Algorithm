import collections

dp = collections.defaultdict(int)

n = int(input())

nums = list(map(int, input().split()))


for i in range(n):

    for j in range(i):

        if nums[i] > nums[j] and dp[j] > dp[i]:
            dp[i] = dp[j]
    
    dp[i] += 1

    # print(dp)


print(max(dp.values()))