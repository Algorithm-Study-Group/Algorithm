n = int(input())

arr = list(map(int, input().split(" ")))
result = [-1] * n
stack = []

for idx, num in enumerate(arr):
    if not stack:
        stack.append([num, idx])
        continue

    while stack and num > stack[-1][0]:
        n, i = stack.pop()
        result[i] = num
    stack.append([num, idx])
    
print(*result)
# result[n-1] = -1




