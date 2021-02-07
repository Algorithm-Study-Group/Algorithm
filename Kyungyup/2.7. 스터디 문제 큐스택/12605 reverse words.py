N = int(input())
arr = [list(input().split(" ")) for _ in range(N)]

def solution():
    stack = ""
    for i in range(0,N):
        for j in range(len(arr[i])-1, -1, -1):
            if j == 0:
                stack += arr[i][j]
            else:
                stack += arr[i][j] + " "

        print("Case #{}: {}".format(i+1, stack))
        stack = ""

solution()