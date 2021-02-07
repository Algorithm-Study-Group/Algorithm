from collections import deque
arr = list(input())

def solution():
    dq = deque(["("])
    count = 0
    for i in range(1, len(arr)):
        if arr[i] == ")" and arr[i-1] == "(": # 레이저 커트 부분
            dq.popleft()
            count += len(dq)
        elif arr[i] == "(": # 새로 막대가 시작하는
            dq.append("(")
        elif arr[i] == ")": # 막대가 끝나는 부분
            count += 1
            dq.popleft()
    print(count)
solution()