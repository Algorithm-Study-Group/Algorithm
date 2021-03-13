n = int(input())

arr = [0 for _ in range(n+1)]

arr[1] = 0

for i in range(2, n+1):
    if i % 3 == 0:
        arr[i] = arr[i//3] + 1
    elif i % 2 == 0:
        arr[i] = arr[i//2] + 1
    else:
        arr[i] = arr[i-1] + 1

print(arr[n])