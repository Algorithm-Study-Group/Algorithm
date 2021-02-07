from _collections import  deque
progresses =[95, 90, 99, 99, 80, 99]
dq = deque(progresses)
print(dq)
speeds = [1, 1, 1, 1, 1, 1]
ans = []
def solution():
    while dq:
        while dq[0] < 100:
            count = 0
            for i in range(len(dq)):
                dq[i] += speeds[i]

        while True:
            if dq[0] >= 100:
                count += 1
                dq.popleft()
                speeds.popleft()
                if not dq:
                    break
            else:
                break
        ans.append(count)
        count = 0
    print(ans)




solution()