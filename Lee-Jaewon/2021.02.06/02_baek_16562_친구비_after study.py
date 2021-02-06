## 2. 스터디 후 다시풀기

## 재귀함수는 보통 횟수가 지정되어있음
## 백준은 1,000번 > 1,000번 넘어가면 런타임에러
## 이러한 재귀함수 횟수에 대한 상한선을 제거하기 위해
## 다음과 같은 코드를 사용
import sys
sys.setrecursionlimit(10**9)




############ (1) 입력
## 학생수, 친구관계수, 가지고있는 돈 입력
N, M, money = map(int, input().split())

## 친구비를 담은 리스트 입력
friend_price_list = list(map(int, input().split()))

## 친구관계입력
relation_graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    v, w = map(int, input().split())
    relation_graph[v].append(w)
    relation_graph[w].append(v)
    

############### (2) DFS구현

def DFS(graph, node, visited, friend_price_list):
    visited[node] = True
    friend_price_list[node-1] = float('inf')
    
    for linked_node in graph[node] :
        if not visited[linked_node]:
            DFS(graph, linked_node, visited, friend_price_list)


############### (3) 
total_money = 0

while sum(visited) != N :
    min_price = min(friend_price_list)
    min_price_index = friend_price_list.index(min_price) + 1

    total_money += min_price
    DFS(relation_graph, min_price_index, visited, friend_price_list)

    
if total_money <= money :
    print(total_money)
else :
    print('Oh no')








