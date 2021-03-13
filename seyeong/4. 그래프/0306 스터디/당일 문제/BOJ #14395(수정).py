import sys, collections, math

s, t = map(int, sys.stdin.readline().split())

# 되는 경우
# 1. target이 start의 거듭제곱이고 지수가 2의 거듭제곱일 때
# 2. 1에 해당하고 2가 곱해진 꼴
# 3. target이 2의 거듭제곱 꼴
# 4. 외에는 모두 -1 출력

def bfs(start, target):
    MAX = 10e9
    
    
    
    if target == 0:
        return '-'
    
    if start == target:
        return 0

    if target == 1:
        return '/'

    values = set()
    values.add(start)
    dq = collections.deque()
    dq.append([start, ''])

    # if math.log(target, 2).is_integer():
    #     # print("yes")
    while dq:
        num, path = dq.popleft()
        if num == target:
            return path
        num2 = num * num
        if 0 <= num2 <= MAX and num2 not in values:
            dq.append([num2, path+'*'])
            values.add(num2)
        
        num2 = num + num
        if 0 <= num2 <= MAX and num2 not in values:
            dq.append([num2, path+'+'])
            values.add(num2)

        num2 = 1
        if num2 not in values:
            dq.append([num2, path+'/'])
            values.add(num2)
        
    return -1




    # else:
    
    #     while dq:
    #         num, path = dq.popleft()
    #         if num == MAX:
    #             return path
    #         if num in values or num > target:
    #             continue
    #         values.add(num)
    #         dq.append([num*num, path+'*'])
    #         dq.append([num*2, path+'+'])
    #         # dq.append([1, path+'/'])
    #     return -1

print(bfs(s,t))