import collections

s = input().split()
n = int(input())

# print(s)
result = 0
c = collections.Counter(s)

while True:
    sub_count = 0 
    for task, _ in c.most_common(n+1):
        result += 1
        # 실제 문자 개수
        sub_count += 1 

        c.subtract(task)
        # 개수가 0 이하인 아이템을 제거
        c += collections.Counter()
    # n+1 개 중에서 실제 문자 개수만 차감
    # 즉, idle 개수를 더해주는 것과 같음
    # 실제 문자 개수가 n+1 개였으면 idle이 필요 없으므로 0이 더해짐
    if not c:
        break
    result += n + 1 - sub_count
    
        

print(result)

    