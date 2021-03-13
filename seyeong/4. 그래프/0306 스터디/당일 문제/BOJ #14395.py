import sys, collections, math

s, t = map(int, sys.stdin.readline().split())

# 되는 경우
# 1. target이 start의 거듭제곱이고 지수가 2의 거듭제곱일 때
# 2. 1에 해당하고 2가 곱해진 꼴
# 3. target이 2의 거듭제곱 꼴
# 4. 외에는 모두 -1 출력

def bfs(start, target):
    result = ''
    
    if target == 1:
        return '/'
    
    if target == 0:
        return '-'
    
    if start == target:
        return 0
    path = prime_factorization(start, target)

    if path:
        # print(path)
        
        counter = collections.Counter(path)
        a = counter[2] # 3 
        b = counter[start] # 2
        
        if int(math.log(b))
        if b == 0:
            temp = ''
            result += '/+'
            while a > 1:
                if a % 2 == 0:
                    temp += '*'
                    a /= 2

                else:
                    temp += '+'
                    a -= 1
            result += temp[::-1]
            return result


        else:
            if int(b) % 2 != 0:
                
                print("no")
                return -1 
            cnt = int(math.log(b ,2))
            if a > 0:
                result += '+'
                temp = 1
                
                while temp*(2**cnt) > a:
                    result += '+'
                    temp += 1
                
                for _ in range(cnt):
                    result += '*'
                    temp *= 2

                while temp == a:
                    result += '+'
                    temp += 1

            else:
                for _ in range(cnt):
                    result += '*'
            

            
            return result
            
            
            
    else:
        return -1

    


def prime_factorization(s, t):
    ls = []
    num = t
    
    for i in [2, s]:

        while ( num % i == 0 ) :
            ls.append(i)
            num = num / i
    if num == 1:
        return ls
    else:
        return False

print(bfs(s, t))