import sys, collections, math

s, t = map(int, sys.stdin.readline().split())

# 되는 경우
# 1. target이 start의 거듭제곱이고 지수가 2의 거듭제곱일 때
# 2. 1에 해당하고 2가 곱해진 꼴
# 3. target이 2의 거듭제곱 꼴
# 4. 외에는 모두 -1 출력

def bfs(start, target):
    
    
    if target == 1:
        return '/'
    
    if target == 0:
        return '-'
    
    if start == target:
        return 0

    values = set()
    dq = collections.deque()
    dq.append([start, ''])

    # if math.log(target, 2).is_integer():
    #     # print("yes")
    while dq:
        num, path = dq.popleft()
        if num == target:
            return path
        if num in values:
            continue
        values.add(num)
        if num*num <= target:
            dq.append([num*num, path+'*'])
        if num*2 <= target:
            dq.append([num*2, path+'+'])
        dq.append([1, path+'/'])
    return -1




    # else:
    
    #     while dq:
    #         num, path = dq.popleft()
    #         if num == target:
    #             return path
    #         if num in values or num > target:
    #             continue
    #         values.add(num)
    #         dq.append([num*num, path+'*'])
    #         dq.append([num*2, path+'+'])
    #         # dq.append([1, path+'/'])
    #     return -1

print(bfs(s,t))