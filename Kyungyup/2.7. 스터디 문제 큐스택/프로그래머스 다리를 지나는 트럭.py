from collections import deque

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

def solution():
    time = 1
    truck_weights_q = deque(truck_weights)
    truck_ing = deque([])
    time_list = deque([])

    while True:
        if not truck_ing and not truck_weights_q: # 다리에도 없고, 지나갈 것도 없으면
            break
        else:
            if truck_weights_q:
                if sum(truck_ing) + truck_weights_q[0] <= weight: # 다리의 합과 트럭 리스트 빼고 넣고
                    truck_ing.append(truck_weights_q.popleft())
                    time_list.append(bridge_length)
            for i in range(len(time_list)): # 타임리스트에 넣어줌
                time_list[i] -= 1
            if time_list[0] == 0:
                time_list.popleft()
                truck_ing.popleft()
        time += 1 # 시간 추가

    return time

solution()