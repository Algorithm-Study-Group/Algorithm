N = int(input())
arr = [list(input()) for _ in range(N)]
def solution():
    foo = False
    stack = []
    for i in range(N):
        for j in range(len(arr[i])):
            if arr[i][j] == "(":
                stack.append("(")
            elif arr[i][j] == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    foo = True
                    break
        if foo:
            print("NO")
            foo = False
        elif len(stack) > 0:
            print("NO")
        else:
            print("YES")
        stack = []


solution()