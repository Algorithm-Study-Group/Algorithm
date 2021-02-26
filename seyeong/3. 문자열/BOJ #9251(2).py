s1 = input()
s2 = input()

answer = [[0] * len(s1)]
cnt = 0 
i = 0
while i < len(s1):
    substring = s1[i:]
    cnt = 0
    base = substring[cnt]
    for j in range(len(s2)):
        if s2[j] == base:
            answer[i][0] += 1
            cnt += 1
            if cnt < len(s1) - i:
                base = substring[cnt]
            else:
                break
    i+=1 
    print(answer)
            