t = int(input())

def bridge(n, m):
    answer = 1
    k = m-n

    while m > k:
        answer *= m
        m -= 1

    while n > 1:
            
        answer = answer // n
        n = n-1
    return answer

for _ in range(t):
    n, m = map(int, input().split())
    print(bridge(n, m))