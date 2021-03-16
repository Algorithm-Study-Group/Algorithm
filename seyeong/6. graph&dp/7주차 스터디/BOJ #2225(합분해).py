import math

n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(k)]

for i in range(k):
    for j in range(n+1):
        
        if i == 0:
            dp[i][j] = 1
            
        if i == 1:
            dp[i][j] = j+1
            # if j == 0:
            #     dp[i][j] = 1

        if i > 1:
            for l in range(j+1):
                dp[i][j] += dp[i-1][l]
print(dp[-1][-1])

one = n
zero = k-1

result = math.factorial(one+zero) / math.factorial(n) / math.factorial(k-1)

if k == 1:
    print(1)
else:
    print(int(result))

