from _collections import deque

priorities = [2, 1, 3, 2]
location = 2
def solution():
    global location
    dq = deque(priorities)
    count = 0
    while True:
        max_value = max(dq) # 최대값이 뭔지 구해줌
        if location == 0 and max_value == dq[location]: # 만약 최대 우선순위가 출력된다면
            count += 1
            break

        temp = dq.popleft() # 뺴주고
        if max_value == temp: #최대값이면
            count += 1
        else:
            dq.append(temp) # 뒤에 넣어줌
        if location == 0:
            location = len(dq) - 1
        else:
            location -= 1
    return count
solution()