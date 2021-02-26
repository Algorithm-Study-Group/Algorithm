T = int(input())

for _ in range(T):
    ans = []

    F = int(input())
    for _ in range(F):
        answer = set()
        friends = input().split(" ")
        check1, check2 = False, False
        for i in ans:
            if friends[0] in i:
                check1 = True
                answer.update(friends)
                answer = answer | i
            if friends[1] in i:
                check2 = True
                answer.update(friends)
                answer = answer | i
            if check1 or check2:
                ans.append(answer)
        if len(answer) == 0:
            print(2)
        else:
            print(len(answer))

        if not check1 and not check2:
            ans.append(set(friends))
