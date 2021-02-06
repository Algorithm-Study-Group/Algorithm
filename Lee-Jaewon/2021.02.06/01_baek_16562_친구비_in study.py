### 1. 스터디에서 풀었을때
# 주어진시간 : 1시간
# DFS에 대해서 알기만했지, 실제로 문제에 적용해본적이 없음
# 알고리즘을 전혀 고려하지 않고 플었기 때문에 문제를 풀 수 없었음
# 시간이 다 끝나기 5분전에 이문제가 DFS문제구나 라는 것을 깨달았음

### 아래의 코드는 한시간 동안 작성한 코드
### 쓸모없음

## 학생수, 친구관계수, 가지고있는돈
N, M, money = map(int, input().split())

## 친구별 가격 입력
price_list = list(map(int, input().split()))


## 친구 관계 입력
relation_array = []
for _ in range(M):
    v, w = map(int, input().split())
    relation_array.append([v, w])





## 친구번호와 친구가격을 하나의 튜플로 만들자
total_money = 0
while relation_array:
    price_list_with_index = [(friend_idx+1, price) for friend_idx, price in enumerate(price_list)]
    friend_idx, friend_price = min(price_list_with_index, key=lambda x : x[1])

    total_money += price_list[friend_idx-1]

    temp = [relation_list for relation_list in relation_array if friend_idx in relation_list]
    relatrion_friend_list = list(set(sum(temp, [])))

    for idx in relatrion_friend_list :
        price_list[idx-1] = float('inf')
    relation_array = [relation_list for relation_list in relation_array if friend_idx not in relation_list]

    print(price_list_with_index)
    print(total_money)


if total_money <= money:
    print(total_money)
else :
    print('Oh no')


